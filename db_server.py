#!flask/bin/python
# Before your interview, write a program that runs a server that is accessible on http://localhost:4000/.
# When your server receives a request on http://localhost:4000/set?somekey=somevalue
# it should store the passed key and value in memory.
# When it receives a request on http://localhost:4000/get?key=somekey it should return the value stored at somekey.
# During your interview, you will pair on saving the data to a file.
# You can start with simply appending each write to the file, and work on making it more efficient if you have time.
from flask import Flask
from flask import request

app = Flask(__name__)
params = {}

@app.route('/')
def index():
    # TODO: something here
    return('Oh, hi. Nothing to see here. Please, move along.')

@app.route('/set', methods=['GET'])
def setting_values():
    """ This is where we set the input values as keys and values then store them in memory - seems like in a dict"""
    this_thing = request.args
    e_k = request.args.keys()
    for k in e_k:
      params[k] = request.args.get(k)
    print(str(params))
    return (str(params))

@app.route('/get')
def print_value():
    val = request.args.get('key')
    print (params[val])
    return(params[val])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)