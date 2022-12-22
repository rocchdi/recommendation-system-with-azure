#app.py
#pip install flask
#set FLASK_APP=app
#flask run


import requests
from flask import Flask, render_template, request
import pandas as pd
import re



global url

# Azure Function endpoint
#url_azure = "https://azure-func-rec6.azurewebsites.net/api/azure-func6"
url_azure = "https://azure-func-11.azurewebsites.net/api/azure-func11"
 
 
 


app = Flask(__name__)

 

 

df = pd.read_csv('articles_users.csv')
user_ids = df['user_id']


@app.route('/', methods=['GET'])
def home():

	return render_template('index.html', user_ids=user_ids)

	#return render_template('index.html', image_names=image_names)
	 






@app.route('/', methods = ['POST'])
def predict():
	
	#select user_ids 
    	#user_ids = [0,1, ..]

	user_id = request.form.get('select')
	
	print(user_id)
	 

	user = '%s' %(user_id) 

	headers = {'accept': 'application/json'}
	 
	# Appel zure Function submit user_id 


	var2 = "?userId="+str(user_id)
	 
	url = "".join([url_azure, var2])


	response = requests.post(url, headers=headers)
	 

 
	#print(response.status_code)
	#print(response.headers)

	

	if response.status_code == 200:
		recommended = response.content
		#recommended = re.findall(r'\".*?\"', str(recommended))
		#res = [int(s) for s in str(recommended).split() if s.isdigit()]

		temp = re.findall(r'\d+',  str(recommended))
		recommended = list(map(int, temp))
		#recommended = str(res)
		 
		print(recommended)
    			 
 
	return render_template('recommendation.html', recommendation=user, recommended=recommended, user_ids=user_ids)

	 



if __name__ == '__main__':
	app.run(port=3000,debug=True)

