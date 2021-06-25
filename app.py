from flask import Flask
from flask import render_template
from flask import request

app = Flask("my_first_app")

@app.route('/', methods=["GET"])
def home():
    name = request.args.get("name")
    cname = request.args.get("company")
    # print(name,cname)

    # name = ["Nikhil",'Prathamesh']
    template = render_template('home.html',myname=name,cname = cname)
    return template



@app.route('/new')
def new():
    return "You are in new app"


@app.route('/myform')
def myForm():
    template = render_template('forms.html')
    return template
