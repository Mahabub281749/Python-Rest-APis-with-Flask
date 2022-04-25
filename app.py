from flask import Flask, jsonify
app = Flask(__name__) #Flask("Hi"); you can write this one also

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

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
                "phoneName" : "Iphone8"
                "phoneNumber" : 11111
            }
        ]
    }
    return jsonify(retJson)

#without defining port
if __name__=="__main__":
    app.run(debug=True)
