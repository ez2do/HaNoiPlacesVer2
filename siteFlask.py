import os
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Place, Base
from werkzeug.utils import secure_filename	#use for uploading file

UPLOAD_FOLDER = '/home/tuananh/WebDev/HanoiPlaces-project/static/img'
ALLOWED_EXTENSIONS = set(['tif', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#read the data base
engine = create_engine('sqlite:///places.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

#process filename of image uploaded
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#homepage
@app.route('/', methods = ['GET', 'POST'])
def HomePage():
	#when uploading a place
	if request.method == 'POST':
		#upload name, description, type of place
		place_name = request.form['name']
		place_description = request.form['description']
		place_type = request.form['type'].lower()

		#upload image
		#check if the POST request has the file part
		# if 'file' not in request.files:
		# 	flash('No file part')
		# 	return redirect(url_for('HomePage'))
		# file = request.files['file']

		# #if user does not select file, browser also submit a empty
		# #part without filename
		# if file.filename == '':
		# 	flash('No selected file')
		# 	return redirect(url_for('HomePage'))

		#if file exist and has an image type
		file = request.files['image']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		
		place_img_path = 'img/' + filename
		new_place = Place(name = place_name, description = place_description, 
			type = place_type, rate_times = 0, total_point = 0, rating = 0, img_path = place_img_path)

		session.add(new_place)
		session.commit()

		return redirect(url_for('HomePage'))

	else:
		places = session.query(Place).all()
		return render_template('HanoiPlace.html', places = places)

@app.route('/update', methods = ['POST'])
def update():
	place = session.query(Place).filter_by(id = request.form['id']).first()
	place.rate_times += 1
	place.total_point += int(request.form['point'])
	place.rating = place.total_point / place.rate_times

	session.add(place)
	session.commit()

	return jsonify({'result' : 'success', 'rating' : place.rating})


if __name__ == '__main__':
	app.debug = True
	app.run(host = '', port = 1111)