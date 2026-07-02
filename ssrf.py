from flask import Flask, request
import requests

app = Flask(__name__)

# VULNERABILITY: The server fetches the URL provided by the user.
# An attacker can use this to scan internal networks or access metadata services (e.g., http://169.254.169.254/)
@app.route('/fetch-url')
def fetch_url():
    target_url = request.args.get('url')
    
    # The server performs the request on behalf of the user
    response = requests.get(target_url)
    return response.text
