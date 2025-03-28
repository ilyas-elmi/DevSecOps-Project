from flask import Flask, request, jsonify
import sqlite3
import jwt  # PyJWT library

app = Flask(__name__)
SECRET_KEY = "supersecret"

# SQL Injection
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Unsafe query (SQL Injection vulnerability)
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    result = cursor.fetchone()
    return jsonify(success=bool(result))

# Insecure JWT handling
@app.route('/token', methods=['GET'])
def token():
    username = request.args.get('username', 'guest')
    # JWT token generated with none algorithm (insecure)
    token = jwt.encode({"user": username}, key=None, algorithm="none")
    return jsonify(token=token)

# Sensitive data in logs
@app.route('/submit-card', methods=['POST'])
def submit_card():
    card_number = request.form.get('card')
    print(f"Received card number: {card_number}")  # Logging sensitive info
    return "Card submitted!"