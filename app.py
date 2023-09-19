from flask import Flask, request, jsonify

app=Flask(__name__)
num=[1,2,3,4,5]

@app.route('/')
def hello_world():
     return "Hello World!"

@app.route("/evenodd<int:num>")
def evenodd(num):
    Status=None
    if num%2==0:
        Status= "Even"
    else:
        Status="Odd"
    return jsonify ({'status':Status})

@app.route("/addnum", methods=['POST'])
def addnum():
    request_data= request.get_json()
    print(request_data['num'])
    num.append(request_data['num'])

@app.route("/showlist")
def show():
    return jsonify ({'list':num})


if __name__=="__main__":
    app.run(debug=True)
