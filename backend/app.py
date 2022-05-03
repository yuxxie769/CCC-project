# from msilib.schema import Directory
from flask import Flask, json, url_for, redirect, render_template, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)

temp_dire = '../temp_data'

@app.route("/analysis/data", methods=["GET"])
def read_analysis_crime():
    filename = "final_V_2.json"
    try:
        with open(temp_dire + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "  message": "{}".format(e)})

@app.route("/analysis/suburb", methods=["GET"])
def read_analysis_suburb():
    filename = "suburb.json"
    try:
        with open(temp_dire + '/' + filename) as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "Error", "  message": "{}".format(e)})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)  
    app.run()      
