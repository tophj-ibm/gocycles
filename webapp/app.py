import os

from flask import Flask, render_template

app = Flask(__name__)
testString = "currently no one is playing the game :("

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/test/players', methods=['GET'])
def getplayers():
	return testString

@app.route('/test/players/<string:newplayer>', methods=['POST'])
def addPlayer():
	if (testString == 'currently no one is playing the game :('):
		testString = newplayer	
		return testString
	else:
		testString = testString+" " + newplayer
		return testString

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

