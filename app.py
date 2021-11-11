from flask import Flask,render_template, request
from LogParser import LogParser
import os

sep = os.path.sep
UPLOAD_FOLDER = '.'+sep+'uploaded_files'
ALLOWED_EXTENSIONS = set(['txt', 'log'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def hello_world():
    fl = getFileList()
    return render_template("homepage.html", fileList = fl, selected = False)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=["POST"])
def submit():
    parser = LogParser()
    title = request.form.get("fName")
    parser.reset()
    fl = getFileList()

    if title != "None":    
        parser.setFile(os.getcwd()+sep+'logs'+sep+title)
        parser.parse()
        time = parser.time
        return render_template("homepage.html", fileList = fl, result_time = time, selected_file = title, selected = True)

    file = request.files['uploadedFile']
    if file.filename != '':
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        parser.setFile('.'+sep+'uploaded_files'+sep+file.filename)
        parser.parse()
        time = parser.time
        return render_template("homepage.html", fileList = fl, result_time = time, selected_file = file.filename, selected = True)
    del parser
    return render_template("error.html")

def getFileList():
    fileList = list((os.listdir(os.getcwd()+sep+'logs'+sep)))
    return fileList
    

if __name__ == '__main__':
    app.run(debug=True)