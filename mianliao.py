from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        logindata = {
            "account": username,
            "password": password
        }

        r = requests.get("http://prod.tjut.cc/api/login", params = logindata)

        userstatus = json.loads(r.text)

        if(userstatus['code'] != 1):
            return render_template('index.html', error = "用户名或密码错误")
        else:
            userstatus = userstatus['response']
            uid = userstatus['uid']
            token = userstatus['token']
            url = "http://stage.tjut.cc/login/do_counselor?1=1&uid=" + uid + "&token=" + token
            return render_template('index.html', url = url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
