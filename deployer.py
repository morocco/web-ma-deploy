import os
import json
from flask import Flask, request
from subprocess import call

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEPLOY_SCRIPT = os.path.join(BASE_DIR, 'deploy.sh')

@app.route('/', methods=['GET', 'POST'])
def deploy():
	if request.method == 'GET':
		return 'Deployment server is up.'

	data = json.loads(request.data)
	call([DEPLOY_SCRIPT, '/home/web-ma'])

if __name__ == '__main__':
	app.run(port=6868)
