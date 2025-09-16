from flask import Flask, render_template, jsonify
import os, requests

app = Flask(__name__, template_folder='templates')

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://backend-service:8080')

@app.route('/')
def index():
    return render_template('index.html', backend_url=BACKEND_URL)

@app.route('/health')
def health():
    return jsonify({"status":"ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
