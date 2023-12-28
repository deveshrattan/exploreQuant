from flask import Flask, session
from upstocksAPIDetails import getAccessToken, testGetpositions
from instance import config  

app = Flask(__name__)
app.config.from_object(config.CustomConfig)
app.secret_key = app.config['SESSION_SECRET_KEY']

@app.route('/')
def hello():
    return 'Hello, Quant!'
    
@app.route('/getAccessToken')
def getAccessTokenWrapper():
    print(config.CustomConfig)
    print("---------")
    print(app.config)
    token = getAccessToken(app.config['API_KEY'], app.config['API_SECRET'], app.config['REDIRECT_URI'])
    print(token)
    session['access_token'] = token
    return 'new page'

@app.route('/testApicall')
def testCall():
    testGetpositions()
    return "test"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8091, debug=True)