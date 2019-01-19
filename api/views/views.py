from flask import request, jsonify, request
from api import app
from api.models.redflags import RedFlag
from api.controllers.controller import validate_string

redflags = []

# A testing end-point
@app.route('/')
def index():
    return jsonify({"message": "Welcome to my iReporter home"})

# create a red-flag end-point
@app.route('/api/v1/redflags', methods=['POST'])
def create_redflag():
    data = request.get_json()
    inc_id = len(redflags)+1
    location = data.get('location')
    comment = data.get('comment')
    images = data.get('images')
    videos = data.get('videos')

    try:
        validate_string(data['comment'])
        flag_record = RedFlag(id=inc_id, loc=location, comment=comment, image =images, vid=videos)
        redflags.append(flag_record)
    except ValueError :
        return jsonify({'status': 400, 'message': 'comment should be a string'})
    return jsonify({'status': 201, 'redflags': [flag_record.to_json()]})

# get all red-flags end-point
@app.route('/api/v1/redflags', methods=['GET'])
def get_all_redflags():
    json_redflags = []
    print(redflags)
    for redflag in redflags:
        json_redflags.append(redflag.to_json())

    print(json_redflags)
    print(len(json_redflags))
    if len(json_redflags) < 1:
        return jsonify({'status': 400, 'message': 'There are no red-flag records'})
    return jsonify({'status': 200, 'redflags': json_redflags})
