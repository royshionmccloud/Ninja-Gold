from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key = 'reeeader'

@app.route('/process_money', methods=['POST'])
def n_count():
    locate = request.form['building']
    current_time =  datetime.datetime.now().strftime('%m-%d-%Y %I:%M %p')
    if locate == 'farm':
        gold_in = random.randint(10,20)
    elif locate == 'cave':
        gold_in = random.randint(5,10)
    elif locate == 'house':
        gold_in = random.randint(2,25)
    elif locate == 'casino':
        gold_in = random.randint(-50,50)        
    session['total_gold'] += gold_in
    session['total_moves'] += 1
    if gold_in >= 0:
        message = f"<p class='text-success'>You gained {gold_in} from {locate} {current_time} </p>"
        session['activities'] += message
    elif gold_in < 0:
        message = f"<p class='text-danger'>You lose {gold_in} from {locate} {current_time} </p>"
        session['activities'] += message
    if session['total_moves'] <= 14 and session['total_gold'] == 500:
        message = f"<p class='text-success'>You won the game</p>"
        session['activities'] += message
    elif session['total_moves'] > 14 and session['total_gold'] != 500:
        message = f"<p class='text-danger'>You lose the game</p>"
        session['activities'] += message          
    return redirect('/')


@app.route('/')
def gold():
    if 'total_gold' and 'activities' and 'total_moves' not in session:
        session['total_gold'] = 0
        session['activities'] = ""
        session['total_moves'] = 0
    return render_template('ninjagold.html', message=session['activities'])

@app.route('/destroy_session')
def n_dsess():
    session.clear()
    return redirect('/')














if __name__=="__main__":
    app.run(debug=True)