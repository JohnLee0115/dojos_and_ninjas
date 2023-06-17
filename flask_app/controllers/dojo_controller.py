from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.dojo_model import Dojo

@app.route('/')
def send_to_dojos():
    return redirect('/dojos')

@app.route('/dojos')
def show_dojos():

    all_dojos = Dojo.get_all()

    return  render_template('index.html', all_dojos = all_dojos)

@app.route('/dojos/add/', methods = ['POST'])
def add_dojo():

    Dojo.add_dojo(request.form)

    return redirect('/')

@app.route('/dojos/<int:id>')
def show_dojo_ninjas(id):

    one_dojo_ninjas = Dojo.get_one_dojo({'id' : id })

    return render_template('show.html', one_dojo_ninjas = one_dojo_ninjas)