from flask import Flask,jsonify,request
app=Flask(__name__)
Data=[
    {
        "id":1,
        "Contact":"9423567845",
        "name":"Vinal Chhajed",
        "done":False

    },
    {
        "id":2,
        "Contact":"8484099207",
        "name":"Aryan Chhajed",
        "done":False

    },
    {
        "id":3,
        "Contact":"8484809203",
        "name":"Charmi Chhajed",
        "done":False

    },
]

@app.route("/add_Data",methods=["POST"])
def addData():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "message":"Please provide the data!!"
        },404)
    data={
        "id":Data[-1]["id"]+1,
        "Contact":request.json["Contact"],
        "name":request.json.get("name",""),
        "done":False
    }
    Data.append(data)
    return jsonify({
        "Status":"Success",
        "message":"Data added successfully"
    },23)
@app.route("/get_Data")
def getData():
    return jsonify({
        "data":Data
    })

if(__name__=="__main__"):
    app.run()