from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


@app.route('/ninjas')
def show_ninja_form():

    all_dojos = Dojo.get_all()

    return render_template('ninjaform.html', all_dojos = all_dojos)

@app.route('/submit_ninja_form', methods = ['POST'])
def submit_ninja_form():

    Ninja.add_ninjas(request.form)

    return redirect('/')