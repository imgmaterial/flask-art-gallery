from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
import sqlalchemy as sql
import uuid
from datetime import datetime

secret_key = "asdfadgangiwerubasdjvnaksd"
engine = sql.create_engine("sqlite:///image_info.db")

app = Flask(__name__)

IMG_FOLDER = os.path.join("static", "IMG")

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route("/images")
def show_all():
    IMG_LIST = os.listdir(app.config['UPLOAD_FOLDER'])
    IMG_LIST = [i for i in IMG_LIST]
    return(render_template("index.html", imagelist=IMG_LIST))

@app.route("/images/<img>")
def Display_img(img):
    IMG = os.path.join('IMG/' + img)
    print(IMG)
    return(render_template("image.html", user_image = IMG, show_tags = show_tags, img = img))


@app.route("/upload", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = '{}{:-%Y%m%d%H%M%S}.png'.format(str(uuid.uuid4().hex), datetime.now())
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('Display_img', img=filename))
    return(render_template("upload.html"))

def show_tags(img_name):
    with engine.connect() as conn:
        result = conn.execute(sql.text("SELECT tag_name FROM object_tag_mapping JOIN INFO ON object_reference = INFO.id JOIN TAGS ON tag_reference = TAGS.id WHERE image_name = :img"), { "img" : img_name})
        output = [row.tag_name for row in result]
        
    return(output)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__=='__main__':
    app.run(debug=True)
