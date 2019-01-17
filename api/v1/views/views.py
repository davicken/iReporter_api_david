from flask import request, jsonify
from api.v1 import app
from api.v1.models.redflags import RedFlag

# validations
from api.v1.controllers.controller import validate_string
# from api.v1.controllers.controller import required_image_field 
# from api.v1.controllers.controller import comment_length

from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")



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
    inc_type = "red-flag"
    createdBy = data.get('createdBy')
    createdOn = current_time
    location = data.get ('location')
    status = data.get('status')
    comment = data.get('comment')
    images = data.get('images')
    videos = data.get('videos')


    try:
        # validate_string(data['inc_type'])
        # required_image_field (data['images'])
        # comment_length (data['comment']) 
        flag_record = RedFlag(inc_type, inc_id,location, createdOn, createdBy, status, comment, images, videos)
        redflags.append(flag_record)
    except ValueError as e:
        print(e)
        return jsonify({'status': 400, 'message': 'location should be a string'})
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
        return jsonify({ 'status' : 400, 'message': 'There are no red-flag records'})
    return jsonify({'status' : 200, 'redflags': json_redflags})
