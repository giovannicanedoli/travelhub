from flask import Flask,render_template, url_for, redirect, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, logout_user
from datetime import timedelta
from utils import *

import sys

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "HOMEWORK LTW"
#altra roba
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = USERNAME
app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

app.permanent_session_lifetime = timedelta(minutes=25)   #temporaneoo

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)    
    username = db.Column(db.String(30),nullable = False, unique = True)    
    password = db.Column(db.String(250),nullable = False)

    def __init__(self, username = None,password = None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}, password {self.password}>'
    
class Cities(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)    
    like_messi = db.Column(db.Integer)    
    save_messi = db.Column(db.Integer)
    nome = db.Column(db.String(250), nullable = False)
    paese = db.Column(db.String(250), nullable = False)
    photo = db.Column(db.String(250), nullable = False)
    description = db.Column(db.String(250), nullable = False)

    def __init__(self,like = 0, nome = None, paese = None, photo = None):
        self.like = like
        self.nome = nome
        self.paese = paese
        self.photo = photo

    def __repr__(self):
        return f'<City {self.nome} in {self.paese}, likes: {self.like_messi}, photo: {self.photo}>'

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)   
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cities_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    #uselist = False -> un record è associato ad un record delle classi sopra, da mettere???

    users_like = db.relationship("Users", backref=db.backref("users_like", uselist=False))
    cities_like = db.relationship("Cities", backref=db.backref("cities_like", uselist=False))

class Saves(db.Model):
    __tablename__ = 'saves'
    id = db.Column(db.Integer, primary_key=True)   
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cities_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    users_save = db.relationship("Users", backref=db.backref("users_save", uselist=False))
    cities_save = db.relationship("Cities", backref=db.backref("cities_save", uselist=False))

db.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

@app.route("/")
def main_route():
    cities=Cities.query.all()
    return render_template("index.html", cities=cities)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get('username_input')
        password = request.form.get("password_input1")
        password_verify = request.form.get("password_input2")
    
        password_ok = verify_password(password_verify)

        user = Users.query.filter_by(username = username).first()

        if user:
            return render_template("signup.html", user_alive = True)

        if password == password_verify and password_ok:
            user = Users(username, password)
            db.session.add(user)
            db.session.commit()

            session.permanent = True
            
            session['username'] = username
            session['password'] = password
            session['id'] = user.id

            return redirect(url_for("main_route"))
        else:
            return render_template("signup.html", password_ok=password_ok, password=password, password_verify=password_verify)
    elif 'username' in session and 'password' in session:
        return redirect(url_for("main_route"))
    else:
        return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username_input")
        password_verify = request.form.get("password_input")
        user = Users.query.filter_by(username = username).first()
        
        if user and user.password == password_verify:
            login_user(user)           
            session['username'] = username
            session['password'] = password_verify
            session['id'] = user.id

            return redirect(url_for("main_route"))
        
        elif not user:
            return render_template("login.html", something_failed = True, user_not_found = True)
        
        else:
            return render_template("login.html", something_failed = True, user_not_found = False)
        
    elif 'username' in session and 'password' in session and 'id' in session:
        return redirect(url_for("main_route"))
    
    else:
        return render_template("login.html", something_failed = False)

@app.route('/forget', methods = ["GET", "POST"])
def forgotpasswd():
    if request.method == "POST":
        
        username = request.form.get('username_input')

        user = Users.query.filter_by(username = username).first()
        if not user:
            #user is not present in db
            return render_template("forgot.html", user_alive = False, email_sent = False)

        token = generate_reset_token()
        token += username
        
        msg = Message('Reset Password', sender = USERNAME, recipients=[user.username])

        #se nella pagina di confirm_forget metti il token giusto allora vai avanti altrimenti ba
        msg.body = f'Click on this link to reset the password: {url_for("confirm_forget", token = token, _external = True)}'
        mail.send(msg)        

        return render_template("forgot.html", user_alive = True, email_sent = True)
    
    else:
        return render_template("forgot.html")
    
#questa funzione deve essere riscritta
@app.route('/forget/<token>/confirm', methods = ["GET", "POST"])
def confirm_forget(token):
    if request.method == "POST":
        email = token[43:]
        print(email)
        username = request.form.get('username_input')
        password = request.form.get("password_input1")
        password_verify = request.form.get("password_input1")

        password_ok = verify_password(password_verify)

        if username != email:
            return render_template("forgot.html", bad_user = False, user_alive = True, password_match = False, password_quality = False, email_sent = False)
        
        user = Users.query.filter_by(username = username).first()
        if not user:
            #user is not present in db
            return render_template("forgot.html", user_alive = False, password_match = True, password_quality = True, email_sent = False)
        if password == password_verify and password_ok:

            user.password = password_verify
            db.session.commit()
            return redirect(url_for("login"))
            
        elif password != password_verify:
            return render_template("forgot.html", user_alive = True, password_match = False, password_quality = True, email_sent = False)
        else:
            return render_template("forgot.html", user_alive = True, password_match = True, password_quality = False, email_sent = False)
        
    else:
        return render_template("confirm_forgot.html")
    

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/<something>')
def goto(something):
    return redirect(url_for('main_route'))


@app.route("/logout")
def logout():
    logout_user()
    session.clear()

    return redirect(url_for("main_route"))

@app.route("/like")
def like():
    return render_template("like.html")


@app.route('/leavealike', methods = ["POST"])
def leave_like():
    form_sent = request.form
    #print(form_sent)

    if 'username' in session and 'password' in session and 'id' in session:

        city_id = form_sent.getlist('primarykey')[0]
        city = Cities.query.filter_by(id = city_id).first()
        
        
        if not city:
            raise Exception('id not found, nso che cazzo è successo')
        
        city.like_messi += 1
        

        user_id = session.get('id')

        like = Like()
        like.users_id = user_id
        like.cities_id = city_id
        db.session.add(like)
        db.session.commit()


        print("ao è andato tutto bene")
        status_code = {'code' : '200'}

    else:
        print('utente non loggato!')
        status_code = {'code' : '400'}
    

    return jsonify(status_code)


@app.route('/savephoto', methods = ["POST"])
def save_photo():

    form_sent = request.form
    
    if 'username' in session and 'password' in session and 'id' in session:

        city_id = form_sent.getlist('primarykey')[0]
        city = Cities.query.filter_by(id = city_id).first()
        
        if not city:
            raise Exception('id not found, nso che cazzo è successo')
            sys.exit(-1)        

        user_id = session.get('id')
        city.save_messi += 1

        save = Saves()
        save.users_id = user_id
        save.cities_id = city_id
        db.session.add(save)
        db.session.commit()


        print("ao è andato tutto bene")
        status_code = {'code' : '200'}

    else:
        print('utente non loggato!')
        status_code = {'code' : '400'}
    
    return jsonify(status_code)


if __name__ == '__main__':
    app.run(debug=True)
