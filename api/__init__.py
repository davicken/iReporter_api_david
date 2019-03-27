from flask import Flask
app = Flask(__name__, instance_relative_config=True)

from api.views import incident_view
app.register_blueprint(incident_view.b_print)
