#from urllib import request
from requests import request
from flask import Flask, render_template, request, redirect
import os
import dbconn as db

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

@app.route('/bloglist') # default methods=['GET']
def bloglist():
    conn = db.dbconn()
    cursor = conn.cursor()
    sql = '''select * from blog''' # 실행할 쿼리문
    cursor.execute(sql) # 실행
    rows = cursor.fetchall() # 전부다 불러옴 fetchall, 하나만 fetchone -> 불러와서 rows에 저장
    print(rows)
    return render_template('bloglist.html',data = rows) 

@app.route('/blogform', methods=['GET','POST'])
def blogform():
    if request.method == 'GET':
        return render_template('blogform.html')
    else:
        # 글을 DB에 저장
        return redirect('/bloglist') # 저장하고 목록으로 돌아가기위해 redirect
if __name__ =='__main__':
    app.run(debug=True,port=80)
