# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, jsonify
import grequests
import json

app = Flask(__name__)

@app.route('/api/login', methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    login_data = json.loads(request.get_data())
    r = grequests.get(
      "http://prodv1.tjut.cc/api/login/",
      params={
        "account": login_data['username'],
        "password": login_data['password']
      })
    r = grequests.map([r])[0]
    return jsonify(r.json())
