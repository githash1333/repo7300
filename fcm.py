from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the basic Flask API!"

@app.route('/get-data', methods=['GET'])
def get_data():
    # Example data to return
    data = {
        "Title": "VM-TEST",
        "Body": "Body of this test message.",
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
