import os, sys, inspect
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app_path = inspect.getfile(inspect.currentframe())
sub_dir = os.path.realpath(os.path.dirname(app_path))
main_dir = os.path.dirname(sub_dir)

sys.path.insert(0, sub_dir)

import pickle, json
import numpy as np
from api_response import api_response
from flask import Flask, request, jsonify
from warnings import filterwarnings, simplefilter
filterwarnings("ignore")
simplefilter(action='ignore', category=FutureWarning)
import traceback


app = Flask(__name__)

mdl = pickle.load(open(os.path.join(main_dir, 'model/mdl.pickle'),'rb'))


@app.route("/creditscore", methods=['GET', 'POST'])
def index():
    output = []

    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            print(data)
            output = mdl.predict(data)
            true_response = api_response(output)
            return jsonify(true_response.true_output())

        except Exception as error:
            false_response = api_response(output)
            return jsonify(false_response.error_output())
    else:
        false_response = api_response(output)
        return jsonify(false_response.error_req())


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
