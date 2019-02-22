# from flask import json

    
# def test_index(self):
#     # test for whether the default root url returns the correct message
#     response = self.test_app.get('/api/v1/')
#     self.assertEqual(response.status_code, 200)
#     my_data = response.data.decode()
#     message = {
#         "message": [
#                 "Welcome to Mwesigwa\'s iReporter APIs home",
#                 "Endpoints",
#                 "#1 : GET /api/v1/red-flags",
#                 "#2 : GET /api/v1/red-flags/<red_flag_id>",
#                 "#3 : POST /api/v1/red-flags",
#                 "#4 : PATCH /api/v1/red-flags/<red_flag_id>/location",
#                 "#5 : PATCH /api/v1/red-flags/<red_flag_id>/comment",
#                 "#6 : DELETE /api/v1/red-flags/<red_flag_id>"
#                 ]
#     }
#     self.assertEqual(json.loads(my_data), message)