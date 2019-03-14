from flask import Flask
app = Flask(__name__, instance_relative_config=True)

from api.views import incident_view, users_view, auth_view
app.register_blueprint(incident_view.b_print)
app.register_blueprint(users_view.ub_print)
app.register_blueprint(auth_view.authb_print)
