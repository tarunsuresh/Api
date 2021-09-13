from flask import Flask,jsonify,request


task=[
    {
        "id":1,
        "title":"gros",
        "description":"mill,milk,ghee",
        "done":False
    }
]

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome"

@app.route("/getData")
def getData():
    return jsonify({
        "data" : task,

    }) 

@app.route("/addData",methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the correct data"
        },400)

    add_task={
        "id":task[-1]["id"]+1,
        "title": request.json["title"],
        "description":request.json.get("description",""),
        "done":False

    }    
    task.append(add_task)
    return jsonify({
            "status":"sussces",
            "message":"task added sussecfuly"
        })


if(__name__=="__main__"):
    app.run(debug=True)
