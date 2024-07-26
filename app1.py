from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post-data', methods=['POST'])
def post_data():
    # Check if the request contains JSON data
    if request.is_json:
        data = request.get_json()
        # Process the JSON data (for demonstration, just echo it back)
        return jsonify({'received_data': data}), 200
    else:
        return jsonify({'error': 'Request must be JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)
