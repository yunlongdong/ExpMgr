from flask import Flask
from flask import render_template
from flask import url_for, request
import numpy as np
import json
import glob
import sys
import os
import argparse
from .constants import results_dir
from time import time
parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=5000, help='port, default 5000.')
parser.add_argument('--logdir', type=str, required=True, help='the directory save the json files.')

args = parser.parse_args()

dir_name = os.path.join(args.logdir, results_dir)

def search_exp():
    exp_list = glob.glob(os.path.join(dir_name, '*.json'))   
    exp_list_basename = [os.path.basename(exp) for exp in exp_list[::-1]]
    return exp_list_basename
    
def load_json(fn):
    fn = os.path.join(dir_name, fn)
    info = json.load(open(fn, 'r'))
    return info
    
app = Flask(__name__)

@app.route('/')
def main_page():
    start = time()
    exp_list = search_exp()
    print('search time:', time()-start)
    
    start = time()
    url_for('static', filename='images/')
    url_for('static', filename='libs/')
    url_for('static', filename='vendor/')
    print('url_for time:', time()-start)
    
    start = time()
    content =  render_template('index.html', exp_list=exp_list)
    print('template time', time()-start)
    return content

@app.route('/get_json', methods=["GET"])
def get_json():
    name = request.args.get("name")
    return json.dumps(load_json(name))
    
if __name__ == "__main__":
    app.run(port=args.port, debug=False, threaded=True)