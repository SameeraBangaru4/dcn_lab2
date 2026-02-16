from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    now = datetime.utcnow().isoformat() + 'Z'
    return jsonify({"time": now})

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
