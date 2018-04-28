import json
import requests
from flask import Flask
from flask import request, render_template, jsonify, make_response

app = Flask(__name__)

'''

Load Data

'''


data_url = 'https://raw.githubusercontent.com/hvo/datasets/master/nyc_restaurants_by_cuisine.json'

def load_data():
	'''load data from url'''
	return json.loads(requests.get(data_url).content)


def load_zipcode(zipcode):
	'''get the cuisine counts for the requested zipcode'''
	return sorted([
		dict(
			cuisine=d['cuisine'],
			total=d['perZip'].get(zipcode)
		)
		for d in data
	], key=lambda d: d['total'], reverse=True)



data = load_data()

all_zipcodes = list(set([
	zcode for d in data
	for zcode in list(d['perZip'].keys())
]))




'''

App Routes

'''

@app.route('/')
def index():
	'''Renders the page'''
	return render_template('index.html', all_zipcodes=all_zipcodes)


@app.route('/restaurants')
@app.route('/restaurants/<zipcode>')
def get_zipcode_data(zipcode=None):
	'''Returns a json array of cuisine and counts for the specified zipcode'''
	zip_data = load_zipcode(zipcode)
	return jsonify(zip_data)


@app.route('/chart')
@app.route('/chart/<zipcode>')
def get_zipcode_chart(zipcode=None):
	'''Render the altair chart'''
	return render_template('altair/bar_chart.json', zipcode=zipcode)


if __name__ == '__main__':
	app.run(debug=True, port=5001)
