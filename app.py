from flask import Flask, jsonify
from mysql_db import get_mysql_connection
from mongo_db import get_mongo_collection

app = Flask(__name__)

@app.route("/user/<int:id>")
def get_user(id):
    # Check in MongoDB first
    users = get_mongo_collection()
    user = users.find_one({"id": id}, {"_id": 0})
    if user:
        return jsonify(user)
    
    # Fallback to MySQL
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (id,))
    row = cursor.fetchone()
    if row:
        return jsonify({"id": row[0], "name": row[1], "email": row[2]})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
