from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "main page"

@app.patch('/pat/<inputId>')
def patchmethod(inputId):
    data = request.get_json()
    users = data
    #print(inputId)
    print(f'The users data is {users}')
    if inputId in users.values():
        users["Id"] = 1000
        print(f"The data after updating is {users}")
        res = "Data updated"
        return res
    print(f"The data after creation is {users}")
    res = "Data created"
    return res

@app.delete("/del/<inputId>")
def deletemethod(inputId):
    data = request.get_json()
    users = data
    #print(inputId)
    print(f'The users data is {users}')
    if inputId in users.values():
        del users["Id"]
        print(f"The data after deleting is {users}")
        res = "Data deleted"
        return res
    res = "Data not found"
    return res

app.run(debug=True)