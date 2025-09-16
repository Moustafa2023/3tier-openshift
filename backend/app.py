from flask import Flask, jsonify, request
import os, psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST','db-service')
DB_NAME = os.environ.get('DB_NAME','appdb')
DB_USER = os.environ.get('DB_USER','appuser')
DB_PASS = os.environ.get('DB_PASS','apppass')
DB_PORT = os.environ.get('DB_PORT','5432')

def get_conn():
    return psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)

@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT);")
    cur.execute("SELECT id, name FROM items ORDER BY id DESC;")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return jsonify([{'id': r[0], 'name': r[1]} for r in rows])

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.json or {}
    name = data.get('name','no-name')
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO items (name) VALUES (%s) RETURNING id;', (name,))
    conn.commit()
    new_id = cur.fetchone()[0]
    cur.close(); conn.close()
    return jsonify({'id': new_id, 'name': name}), 201

@app.route('/health')
def health():
    return jsonify({'status':'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '8080')))
