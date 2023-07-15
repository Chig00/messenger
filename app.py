import time
import collections
import flask

app = flask.Flask(__name__)

MAX_MESSAGES = 25

#
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
    
    print(flask.render_template("index.html", name = name, messages = messages))
    
    return flask.render_template("index.html", name = name, messages = messages)