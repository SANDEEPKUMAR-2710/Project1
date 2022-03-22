from  flask import Flask,jsonify,request;
from sql import *;
app = Flask(__name__)

@app.get('/')
def hello():
    all_data = getAll()
    return(jsonify(all_data));    
        
@app.post('/hey')
def add():
    data = request.get_json()
    insert(data)
    return("Data added")

if __name__ == '__main__':
    app.run(debug = True)