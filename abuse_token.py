# vulnerable_api.py
# Educational example showing API token abuse — DO NOT DEPLOY IN PRODUCTION.
# Usage (lab only):
#   GET /user/2?api_token=token-for-user-1  <- token validated but NOT checked against requested resource

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory "database" for demo only
USERS = {
    1: {"id": 1, "username": "alice", "email": "alice@example.local"},
    2: {"id": 2, "username": "bob", "email": "bob@example.local"},
}

# Simple token -> user_id mapping (demo)
TOKENS = {
    "token-user-1": 1,
    "token-user-2": 2,
    # NOTE: tokens exist, but the app below does NOT enforce that the token owner
    # matches the requested resource, which allows abuse.
}

def get_user_by_id(user_id):
    return USERS.get(user_id)

@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # Token supplied as query param (bad practice) or header
    token = request.args.get("api_token") or request.headers.get("X-API-Token")
    if not token or token not in TOKENS:
        abort(401, description="Invalid or missing API token")

    # VULNERABILITY:
    # The code only checks that the token exists; it does NOT verify that the
    # token's owner is allowed to access the requested user_id.
    user = get_user_by_id(user_id)
    if not user:
        abort(404, description="User not found")

    # Sensitive info returned even if token belongs to a different user
    return jsonify(user)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
