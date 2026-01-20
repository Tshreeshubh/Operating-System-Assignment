from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    content = request.json
    user_message = content.get('message', '')
    
    server_response = f"{user_message} - [Verified by Shreeshubh REST API]"
    
    return jsonify({
        "status": "success",
        "reply": server_response
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
