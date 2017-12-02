from flask import Flask, request, render_template, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        login_data = json.loads(request.get_data())

        username = login_data['username']
        password = login_data['password']
        
        login = {
            "account": username,
            "password": password
        }
        login_url = "http://prodv1.tjut.cc/api/login/"
        r = requests.get(login_url, params = login)

        return jsonify(r.json())

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
