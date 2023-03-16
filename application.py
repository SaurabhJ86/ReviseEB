from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "Hello World, this is your Lord, Sir Henser Dufrey. This shall be taken along with a sense of urgency."