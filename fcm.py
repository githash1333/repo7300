from flask import Flask, jsonify, request
import socket
def get_local_ip_address():
    try:
        # Connect to an external server to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Using Google DNS server address
        local_ip_address = s.getsockname()[0]
        s.close()
        return local_ip_address
    except Exception as e:
        print(f"Unable to get local IP address: {e}")
        return None
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
    app.run(host=get_local_ip_address(),port=8421)
