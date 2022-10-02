#In this file, we will use the flask web framework to handle the POST requests that we will get from the request.py and from HTML file

#import packages
import os
import numpy as np
import flask
from flask import Flask, request, jsonify,  render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('models/CropPricePrediction.pkl','rb'))

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():



    return flask.render_template('index.html')



# def save_path():
#     headers = ('name', 'price', 'quantity')
#     values = (
#         request.form.getlist('name[]'),
#         request.form.getlist('price[]'),
#         request.form.getlist('quantity[]'),         
#     )
#     items = [{} for i in range(len(values[0]))]
#     for x,i in enumerate(values):
#         for _x,_i in enumerate(i):
#             items[_x][headers[x]] = _i
#     return jsonify(items)
# get data from the html form and perform prediction
@app.route('/result',methods = ['POST'])
def result():
	if request.method == 'POST':
	    # string[]
		# arr=['state','district','market','commodity','variety']
		
		values = (
        request.form['state']
        request.form['district']
        request.form['market']
		request.form['commodity']  
		request.form['variety']         
    )
	
		input = str(values)

		# convert the data into numpy array and perform prediction
		prediction = model.predict([[np.array(input)]])
		output = prediction[0]

		# round output into two decimals
		output = str(output, 2)

		return render_template("result.html", prediction=output, years = data)


# get data from script file and perfrom prediction
@app.route('/api',methods=['POST'])
def predict():

	#get the data in json format
	data = request.get_json(force=True)

	#convert the data into numpy array and perform prediction
	prediction = model.predict([[np.array(data['exp'])]])
	output = prediction[0]

	#return result in json format
	return jsonify(output)


# set port into 5000 and debug is True
if __name__ == '__main__':
	app.run(port=5000, debug=True)
