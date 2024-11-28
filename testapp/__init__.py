from flask import Flask
from testapp import config

app = Flask(__name__)
app.config.from_object(config)

import testapp.views
