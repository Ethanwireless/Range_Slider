from flask import Flask, redirect, url_for, request, render_template
from db import*

db_file = "./database.db"
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index',methods = ['POST', 'GET'])
def page():
	if request.method == 'POST':
		data_values = str(request.form['json_str'])
		print ('Debug msg: POST request from index')
		co = data_values.find(',')
		cur_min = int(data_values[1:co])
		cur_max = int(data_values[co+1:-1])
		print ('Debug msg: MIN: [{0}], MAX: [{1}] @ server'
			.format(cur_min, cur_max))
		update_value(db_file, 0, cur_min)
		update_value(db_file, 1, cur_max)

	else:
		pass

	return render_template('index.html')

if __name__ == '__main__':
	init_db(db_file)
	# toggle debug mode
	app.run(host='0.0.0.0', port = 5000, debug = True)
