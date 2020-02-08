from flask import Flask,request
from flask import json
import requests
import time
import sys

sys.path.insert(0, "/TensorFlowKeras")

from TensorFlowKeras import label_image

app = Flask(__name__)

def download(imgurl):
	import datetime
	imgfilename = datetime.datetime.today().strftime('%Y%m%d') + '_' + imgurl.split('/')[-1]
	with open("uploads/" + imgfilename, 'wb') as f:
		f.write(requests.get(imgurl).content)
	return imgfilename


@app.route("/", methods = ['GET'])
def predict():

	if(request.args.get('image_url') == None):
		return app.response_class(
		    response= json.dumps({'msg' : 'Please provide "image_url" query parameter i-e ?image_url=https://i.imgur.com/oDf68ZO.jpg'}),
		    status=500,
		    mimetype='application/json'
		)

	image_url = request.args.get('image_url')
	file_name = "uploads/" + download(image_url)

	result = dict()

	result['local e nome da imagen'] = file_name
	result['classificacao'] = label_image.classifier(file_name)

	response = app.response_class(
	    response=json.dumps(result, encoding='UTF-8',default=str),
	    status=200,
	    mimetype='application/json'
	)
	return response

app.run(debug=True, port=5000, host='0.0.0.0')