#!/usr/bin/python3
import requests
import json
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

html= """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>Astronomy Picture of the Day</h1>
<form action = "/getpicture" method = "GET">
        <p><input type = "submit" value = "Get A Picture"></p>
    </form>


</body>
</html>"""


html3= """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>Couldn't retrieve data</h1>



</body>
</html>"""


@app.route("/")
def start():
    return html

@app.route("/failure")
def error():
    return html3


@app.route("/getpicture", methods = ["GET"])
def login():
    NASAAPI = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    # make a call to NASAAPI
    apodresp = requests.get(NASAAPI)

    # strip off json
    apod = apodresp.json()

    if apod:
        #data= json.loads(apod)
        daily_pic = apod["url"]
        date = apod["date"]
        explanation = apod["explanation"]
        #return html2
        return render_template('html2.html', daily_pic = daily_pic, date = date, explanation=explanation)
    else:
            return redirect("/failure")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
