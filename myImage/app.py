from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
	key = os.environ.get("SECRET_KEY")
	return "<h1>Welcome to the world of Docker! YOU'RE MINE NOW!!! {}</h1>".format(key)

app.run(host="0.0.0.0", port="5000") #int(port)
