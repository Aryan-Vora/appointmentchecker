import data
from flask import Flask, render_template, request
from datetime import date, datetime

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/',methods=["GET", "POST"])
def home():
    if request.method == "POST":
        info = data.getSchedule(request.form["state"])
        appointments =[]
        parsedInfo = ["","","",""]

        for i in range(len(info)):
            parsedInfo[0] = (info[i][5])[5:]
            parsedInfo[1] = date(day=int((info[i][1])[24:26]), month=int((info[i][1])[21:23]), year=int((info[i][1])[16:20])).strftime('%A, %B %dth, %Y')
            parsedInfo[2]= datetime.strptime((info[i][1])[28:], "%H:%M").strftime("%I:%M %p")
            if parsedInfo[2][0] == "0":
                parsedInfo[2] = parsedInfo[2][1:]
            parsedInfo[3]= (info[i][4])[9:]
            appointments.append(parsedInfo[3]+" minute appointment found at " + parsedInfo[0] + " on " + parsedInfo[1] + " at " +parsedInfo[2])
        return render_template("output.html", appointments=appointments, len = len(info), info=info)
    return render_template('home.html')
