from importlib.resources import contents
from flask import Flask, render_template, request, redirect
import sys


app = Flask(__name__)


nextId = 4
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href ="/update/{id}/">update</a></li>
        '''
    return f'''<doctype html>
    <html>
        <body>
            <div style="text-align:center ">
                <h1><a href ="/" style='color:green'>PIKA</a></h1>     
                <h1>Login</h1>
           
            <form action="/create/" method ="POST">
                <div style="text-align:center">
                    <p><input type = "text" name = "title" placeholder = "Id" size= 15></p>
                    <p><input type ="password" placeholder = "Password" size = 15></textarea></p>    
                    <p><input type ="submit" value="LOGIN" > </p>
                </div>
            </form>
            {content}
        </body>
    </html>
                '''

'''///'''
@app.route("/updatemember/")
def Loginsite():
    return f'''<doctype html>
    <html>
        <body>
        needs Update
        </body>
    
    </html>

    '''


def getcontents():
    liTags =''
    for topic in topics :
        liTags = liTags + f'<li><a href ="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags


@app.route("/")
def index():
    return template(getcontents(), '<div style = "text-align:center"><h2>welcome</h2>this site PIKA ROBOTICS</div>')



@app.route("/create/", methods=['get','post'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method ="POST">
                
                <p><input type = "text" name = "title" placeholder = "Id" size= 15></p>
                <p><input type ="password" placeholder = "Password" size = 10></textarea></p>    
                <p><input type ="submit" value="create"> </p>
            </form>
        '''
        return template(getcontents(), content)
    else:
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic= {'id':nextId ,'title':title, 'body':body}
        topics.append(newTopic)
        url ='/read/'+str(nextId)+'/'
        nextId = nextId+1 
        return redirect(url)

@app.route("/read/<int:id>/")
def read(id):
    title = ''
    body = ''
    for topic in topics :
        if id == topic['id']:
             title = topic['title']
             body = topic['body'] 
             break  
    return template(getcontents(), f'<h2>{title}</h2>{body}',id)
                
@app.route("/update/<int:id>/", methods=['get','post'])
def update(id):
    if request.method == 'GET':
        content = '''
        
            <form action="/create/" method ="POST">
                
                <p><input type = "Id" name = "title" placeholder = "Id" size = 15></p>
                <p><input type ="password" placeholder = "Password" size=10 ></textarea></p>    
                <p><input type ="submit" value="create"> </p> 
            </form>
        '''
        return template(getcontents(), content)
    else:
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic= {'id':nextId ,'title':title, 'body':body}
        topics.append(newTopic)
        url ='/read/'+str(nextId)+'/'
        nextId = nextId+1 
        return redirect(url)
    
@app.route("/test/")
def test():
    return f'''<doctype html>
        <html lang="ko">
            <head>
            
            <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
            
            <meta charset="utf-8">
                <title>select device</title>
            </head>
            <body>
                    <div style="text-align:center; line-height: 70px;">
                    <h3>select device</h3>
                    
                    <form>
                        <select name="SelectRobot">
                            <option value="">Robot Select</option>
                            <option valte="Robot1">Robot1(unable)</option>
                            <option valte="Robot2">Robot2</option>
                            <option valte="Robot3">Robot3</option>
                        </select>
                        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                        <select name="SelectWearable">
                            <option value="">Wearable Select</option>
                            <option valte="Wearable1">Wearable1</option>
                            <option valte="Wearable2">Wearable2</option>
                            <option valte="Wearable3">Wearable3</option>
                        </select>
                    </form> 
                    </div>
                    
                    <form>
                        <label for="cb1"></label>
                        <div style="text-align:center; line-height: 300px;">
                            <p><input type ="submit" value="select"> </p> 
                        </div>
                    </form>
            </body>
        </html>
                '''
                
@app.route("/test2/")
def test2():
    return f'''<doctype html>
        <html lang="ko">
            <head>
            
            <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
            
            <meta charset="utf-8">
                <title>select device</title>
            </head>
            <body>
                    <div style="text-align:center; line-height: 70px;">
                        <h1>device check</h1>
                        <h3>Motor 1 &nbsp&nbsp&nbsp&nbsp&nbsp Nomal</h3>
                        <h3>Motor 2 &nbsp&nbsp&nbsp&nbsp&nbsp Nomal</h3>
                        <h3>Motor 3 &nbsp&nbsp&nbsp&nbsp&nbsp <span style="color:red">Error</span>
                            &nbsp&nbsp&nbsp&nbsp&nbsp <span style="color:red">temperature Error</span></h3>
                        <h3>Motor 4 &nbsp&nbsp&nbsp&nbsp&nbsp Nomal</h3>
                    </div>
            </body>
        </html>
                '''

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)
