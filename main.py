from flask import Flask, request, jsonify
from googleRobot import execute
app = Flask(__name__)

@app.route("/google", methods=["POST"])
def searchInGoogle():
    data = request.get_json()
    search_for = data.get('search_for')
    pages = data.get('pages')

    return jsonify(execute(search_for, pages))

if __name__ == "__main__":
    app.run(debug=True)