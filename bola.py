from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated Database
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

@app.route('/api/user/<int:user_id>')
def get_user_profile(user_id):
    # VULNERABILITY: No check is performed to see if the requesting user 
    # has permission to view the requested user_id.
    user = users.get(user_id)
    
    if user:
        return jsonify(user)
    return "User not found", 404
