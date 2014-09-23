# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, g, session
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy import desc
from apps import app, mydb
from apps.forms import ArticleForm, CommentForm, JoinForm, LoginForm
from apps.models import (
    User,
    Article,
    Process,
    Inspire,
    Comment
)





from google.appengine.ext import db

class Photo(db.Model):
	photo_inClass = db.BlobProperty()
	text_inClass = db.StringProperty()


def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

	return '.' in filename and \
	filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route('/')
@app.route('/index')
def index():
	return render_template("/main/first.html")   """, all_list=Photo.all())



@app.route('/create', methods=['POST'])
def upload_db():
	post_data = request.files['photo']
	filestream = post_data.read()
#	post_text = request.form['text']

	upload_data = Photo()
	upload_data.photo_inClass = db.Blob(filestream)
#	upload_data.text_inClass = post_text
	upload_data.put()

	url = url_for("shows", key=upload_data.key())
	return redirect(url_for('index'), url = url)
	return render_template('/timeline/home.html')



@app.route('/show/<key>')
def shows(key):
	uploaded_data = db.get(key)
	return app.response_class(uploaded_data.photo_inClass)
	"""