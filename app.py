import time
import collections
import flask

MAX_MESSAGES = 25

app = flask.Flask(__name__)
messages = collections.deque()

@app.route("/", methods = ["GET", "POST"])
def index():
    name = flask.request.values.get("name")
    message = flask.request.values.get("message")
    
    if name and message:
        messages.appendleft((
            time.asctime(),
            name,
            message
        ))
        
        if len(messages) > MAX_MESSAGES:
            messages.pop()
    
    return flask.render_template("index.html", name = name, messages = messages)