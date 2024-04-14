from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Base URL of the Quoters service running on localhost
QUOTERS_BASE_URL = "http://host.docker.internal:8080/api"

@app.route('/fetch-random-quote')
def fetch_random_quote():
    response = requests.get(f"{QUOTERS_BASE_URL}/random")
    logging.info(f'Random Quote: {response.json()}')
    return jsonify(response.json())

@app.route('/fetch-quote/<int:quote_id>')
def fetch_quote(quote_id):
    response = requests.get(f"{QUOTERS_BASE_URL}/{quote_id}")
    logging.info(f'Quote ID {quote_id}: {response.json()}')
    return jsonify(response.json())

if __name__ == '__main__':
    # Set host to 0.0.0.0 to make the server visible externally
    app.run(host='0.0.0.0', port=5000)
