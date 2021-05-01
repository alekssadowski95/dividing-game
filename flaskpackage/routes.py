from flask import render_template, redirect, url_for, session, request
from flaskpackage import app, db
from flaskpackage.forms import checkResultForm
from random import randrange


class DivisionTask():
    def __init__(self, dividend, divisor, result):
        self.dividend = dividend
        self.divisor = divisor
        self.result = result

def create_random_division_task(difficulty): 
    value = 9
    if difficulty == 1:
        min_value = 1
        max_value = 9
    elif difficulty == 2:
        min_value = 10
        max_value = 99
    elif difficulty == 3:
        min_value = 100
        max_value = 999
    elif difficulty == 4:
        min_value = 1000
        max_value = 9999
    elif difficulty == 5:
        min_value = 10000
        max_value = 99999

    divisor = randrange(2, 9)
    result = randrange(min_value, max_value)
    dividend = result * divisor
    division_task = DivisionTask(dividend=dividend, divisor=divisor, result=result)  
    return division_task

@app.route('/', methods=['GET', 'POST'])
def home():
    form = checkResultForm()
    session['DIFFICULTY'] = 3 
    if request.method == 'GET':
        if 'DIFFICULTY' not in session: 
            session['DIFFICULTY'] = 1 
        if 'SKILL' not in session: 
            session['SKILL'] = 0
        if 'DIVISION_CREATED' not in session: 
            session['DIVISION_CREATED'] = False
        if session['DIVISION_CREATED'] == False:
            division_task = create_random_division_task(session['DIFFICULTY'])
            session['DIVIDEND'] = division_task.dividend
            session['DIVISOR'] = division_task.divisor
            session['RESULT'] = division_task.result
            session['DIVISION_CREATED'] = True
    if form.validate_on_submit():
        if int(form.result.data) == session['RESULT']:
            session['SKILL'] = session['SKILL'] + 1
            return redirect(url_for('result', result='CORRECT!'))
        else:
            return redirect(url_for('result', result='WRONG!'))      
    return render_template('home.html', dividend=session['DIVIDEND'], divisor=session['DIVISOR'], result=session['RESULT'], skill=session['SKILL'], form=form)

@app.route('/result/<result>', methods=['GET'])
def result(result):
    session['DIVISION_CREATED'] = False
    return render_template('result.html', result=result)
