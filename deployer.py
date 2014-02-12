import os
import sys
import json
from flask import Flask, request
from subprocess import call

app = Flask(__name__)
DEPLOY_SCRIPT = os.path.dirname(os.path.abspath(__file__)) + '/deploy.sh'

@app.route('/', methods=['GET', 'POST'])
def deploy():
	if request.method == 'GET':
		return 'Deployment server is up.'

	call([DEPLOY_SCRIPT, '/home/web-ma'])

if __name__ == '__main__':
 	app.run(port=6868, debug=True)
