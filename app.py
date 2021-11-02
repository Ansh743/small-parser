from flask import Flask,render_template, jsonify, request, redirect,url_for
from LogParser import LogParser
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    fl = getFileList()
    return render_template("homepage.html", fileList = fl)

@app.route("/submit", methods=["POST"])
def submit():
    title = request.form.get("fName")
    parser.reset()
    parser.setFile('.\\logs\\'+title)
    parser.parse()
    time = parser.time
    fl = getFileList()
    return render_template("homepage.html", fileList = fl, result_time = time, selected_file = title)

def getFileList():
    fileList = list(os.listdir(".\\logs\\"))
    return fileList
    

if __name__ == '__main__':
    parser = LogParser()
    app.run(debug=True)