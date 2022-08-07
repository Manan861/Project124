from flask import Flask, jsonify, request
app=Flask(__name__)

tasks=[
    {
        'contact':'9987644456',
        'name': 'Raju',
        'done': False,
        'id': 1
    },
    {
        'contact':'9987644456',
        'name': 'Rahul',
        'done': False,
        'id': 2
    }
]

@app.route("/add-data",methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
    

        },400)
    contact = { 
        'id': List[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False

    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    

    })

@app.route("/getdata")
def gettask():
    return jsonify({
        "data": tasks

    })

if (__name__=="__main__"):
    app.run(debug=True)

    
    

