from myapp import flaskObj
from flask import render_template

@flaskObj.route("/")
def main():
    return render_template("homepage.html")
