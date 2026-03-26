from flask import Flask, request, jsonify
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/')
def home():
    return 'PS3 Browser Server is running!'

@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        return jsonify({
            'content': response.text,
            'status': response.status_code
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
