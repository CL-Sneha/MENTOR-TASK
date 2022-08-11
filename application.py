from flask import Flask, jsonify, request, render_template
import json
import requests

application = Flask(__name__)

@application.route('/')
def pincode():
    return render_template('Index.html')

@application.route('/create_file', methods=['POST'])
def create_file():
    if request.method == 'POST':
        pinc=json.loads(request.data)
        newurl="https://api.postalpincode.in/pincode/" + pinc["pin"]
        x = requests.get(newurl)
        return x.json()[0]
       
if __name__ == "__main__":
    application.run(debug=True)
