from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from datetime import date

app = Flask(__name__)
app.secret_key = "super duper secret key"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "bossing2"

mysql = MySQL(app)

@app.route("/", methods=["POST", "GET"])
def userlog():
    if request.method == "POST":
        usn = request.form["usn"]
        password = request.form["pass"]

        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM tbl_user WHERE usn='{usn}'")
        record = cur.fetchone()
        cur.close()

        if record and password == record[2]:
            session['usn'] = record[1]
            session['firstname'] = record[3]
            session['middlename'] = record[4]
            session['lastname'] = record[5]
            session['gender'] = record[6]
            session['couryear'] = record[7]
            session['address'] = record[8]
            session['prelim'] = record[9]
            session['midterm'] = record[10]
            session['prefinal'] = record[11]
            session['final'] = record[12]

            return redirect(url_for('userdash'))
        
        else:
            return render_template("userlogin.html", error="INVALID USN OR PASSWORD")


    return render_template("userlogin.html")


@app.route("/userdash")
def userdash():
    if all(key in session for key in ["usn", "firstname", "middlename", "lastname", "gender", "couryear", "address", "prelim", "midterm", "prefinal", "final"]):

        return render_template("studentdash.html", usn=session["usn"], firstname=session["firstname"], middlename=session["middlename"], lastname=session["lastname"], gender=session["gender"], couryear=session["couryear"], address=session["address"], prelim=session["prelim"], midterm=session["midterm"], prefinal=session["prefinal"], final=session["final"])
    else:
        return render_template("studentdash.html", error="You are not logged in")


@app.route("/payhistory/<string:usn>")
def payhistory(usn):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM phistory WHERE usn='{usn}'")
    data = cur.fetchall()
    cur.close()

    return render_template("payhistory.html", data=data)

@app.route("/studentbalance/<string:usn>")
def balance(usn):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM tbl_user WHERE usn='{usn}'")
    dataa = cur.fetchall()
    cur.close()

    return render_template("studentbalance.html", ball=dataa)

@app.route("/logout")
def logout():
    session.pop('usn', None)

    return redirect(url_for("userlog"))



@app.route("/admindash")
def main():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_user")
    data = cur.fetchall()
    cur.close()

    return render_template("userdash.html", data=data)

@app.route("/userinfo/<string:id>", methods=["POST", "GET"])
def info(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_user WHERE user_id=%s", (id,))
    info = cur.fetchone()
    cur.close()

    usn = info[1]
    firstname = info[3]
    middlename = info[4]
    lastname = info[5]

    prel = int(info[9])
    midt = int(info[10])
    pref = int(info[11])
    final = int(info[12])

    current_date = date.today()

    total = prel + midt + pref + final

    if request.method == "POST":
        payment = int(request.form["pay"])
        pay = payment

        while payment > 0:
            if prel != 0:
                prelim = min(prel,payment)
                prel -= prelim
                payment -= prelim
            elif midt !=0:
                midterm = min(midt,payment)
                midt -= midterm
                payment -= midterm
            elif pref != 0:
                prefinal = min(pref,payment)
                pref -= prefinal
                payment -= prefinal
            elif final != 0:
                fin = min(final,payment)
                final -= fin
                payment -= fin
            else:
                print("Error")
                break

        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbl_user SET prelim=%s, midterm=%s, prefinal=%s, final=%s WHERE user_id=%s", (prel, midt, pref, final, id))
        mysql.connection.commit()
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO phistory(firstname, middlename, lastname, amount, date, usn) VALUES (%s, %s, %s, %s, %s, %s)", (firstname, middlename, lastname, pay, current_date, usn))
        mysql.connection.commit()
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM phistory WHERE payment_id=LAST_INSERT_ID()")
        resibo = cur.fetchone()
        cur.close()

        return render_template("receipt.html", resibo=resibo)

    return render_template("userinfo.html", stud=info, total=total)

@app.route("/adminlogin", methods=["POST", "GET"])
def adlogin():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["pass"]

        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM tbl_admin WHERE username='{user}'")
        records = cur.fetchone()
        cur.close()

        if records and password == records[2]:
            session['username'] = records[1]
            session['name'] = records[3]

            return redirect(url_for('userdashad'))
        
        else:
            return render_template("adminlog.html", error="INVALID USERNAME OR PASSWORD")


    return render_template("adminlog.html")

@app.route("/admindashlog")
def userdashad():
    if all(keys in session for keys in ["username", "name"]):

        return render_template("admindash.html", username=session["username"], name=session["name"])
    else:
        return render_template("admindash.html", error="You are not logged in")


@app.route("/adminlogout")
def adminlogout():
    session.pop('username', None)

    return redirect(url_for("adlogin"))

@app.route("/adminpayhistory")
def adphistory():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM phistory")
    history = cur.fetchall()
    cur.close()

    return render_template("adminpayhistory.html", hist=history)

if __name__ == "__main__":
    app.run(debug=True)
