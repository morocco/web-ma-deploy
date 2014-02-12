import json
from flask import Flask, request
from subprocess import call

app = Flask(__name__)

@app.route('/', methods=['POST'])
def deploy():
	data = json.loads(request.data)
	call(['deploy.sh', '/home/web-ma'])

if __name__ == '__main__':
	app.run(port=6868)
