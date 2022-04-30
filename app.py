from flask import Flask, jsonify, request
import json
app = Flask(__name__) #Flask("Hi"); you can write this one also

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    #Get x,y from the posted data
    dataDict = request.get_json()

    if "y" not in dataDict:
        return "ERROR", 305

    x = dataDict["x"]
    y = dataDict["y"]

    #Add z=x+y
    z=x+y

    #Prepare a Josn, "z":z
    retJSON = {
        "z":z
    }

    return jsonify(retJSON), 200
@app.route('/bye')
def bye():
    #prepare a response for the request that came to /bye
    c= 2*534
    s =str(c)
    retJson = { 
                    'Name' : 'Mahabub',
                    'Age' : 22,
                    "phones" : [
                        {
                            "phoneName" : "Iphone8",
                            "phoneNumber" : 11111
                        }
                    ]
                  
    }
    return json.dumps(retJson)

#without defining port
if __name__=="__main__":
    app.run(debug=True)
