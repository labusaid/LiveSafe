from flask import Flask, render_template, request, redirect, url_for
import Risk
from requests import get
from threading import Thread
import time

url = "http://192.168.8.234:8123/api/states/"
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI4MjgxYzRkZmQzMzU0YTdkYjFmZDU5ZDZhODRhODI4YiIsImlhdCI6MTU4MTg2MzA5NSwiZXhwIjoxODk3MjIzMDk1fQ.vBI97CKTnF4ze6f8z6KGqVDn0XVIT88wKa_gjS05wiE",
    "content-type": "application/json",
}
responses = {"timeCount": 0, "doorCount": 0, "windowCount": 0, "smokeCount": 0}

app = Flask(__name__)

riskA = Risk.Risk()

@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            return redirect('/index')
        except:
            return 'There was an issue adding your task'

    else:
        return render_template("index.html", values = responses)

@app.route('/')
def home():
    return render_template("home_page.html")

@app.route('/delete/<task_id>')
def delete(task_id):
    try:
        return redirect('/index')
    except:
        return 'There was a problem deleting that task'


if __name__ == '__main__':
    app.run()

@app.route('/risk')
def risk():
    return render_template("risk.html", riskNumber = riskA.calculateRisk())


def loopFunc():
    not_done = True
    while not_done == True:
        responseDoor = get(url+"sensor.door", headers=headers)
        responseWindow = get(url+"sensor.switch", headers=headers)
        responseSmoke = get(url+"sensor.button", headers=headers)
        print(responseDoor.text.split()[17])
        if responseDoor.text.split()[17] == "\"open\"}":
            responses['doorCount']+=1
        if responseSmoke.text.split()[17] == "\"pressed\"}":
            responses['smokeCount']+=1
        if responseWindow.text.split()[17]=="\"on\"}":
            responses['windowCount']+=1
        if responses['timeCount'] >= 90:
            not_done = False
        responses['timeCount'] += 1
        riskA.set(**responses)
        print(responses['timeCount'])
        time.sleep(1)



x=Thread(target=loopFunc)
x.start()