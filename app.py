from flask import Flask
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
    return "bye"

#without defining port
if __name__=="__main__":
    app.run(debug=True)
