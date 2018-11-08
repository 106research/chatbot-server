# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:18:16 2016
@author: winpython
"""

import os
from flask import Flask, request, send_file, send_from_directory, session
from werkzeug import secure_filename
# belows include self-define libs and func

from wav_to_STT import input_filename
from jiebaCut import func_cut
from chatbot_response import Chat_with_Bot
# aboves include self-define libs and func
import numpy as np
import json
from chatbot import chatbot

project= chatbot.Chatbot()
project.main(['--modelTag', '1108', '--test', 'daemon'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['wave', 'wav'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route("/", methods=['get', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',filename = filename))
            #wav2sep(filename)
            # below finished word translate and cutting

            asking = func_cut(input_filename(filename))
            responsing = Chat_with_Bot(asking, project)
            print(responsing)

            # above print the predition of response without tag
            ans = (filename)
            # below decode json from nvidia digits output





            # print(ans.decode('utf8').replace("\n"," "))

            # return ans.decode('utf8')
            return (responsing)
    return '''
    <doctype html>
    <title>test upload</title>
    <h1>Upload NoTag</h1>
    <form action="" method="post" enctype=multipart/form-data>
        <p><input type=file name=file>
           <input type=submit name=upload></p>
    </form>
    '''


@app.route("/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)