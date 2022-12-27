from flask import Flask, render_template, url_for, request, flash, abort, session, redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from datetime import datetime

# 'sqlite:///project.db'
# 'postgresql://postgres:123@localhost/db'
# db = SQLAlchemy()
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'Hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SECRET_KEY'] = 'sdasdas'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# db.init_app(app)

# >>> from main import app, db
# >>> app.app_context().push()
# >>> db.create_all()


class Quiz(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    # date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Quiz %r>' % self.id


# with app.app_context():
#     db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stores')
def stores():
    return render_template('about.html')


@app.route('/survey_designer')
def survey_designer():
    #
    # if request.method == 'POST':
    #     if len(request.form) > 2:
    #         flash('Cообщение отправлено')
    #     else:
    #         flash('Error')
    #     print(request.form)
    return render_template('survey_designer.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        disease = request.form['username']
        tebl1 = Quiz(title=disease, intro=disease, text=disease)
        try:
            db.session.add(tebl1)
            db.session.commit()
            return redirect('/')
        except:
            return 'придобавлении квиза произошла ошибка'

    else:
        return render_template('quiz.html')

    # if 'userLogged' in session:
    #     return redirect(url_for('profile', username=session['userLogged']))
    # elif request.method == 'POST' and request.form['username'] == 'selfedu' and request.form['psw'] == '123':
    #     session['userLogged'] = request.form['username']
    #     return redirect(url_for('profile', username=session['userLogged']))
    #
    # return render_template('login.html')


@app.route('/profile/<username>')
def profile(username):
    if 'userLogeed' not in session or session['userLogged'] != username:
        abort(401)
    return f'Пользователь: {username}'


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html')


@app.route('/quiz', methods=['POST', 'GET'])
def quiz():

    if request.method == 'POST':
        disease = request.form['disease']
        tebl1 = Quiz(title=disease, intro=disease, text=disease)
        try:
            db.session.add(tebl1)
            db.session.commit()
            return redirect('/')
        except:
            return 'придобавлении квиза произошла ошибка'

    else:
        return render_template('quiz.html')


if __name__ == '__main__':
    app.run(debug=True)
