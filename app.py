from flask import Flask

app = Flask(__name__)

@app.route("/name")
def myname():
    return "My Name Is Himanshu Singh...."

@app.route("/education")
def myeducation():
    return "Currently doing Internship from LW in Devops.."

@app.route("/about")
def about():
    return "I am Currently looking for the job in Devops as Freshers"


app.run(host='0.0.0.0', port=5000)

