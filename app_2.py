from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import json


app_2 = Flask(__name__) 
api = Api(app_2)

def CheckPostedData(postedData, functionName):
    if (functionName == "add" or functionName == "subtract" or functionName == "multiply"  ):
        if "x" not in postedData or "y" not in postedData:
            return 301 #Missing parameter
        else:
            return 200
    elif (functionName == "division"):
        if "x" not in postedData or "y" not in postedData:
            return 301 #Missing parameter
        elif int(postedData["y"])==0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        # If I am here, the the resource Add was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify Validity of posted data
        status_code = CheckPostedData(postedData, "add")
        if (status_code !=200):
            retJson ={
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        #if i am here then status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Add the posted data
        ret = x+y
        retMap ={
            "Message" : ret,
            "Status Code" : 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        # If I am here, the the resource Subtract was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify Validity of posted data
        status_code = CheckPostedData(postedData, "subtract")
        if (status_code !=200):
            retJson ={
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        #if i am here then status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Subtract the posted data
        ret = x-y
        retMap ={
            "Message" : ret,
            "Status Code" : 200
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        # If I am here, the the resource Multiply was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify Validity of posted data
        status_code = CheckPostedData(postedData, "multiply")
        if (status_code !=200):
            retJson ={
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        #if i am here then status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Multply the posted data
        ret = x*y
        retMap ={
            "Message" : ret,
            "Status Code" : 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        # If I am here, the the resource Divide was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify Validity of posted data
        status_code = CheckPostedData(postedData, "division")
        if (status_code !=200):
            retJson ={
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        #if i am here then status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Divide the posted data
        ret = (x*1.0)/y
        retMap ={
            "Message" : ret,
            "Status Code" : 200
        }
        return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

@app_2.route('/')
def hello_world():
    return "Hello World!"


#without defining port
if __name__=="__main__":
    app_2.run(debug=True)