#from flask_ngrok import run_with_ngrok   # colab 
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)               
    return 'OK'

if __name__ == "__main__":
    #run_with_ngrok(app)        # colab 
    app.run()
