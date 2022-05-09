# Thanks COMP 90024 TEAM 68 Provide template Reference : https://github.com/CCC68/COMP90024_Project2, Hanzhen Yang 1070951, Hanzhong Wang, 1029740, Quan Zhou 1065302, Yuhang Xie 1089250, Ze Liu 1073628
# Modoified By COMP90024 TEAM 45
# Yingpei Ni 1252881
# Yixue Jiang 1023137
# Zirui Shan  1298781
# Jinglin Li 1000797
# Yuxiang Xie 1060196

from flask import Flask, json, url_for, redirect, render_template, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)

temp_dire = '../temp_data'

@app.route("/analysis/data", methods=["GET"])
def read_analysis_crime():
    filename = "analysis_data.json"
    try:
        with open(temp_dire + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "  message": "{}".format(e)})

@app.route("/analysis/suburb", methods=["GET"])
def read_analysis_suburb():
    filename = "analysis_suburb.json"
    try:
        with open(temp_dire + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "  message": "{}".format(e)})

@app.route("/map/Adelaide", methods=["GET"])
def read_map_Adelaide():
    filename = "Adelaide.json"
    try:
        with open(temp_dire + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "  message": "{}".format(e)})

@app.route("/map/Sydney", methods=["GET"])
def read_map_Sydney():
    filename = "Sydney.json"
    try:
        with open(temp_dire + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "  message": "{}".format(e)})

@app.route("/map/Melbourne", methods=["GET"])
def read_map_Melbourne():
    filename = "Melbourne.json"
    try:
        with open(temp_dire + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "  message": "{}".format(e)})

@app.route("/map/Brisbane", methods=["GET"])
def read_map_Brisbane():
    filename = "Brisbane.json"
    try:
        with open(temp_dire + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "  message": "{}".format(e)})

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)  
    app.run()      
