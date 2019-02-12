# from flask import json

# from api.helpers.responses import supported_end_points


# def test_invalid_url(client):
#     response = client.delete("api/v1/")
#     assert response.status_code == 404
#     data = json.loads(response.data.decode())
#     assert data["supportedEndPoints"] == supported_end_points
#     assert data["error"] == "Endpoint for specified URL does not exist"
