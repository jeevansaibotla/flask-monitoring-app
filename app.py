from flask import Flask
from prometheus_client import Counter, generate_latest
import redis
import os

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

REQUEST_COUNT = Counter('flask_request_count', 'Total number of requests')

@app.route('/')
def index():
    r.incr('hits')
    REQUEST_COUNT.inc()
    count = r.get('hits').decode('utf-8')
    return f"<h1>Flask + Redis + Prometheus</h1><p>This page has been visited <b>{count}</b> times.</p>"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
