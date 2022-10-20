#from urllib import request
from requests import request
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/test/<username>')
def test(username):
    print(username)
    return render_template('test_result.html',name=username)

@app.route('/methodin')
def methodin():
    return render_template('inputform.html')


@app.route('/methodout',methods=['GET','POST'])
def methodout():
    if request.method == 'POST':
        print('POST')
        data = request.form
    else :
        print('GET')
        data = request.args
    return render_template('method.html',data1=data,data2=request.method)

@app.route('/fileupload',methods=['GET','POST'])
def fileupload():
    if request.method == 'GET':
        return render_template('fileinput.html')
    else:
        f = request.files['formFile']
        path = os.path.dirname(__file__) + '/upload/'+f.filename
        print(path)
        f.save(path)
        print('저장성공 :)')
        return redirect('/')
    
if __name__ =='__main__':
    app.run(debug=True,port=80)
