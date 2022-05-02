# Hanzhen Yang 1070951, 
# Hanzhong Wang, 1029740,
# Quan Zhou 1065302, 
# Yuhang Xie 1089250, 
# Ze Liu 1073628

# from msilib.schema import Directory
from flask import Flask, json, url_for, redirect, render_template, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)

directory = '../aurin'
# directory = "/home/ubuntu/data"
# directory = "aurin"

@app.route("/map/vic", methods=["GET"])
def map_vic():
    filename = "vic_plus.json"
    try:
        with open(directory + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "message": "{}".format(e)})


@app.route("/map/nsw", methods=["GET"])
def map_nsw():
    filename = "nsw_plus.json"
    try:
        with open(directory + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "message": "{}".format(e)})


@app.route("/analysis/vic", methods=["GET"])
def analysis_vic():
    filename = "vic_analysis.json"
    try:
        with open(directory + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "message": "{}".format(e)})

@app.route("/analysis/nsw", methods=["GET"])
def analysis_nsw():
    filename = "nsw_analysis.json"
    try:
        with open(directory + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "message": "{}".format(e)})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)  
    app.run()      
