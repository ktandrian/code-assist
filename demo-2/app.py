from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Konfigurasi koneksi ke PostgreSQL
app.config['DATABASE_URI'] = 'postgresql://user:password@host:port/database'

# Fungsi untuk membuat koneksi ke database
def get_db_connection():
    conn = psycopg2.connect(app.config['DATABASE_URI'])
    return conn

# Endpoint untuk mendapatkan data user berdasarkan user ID
@app.route('/users/<int:user_id>')
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

# Endpoint untuk mendapatkan semua user ID
@app.route('/users')
def get_all_user_ids():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users")
    user_ids = cursor.fetchall()
    conn.close()

    return jsonify(user_ids)

if __name__ == '__main__':
    app.run(debug=True)
