from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/your_script.py', methods=['POST'])
def handle_post():
    data = request.get_json()
    result = {'message': 'Data received successfully', 'data': data}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)