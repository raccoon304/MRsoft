from importlib.resources import contents
from flask import Flask, render_template, request, redirect
import sys


app = Flask(__name__)

""" @app.route("/")
def hello():
    return render_template("first.html")
 """

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
            <h1><a href ="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
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
    return template(getcontents(), '<h2>welcome</h2>Hello, WEB')


""" 
@app.route("/second")
def se():
    return render_template("second.html")

@app.route("/third")
def th():
    return render_template("third.html") """

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




if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)
