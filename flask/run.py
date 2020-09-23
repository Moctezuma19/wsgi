from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	ide = request.args.get('id')
	return str(ide)

if __name__ == '__main__':
	app.run()