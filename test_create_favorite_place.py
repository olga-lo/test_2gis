import unittest
import requests


class TestCreateFavoritePlace(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://regions-test.2gis.com"
        self.token_url = f"{self.base_url}/v1/auth/tokens"
        self.favorites_url = f"{self.base_url}/v1/favorites"

        # Получение сессионного токена
        token_response = requests.post(self.token_url)
        self.assertEqual(token_response.status_code, 200, "Failed to get session token")

        # Извлечение токена из заголовка Set-Cookie
        self.cookie = token_response.headers.get("Set-Cookie")
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': self.cookie
        }


    def test1_create_favorite_place(self):
        self.data = {
            'title': 'Своя компания',
            'lat': '53.629757',
            'lon': '55.905509'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 200, "Expected status code to be 200 OK")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('id', json_response, "Response JSON should contain 'id'")
        self.assertEqual(json_response['title'], self.data['title'], "Title does not match")
        self.assertEqual(json_response['lat'], float(self.data['lat']), "Latitude does not match")
        self.assertEqual(json_response['lon'], float(self.data['lon']), "Longitude does not match")
        self.assertIsNone(json_response['color'], "Color should be null")
        self.assertIn('created_at', json_response, "Response JSON should contain 'created_at'")


    def test2_create_favorite_place_non_authorized(self):
        self.data = {
            'title': 'Своя компания',
            'lat': '53.629757',
            'lon': '55.905509'
        }
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': ""
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 401, "Expected status code to be 401 Unauthorized")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test3_create_favorite_place_non_title(self):
        self.data = {
            'lat': '53.629757',
            'lon': '55.905509'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test4_create_favorite_place_title_empty(self):
        self.data = {
            'title': '',
            'lat': '53.629757',
            'lon': '55.905509'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test5_create_favorite_place_title_1000(self):
        self.data = {
            'title': 'стосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстостосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволов123456789fdsaqsdfghryeijkslсимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимволовстосимвоооловстосимвов123456789fdsaqsdfghryeijksl',
            'lat': '53.629757',
            'lon': '55.905509'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test6_create_favorite_place_title_symbols(self):
        self.data = {
            'title': 'Вкусно и @#$%^&*',
            'lat': '53.629757',
            'lon': '55.905509'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test7_create_favorite_place_title_non_lat(self):
        self.data = {
            'title': 'Вкусно и вкусно',
            'lon': '55.905509'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test8_create_favorite_place_title_lat_more_90(self):
        self.data = {
            'title': 'Вкусно и вкусно',
            'lat': '91',
            'lon': '55.905509'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test9_create_favorite_place_title_non_lon(self):
        self.data = {
            'title': 'Вкусно и вкусно',
            'lat': '55.905509'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test10_create_favorite_place_title_lon_more_180(self):
        self.data = {
            'title': 'Вкусно и вкусно',
            'lat': '55.905509',
            'lon': '181'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

    def test11_create_favorite_place_color_is_right(self):
        self.data = {
            'title': 'Своя компания',
            'lat': '53.629757',
            'lon': '55.905509',
            'color': 'RED'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        json_response = response.json()
        self.assertEqual(response.status_code, 200, "Expected status code to be 200 OK")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('id', json_response, "Response JSON should contain 'id'")
        self.assertEqual(json_response['title'], self.data['title'], "Title does not match")
        self.assertEqual(json_response['lat'], float(self.data['lat']), "Latitude does not match")
        self.assertEqual(json_response['lon'], float(self.data['lon']), "Longitude does not match")
        self.assertEqual(json_response['color'], self.data['color'], "Color does not match")
        self.assertIn('created_at', json_response, "Response JSON should contain 'created_at'")

    def test12_create_favorite_place_color_is_wrong(self):
        self.data = {
            'title': 'Своя компания',
            'lat': '53.629757',
            'lon': '55.905509',
            'color': 'BLACK'
        }
        response = requests.post(self.favorites_url, headers=self.headers, data=self.data)

        # Проверка статус-кода
        self.assertEqual(response.status_code, 400, "Expected status code to be 400 Bad Request")

        # Проверка тела ответа
        json_response = response.json()
        self.assertIn('error', json_response, "Response JSON should contain 'error'")
        self.assertIn('id', json_response['error'], "Error should contain 'id'")
        self.assertIn('message', json_response['error'], "Error should contain 'message'")

if __name__ == '__main__':
    unittest.main()
