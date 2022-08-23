from importlib.resources import contents
from flask import Flask, render_template, request, redirect
import sys


app = Flask(__name__)
a

@app.route("/")
def index():
    return template('<div style = "text-align:center"><h2>welcome</h2>this site PIKA ROBOTICS</div>')


def template(contents, id=None):
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
                    <p><input type ="password" placeholder = "Password" size = 15></p>    
                    <p><input type ="submit" value="create"> </p>
                </div>
            </form>
            
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
    
@app.route("/test/")
def size():
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
                            <option valte="Robot1">Robot1</option>
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
                            <button class="button">Submit</button>
                        </div>
                    </form>
            </body>
        </html>
                '''
if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)
