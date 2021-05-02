from flask import render_template, redirect, url_for, session, request
from flaskpackage import app, db
from flaskpackage.models import Score
from flaskpackage.forms import CheckResultForm, EnterNicknameForm
from sqlalchemy import desc
from random import randrange
import secrets


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
    elif difficulty == 10:
        min_value = 1000000
        max_value = 9999999
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
    if value > 90 and value <= 99:
        difficulty = 5
    if value == 100:
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
    if 'NICKNAME_DEFINED' in session and session['NICKNAME_DEFINED'] == True:
        form = CheckResultForm()
        if request.method == 'GET':
            if 'DIFFICULTY' not in session: 
                session['DIFFICULTY'] = 1 
            if 'SCORE' not in session: 
                session['SCORE'] = 0
            if 'WIN_SCORE' not in session: 
                session['WIN_SCORE'] = 0
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
                session['LAST_ENTRY'] = int(form.result.data)
                session['WIN_SCORE'] = get_score()
                session['SCORE'] = session['SCORE'] + session['WIN_SCORE']
                current_score = Score.query.filter_by(uuid=session['UUID']).first()
                current_score.score = session['SCORE']
                db.session.commit()
                return redirect(url_for('result', result='CORRECT!'))
            else:
                session['LAST_ENTRY'] = form.result.data
                session['SCORE'] = session['SCORE'] - 50
                current_score = Score.query.filter_by(uuid=session['UUID']).first()
                current_score.score = session['SCORE']
                db.session.commit()
                return redirect(url_for('result', result='WRONG!'))      
        return render_template('home.html', nickname=session['NICKNAME'], dividend=session['DIVIDEND'], divisor=session['DIVISOR'], result=session['RESULT'], difficulty=session['DIFFICULTY'], form=form, score=session['SCORE'])
    else:
        return redirect(url_for('nickname'))

@app.route('/result/<result>', methods=['GET'])
def result(result):
    session['DIVISION_CREATED'] = False
    return render_template('result.html', result=result, last_entry=session['LAST_ENTRY'], nickname=session['NICKNAME'], score=session['SCORE'], win_score=session['WIN_SCORE'], dividend=session['DIVIDEND'], divisor=session['DIVISOR'], result_value=session['RESULT'], difficulty=session['DIFFICULTY'])

@app.route('/credits', methods=['GET'])
def credits():
    return render_template('credits.html', score=session['SCORE'], nickname=session['NICKNAME'],)

@app.route('/highscore', methods=['GET'])
def highscore():
    scores = Score.query.order_by(desc(Score.score)).all()
    return render_template('highscore.html', score=session['SCORE'], nickname=session['NICKNAME'], scores=scores, uuid=session['UUID'])

def init_player(nickname):
    session['UUID'] = secrets.token_hex(16)
    session['SCORE'] = 0
    session['NICKNAME'] = nickname
    session['NICKNAME_DEFINED'] = True

def commit_to_db(score):
    db.session.add(score)
    db.session.commit()

@app.route('/nickname', methods=['GET', 'POST'])
def nickname():
    if 'NICKNAME_DEFINED' in session and session['NICKNAME_DEFINED'] == True:
        return redirect(url_for('home'))
    form = EnterNicknameForm()
    if form.validate_on_submit():  
        if 'NICKNAME_DEFINED' in session and session['NICKNAME_DEFINED'] == True:
            return redirect(url_for('home')) 
        init_player(form.nickname.data)
        score = Score(uuid=session['UUID'], score=session['SCORE'], nickname=session['NICKNAME'])
        commit_to_db(score)
        return redirect(url_for('home'))
    return render_template('nickname.html', form=form)
