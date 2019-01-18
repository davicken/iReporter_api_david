import unittest
import json
from api.v1 import app

class TestRedflags(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_all_redflags(self):
        input_data = {'inc_id': 1, 'location': 'createdOn', 'createdBy': 20}
        self.app_tester.post('/redflags', json=input_data)
        input_data = {'inc_id': 2, 'location': 'Super', 'createdBy': 30}
        self.app_tester.post('/redflags', json=input_data)

        response = self.app_tester.get('/redflags')
        print(response)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['redflags']), 2)
        self.assertEqual(data['redflags'][0]['inc_id'], 1)
        self.assertEqual(data['redflags'][0]['location'], 'createdOn date')

    def test_all_redflags_when_empty(self):
        response = self.app_tester.get('/redflags')
        print(response)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('no redflags', data['message'])

    def test_add_redflags(self):
        input_data = {'inc_id': 1, 'location': 'createdOn', 'createdBy': 2}
        response = self.app_tester.post('/redflags', json=input_data)
        self.assertEqual(response.status_code, 201)

    def test_add_product_wrong_createdBy(self):
        input_data = {'inc_id': 1, 'location': 'createdOn', 'createdBy': 'two'}
        response = self.app_tester.post('/redflags', json=input_data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()