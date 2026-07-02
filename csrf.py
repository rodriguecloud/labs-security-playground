from flask import Flask, request

app = Flask(__name__)

# VULNERABILITY: This route changes the user's password without a CSRF token.
# An attacker can force a logged-in user to hit this URL and change their password.
@app.route('/update-password', methods=['POST'])
def update_password():
    new_password = request.form['password']
    # Logic to update password in database
    return "Password updated successfully!"
