# File to handle tests for all red-flags endpoints
import unittest
from flask import request
import json
from api import app
from api.models.incident_model import RedFlag, IncidentData
from api.controllers.incident_controller import my_redflags


class TestRedflagEndPoints(unittest.TestCase):
    # Class for testing the red-flag endpoints
    def setUp(self):
        self.test_app = app.test_client(self)

 
    def tear_down(self):
        my_redflags.redflags.clear()
       
    def test_index(self):
        response = self.test_app.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        my_data = response.data.decode()
        message = {
            "message": [
                    "Welcome to Mwesigwa\'s iReporter APIs home",
                    "Endpoints",
                    "#1 : GET /api/v1/red-flags",
                    "#2 : GET /api/v1/red-flags/<red_flag_id>",
                    "#3 : POST /api/v1/red-flags",
                    "#4 : PATCH /api/v1/red-flags/<red_flag_id>/location",
                    "#5 : PATCH /api/v1/red-flags/<red_flag_id>/comment",
                    "#6 : DELETE /api/v1/red-flags/<red_flag_id>"
                    ]
        }
        self.assertEqual(json.loads(my_data), message)

    def test_all_redflags_when_not_empty(self): 
        # test that the red-flag data posted can all be retrieved & not empty
        input_data1 = {
            "title": "corruption at the office",
            "images": ["image1", "image2"],
            "videos": ["video1", "video2"],
            "comment": "corruption has become a menace",
            "location": {"lat": "0.3333", "long": "1.0444"}
        }
        self.test_app.post('/api/v1/red-flags', content_type='application/json', data=json.dumps(input_data1), headers={'userId': 1})
        input_data2 = {
            "title": "embezzlement of funds",
            "images": ["image3", "image4"],
            "videos": ["video7", "video8"],
            "comment": "embezzlement is real evil",
            "location": {"lat": "0.3443", "long": "1.4334"}
        }
        post_resp = self.test_app.post('/api/v1/red-flags', content_type='application/json', data=json.dumps(input_data2), headers={'userId': 1})
        self.assertEqual(post_resp.status_code,201)
        response = self.test_app.get('/api/v1/red-flags')
        self.assertEqual(response.status_code, 200)

        my_data = json.loads(response.data.decode())
        self.assertEqual(len(my_data['data']), 2)
        self.assertEqual(my_data['data'][1]['title'], "embezzlement of funds")
        self.assertEqual(my_data['data'][1]['comment'], "embezzlement is real evil")
        self.assertEqual(my_data['data'][0]['images'], ["image1", "image2"])
        self.assertEqual(my_data ['data'][0]['location'], {"lat": "0.3333", "long": "1.0444"})
        self.assertEqual(my_data ['data'][0]['id'], 1)

    def test_all_redflags_when_empty(self):
        response = self.test_app.get('/api/v1/red-flags')
        my_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        # *****************************************
        # response status_code susposed to be 400
        self.assertIn('no red-flag records', my_data['error'])

    def test_create_redflag(self):
        # test whether the status code and data after creating a redflag can be retieved correctly
        input_data = {
            "title": "corruption at the office",
            "images": ["image1", "image2"],
            "videos": ["video1", "video2"],
            "comment": "corruption has become a menace",
            "location": {"lat": "98854", "long": "888484"}
            }
        post_resp = self.test_app.post(
            '/api/v1/red-flags', content_type='application/json', data=json.dumps(input_data), headers={'userId': 1})
        self.assertEqual(post_resp.status_code, 201)
        response = json.loads(post_resp.data.decode())
        my_data = response['data']
        self.assertEqual(response['status'], 201)
        self.assertEqual(my_data[0]['message'], "created red-flag record successfully")

    def test_create_redflag_with_wrong_comment(self):
        input_data = {
            "title": "corruption at the office",
            "images": ["image1", "image2"],
            "videos": ["video1", "video2"],
            "comment": 2,
            "location": {"lat": "98854", "long": "888484"}
            }
        response = self.test_app.post('/api/v1/red-flags', content_type='application/json', data=json.dumps(input_data), headers={'userId': 1})
        self.assertEqual(response.status_code, 200)
        # *************************************
        # status code susposed to be 400
    
   