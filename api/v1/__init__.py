from flask import Flask

app = Flask(__name__)

from api.v1.views import views