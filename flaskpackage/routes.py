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

def get_difficulty():
    value = randrange(1, 100)
    difficulty = 1
    if value >= 1 and value <= 60:
        difficulty = 3
    if value > 60 and value <= 90:
        difficulty = 4
    if value > 90 and value <= 95:
        difficulty = 5
    if value > 95 and value <= 100:
        difficulty = 10
    return difficulty

def get_score():
    score = 0
    if session['DIFFICULTY'] == 1:
        score = 5
    if session['DIFFICULTY'] == 2:
        score = 10
    if session['DIFFICULTY'] == 3:
        score = 25
    if session['DIFFICULTY'] == 4:
        score = 100
    if session['DIFFICULTY'] == 5:
        score = 500
    if session['DIFFICULTY'] == 6:
        score = 1000
    if session['DIFFICULTY'] == 7:
        score = 2000   
    if session['DIFFICULTY'] == 8:
        score = 5000 
    if session['DIFFICULTY'] == 9:
        score = 10000 
    if session['DIFFICULTY'] == 10:
        score = 25000 
    return score

@app.route('/', methods=['GET', 'POST'])
def home():
    form = checkResultForm()
    if request.method == 'GET':
        if 'DIFFICULTY' not in session: 
            session['DIFFICULTY'] = 1 
        if 'SCORE' not in session: 
            session['SCORE'] = 0
        if 'DIVISION_CREATED' not in session: 
            session['DIVISION_CREATED'] = False
        if session['DIVISION_CREATED'] == False:
            session['DIFFICULTY'] = get_difficulty()
            division_task = create_random_division_task(session['DIFFICULTY'])
            session['DIVIDEND'] = division_task.dividend
            session['DIVISOR'] = division_task.divisor
            session['RESULT'] = division_task.result
            session['DIVISION_CREATED'] = True
    if form.validate_on_submit():
        if int(form.result.data) == session['RESULT']:
            session['WIN_SCORE'] = get_score()
            session['SCORE'] = session['SCORE'] + session['WIN_SCORE']
            return redirect(url_for('result', result='CORRECT!'))
        else:
            return redirect(url_for('result', result='WRONG!'))      
    return render_template('home.html', dividend=session['DIVIDEND'], divisor=session['DIVISOR'], result=session['RESULT'], difficulty=session['DIFFICULTY'], form=form, score=session['SCORE'])

@app.route('/result/<result>', methods=['GET'])
def result(result):
    session['DIVISION_CREATED'] = False
    return render_template('result.html', result=result, score=session['SCORE'], win_score=session['WIN_SCORE'])

@app.route('/credits', methods=['GET'])
def credits():
    return render_template('credits.html', score=session['SCORE'])
