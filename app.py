import sqlite3 as sql
from flask import render_template, Flask, request
app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/index1")
def index1():
    return render_template("index1.html")

@app.route("/question1", methods=['GET','POST'])
def question1():
    labels=[]
    values=[]
    r1=float(request.form.get('r1'))
    r2=float(request.form.get('r2'))
    con= sql.connect("earth.db")
    cur=con.cursor()
    cur.execute("select place,COUNT(mag) from earthquake where mag>? and  mag<? group by mag ",[r1,r2])
    data=cur.fetchall()
    for i in data:
        labels.append(i[0])
        values.append(i[1])
    return render_template("index1.html",labels=labels, values=values)


@app.route("/index2")
def index2():
    return render_template("index2.html")

@app.route("/question2", methods=['GET','POST'])
def question2():
    labels=[]
    values=[]
    r1=float(request.form.get('r1'))
    con= sql.connect("earth.db")
    cur=con.cursor()
    cur.execute("select mag, count(mag),substr(time,12,8) as time from earthquake where mag>? and time not between '06:00:00' and '18:00:00' group by mag",[r1])
    data=cur.fetchall()
    for i in data:
        labels.append(i[0])
        values.append(i[1])
    return render_template("index2.html",labels=labels, values=values)

@app.route("/index3")
def index3():
    return render_template("index3.html")

@app.route("/question3", methods=['GET','POST'])
def question3():
    labels=[]
    values=[]
    r1=request.form.get('r1')
    con= sql.connect("earth.db")
    cur=con.cursor()
    cur.execute("select count(*), mag, place from earthquake where place LIKE '%"+str(r1)+"' group by mag")
    data=cur.fetchall()
    for i in data:
        labels.append(i[2])
        values.append(i[0])
    return render_template("index3.html",labels=labels, values=values)

if __name__ == "__main__":
    app.run(debug=True)