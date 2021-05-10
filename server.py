from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'Cast in the name of God, ye not guilty'

@app.route('/')
def initialize():
    session['comp_choice'] = random.randint(1, 50)
    session['guess'] = 0
    session['guess_count'] = 0
    session['scorelist'] = []
    return redirect('/great_number_game')

@app.route('/game_loop', methods=['POST'])
def gameloop():
    session['guess'] = request.form['guess']
    session['guess_count'] += 1
    return redirect('/great_number_game')

@app.route('/great_number_game')
def gamestart():
    if session['guess_count'] == 0:
        return render_template('index.html', firstround = True)
    while int(session['guess_count']) < 5:
        if int(session['guess']) < int(session['comp_choice']):
            display = "Too low!"
            return render_template('index.html', firstround = False, display = display)
        elif int(session['guess']) > int(session['comp_choice']):
            display = "Too high!"
            return render_template('index.html', firstround = False, display = display)
        elif int(session['guess']) == int(session['comp_choice']):
            return render_template('winscreen.html')
    return render_template('/game_over.html')

@app.route('/highscore', methods=['POST'])
def highscore():
    session['scorelist'].append(form.request['name'], "who did it in ", session['guess_count'], "tries!")
    return render_template('hallofchamps.html')

if __name__ == "__main__":
    app.run(debug=True)