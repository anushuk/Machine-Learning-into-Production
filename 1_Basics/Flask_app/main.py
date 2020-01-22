
from flask import Flask, render_template, jsonify, request
import os
import re
from prediction import predic

app=Flask(__name__)


CWD_PATH = os.getcwd() #getting current path


@app.route('/')
def index():
    return render_template('index.html')
#...func...
@app.route('/_hrabg', methods=['GET','POST'])
def hrabg():
    try:
        #getting values from html
        a=int(request.form['item1'])
        b=int(request.form['item2'])
        c=int(request.form['item3'])
        lis=[a,b,c]
        out=predic(lis)
        return jsonify(result=out) #returning the result back to html
    except Exception as e:
        return jsonify(result=str(e))


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
    #app.run(debug=False)
