from flask import request, jsonify, Blueprint
from api import app
from api.controllers.incident_controller import IncidentController

b_print = Blueprint("incident_view", __name__, url_prefix="/api/v1")
redflag_obj = IncidentController()

# A landing Page welcome message endpoint
@b_print.route('/', methods=['GET'])
def home_welcome_message():
    return redflag_obj.index()

# create a red-flag end-point
@b_print.route('/red-flags', methods=['POST'])
def create_new_redflag():
    return redflag_obj.create_redflag()

# get all red-flags end-point
@b_print.route('/red-flags', methods=['GET'])
def get_all_created_redflags():
    return redflag_obj.get_all_redflags()

# get a single red-flag by its id endpoint
@b_print.route('/red-flags/<int:red_flag_id>', methods=['GET'])
def get_specific_redflag(red_flag_id):
    return redflag_obj.get_redflag(red_flag_id)

# delete a single red-flag record by its id endpiont
@b_print.route('/red-flags/<int:red_flag_id>', methods=['DELETE'])
def delete_specific_record(red_flag_id):
    return redflag_obj.delete_record(red_flag_id)

# edit specific red-flag record location endpoint
@b_print.route('/red-flags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_specific_location(red_flag_id):
    return redflag_obj.edit_location_and_comment(red_flag_id)

# edit specific red-flag record  comment endpoint
@b_print.route('/red-flags/<int:red_flag_id>/comment', methods=['PATCH'])
def edit_specific_comment(red_flag_id):
    return redflag_obj.edit_location_and_comment(red_flag_id)