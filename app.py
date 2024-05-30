from flask import Flask,render_template, url_for, redirect, request, session, jsonify, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc, or_
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, logout_user
from datetime import timedelta
from utils import *
import random
import sys
import os

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

app.permanent_session_lifetime = timedelta(minutes=25)   #temporaneo

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)    
    username = db.Column(db.String(30), nullable = False, unique = True)    
    password = db.Column(db.String(250), nullable = False)

    def __init__(self, username = None,password = None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}, password {self.password}>'
    
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(50), nullable = False)
    text = db.Column(db.String(100), nullable = False)
    stars = db.Column(db.String(1), nullable = True)   

    def __init__(self, name = None, text = None, stars = None):
        self.name = name
        self.text = text
        self.stars = stars

    def __repr__(self):
        return f'<User {self.name} says "{self.text}" and leaves {self.stars} stars>'

class Cities(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)    
    like_messi = db.Column(db.Integer)    
    save_messi = db.Column(db.Integer)
    nome = db.Column(db.String(20), nullable = False)
    paese = db.Column(db.String(20), nullable = False)
    photo = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(250), nullable = False)
    iata = db.Column(db.String(5), nullable = True)

    def __init__(self,like = 0, save = 0, nome = None, paese = None, photo = None, iata = None):
        self.like = like
        self.save = save
        self.nome = nome
        self.paese = paese
        self.photo = photo
        self.iata = iata

    def __repr__(self):
        return f'<City {self.nome} in {self.paese}, likes: {self.like_messi}, saves: {self.save_messi} photo: {self.photo}> iata: {self.iata}'

class Like(db.Model):
    __tablename__ = 'likes'
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    cities_id = db.Column(db.Integer, db.ForeignKey('cities.id'), primary_key = True)

    users_like = db.relationship("Users", backref=db.backref("users_like", uselist=False))
    cities_like = db.relationship("Cities", backref=db.backref("cities_like", uselist=False))

class Saves(db.Model):
    __tablename__ = 'saves'
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    cities_id = db.Column(db.Integer, db.ForeignKey('cities.id'), primary_key = True)

    users_save = db.relationship("Users", backref=db.backref("users_save", uselist=False))
    cities_save = db.relationship("Cities", backref=db.backref("cities_save", uselist=False))

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cities_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    comment = db.Column(db.String(1000), nullable=True)

    users_comments = db.relationship("Users", backref=db.backref("users_comments", uselist=False))
    cities_has_comments = db.relationship("Cities", backref=db.backref("cities_has_comments", uselist=False))

db.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

@app.route("/")
def main_route():
    cities=Cities.query.all()

    '''
    SELECT users.nome, comments.cities_id, comments.comment FROM comments JOIN users on users_id = id
    '''
    db_comments = db.session.query(
        Users.username,  # Cambiato 'nome' in 'username' perché 'nome' non esiste nella classe Users
        Comments.cities_id,
        Comments.comment
    ).join(Comments, Users.id == Comments.users_id).all()
    truncated_comments= []
    for com in db_comments:
        ind = com[0].index('@')
        truncated_username = com[0][:ind]  
        truncated_comment = (truncated_username,) + com[1:]  
        truncated_comments.append(truncated_comment)
    print(truncated_comments)
    liked=[]
    if 'username' in session and 'password' in session and 'id' in session:
        user_id = session['id']
        liked_cities = db.session.query(Cities.photo).join(Like, Cities.id == Like.cities_id).filter(Like.users_id == user_id).all()
        liked_photos = [city.photo for city in liked_cities]
 
        saved_cities = db.session.query(Cities.photo).join(Saves, Cities.id == Saves.cities_id).filter(Saves.users_id == user_id).all()
        saved_photos = [city.photo for city in saved_cities]
    else:
        liked_photos = []
        saved_photos = []
    random.shuffle(cities)  #to randomize img shown in index.html

    return render_template("index.html", cities=cities, liked=liked_photos, saved=saved_photos, db_comments = truncated_comments)


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
        password = request.form.get("password_input1")
        password_verify = request.form.get("password_input2")

        password_ok = verify_password(password_verify)

        user = Users.query.filter_by(username = email).first()
        if not user:
            return render_template("forgot.html", user_alive = False, password_match = True, password_quality = True, email_sent = False)
        if password == password_verify and password_ok:

            user.password = password_verify
            db.session.commit()

            #qui mi rimanda alla pagina principale, una pagina intermedia che mi mostra che è andato tutto bene?
            return redirect(url_for("login"))
        
        elif not password_ok:
            return render_template("confirm_forgot.html", password_quality = False)
            
        elif password != password_verify:
            return render_template("confirm_forgot.html", password_match = False)

        
    else:
        return render_template("confirm_forgot.html")

@app.route('/aboutus', methods = ["GET", "POST"])
def aboutus():
     #SELECT * FROM feedback WHERE stars = 5
    reviews = Feedback.query.filter(or_(Feedback.stars == 5, Feedback.stars == 4)).all() #per essere piu umili prendiamo anche le 4 stelle
    reviews = reviews[:10]
    random.shuffle(reviews)
    if request.method == "POST":
        name = request.form.get("name")
        msg = request.form.get("subject")
        rating = request.form.get("sendmedata")
        feed = Feedback(name, msg, rating)
        db.session.add(feed)
        db.session.commit()
        
        print(feed)
        return render_template('aboutus.html', feed=True,reviews = reviews)
    else:
        return render_template('aboutus.html', feed=False, reviews = reviews)

@app.route('/<something>')
def goto(something):
    return redirect(url_for('main_route'))

@app.route("/logout")
def logout():
    logout_user()
    session.clear()

    return redirect(url_for("main_route"))

@app.route("/like", methods = ["GET"])
def like():

    #query per i like
    liked_cities=[]
    foru=[]
    if 'username' in session and 'password' in session and 'id' in session:
        liked_cities = db.session.query(Cities.nome, Cities.photo, Cities.iata,Cities.description, func.count('*').label('total_likes')) \
                        .join(Like, Cities.id == Like.cities_id) \
                        .filter(Like.users_id == session['id']) \
                        .group_by(Cities.nome) \
                        .order_by(desc('total_likes'))\
                        .all()


        #questa query mi serve per i per te
        foru = db.session.query(Cities.nome, Cities.photo,Cities.id, Cities.like_messi).order_by(Cities.like_messi).all()
        foru = foru[:5:-1]
        
        # print(liked_cities, end = "\n\n\n")

        for t in liked_cities:
            print(t)

    size = len(liked_cities)

    return render_template("like.html", city_photo_list=liked_cities, for_u_list = foru, size=size)

@app.route("/favorite")
def favorite():
    saved_ph = []
    if 'username' in session and 'password' in session and 'id' in session:
        user_id = session['id']
    
        saved_cities = db.session.query(Cities.nome, Cities.photo)\
                            .join(Saves, Cities.id == Saves.cities_id)\
                            .filter(Saves.users_id == user_id)\
                            .all()
        saved_ph = [(city.nome, city.photo) for city in saved_cities]
    e=random.randint(1, 4)
    random.shuffle(saved_ph)
    return render_template("favorite.html", saved_ph=saved_ph, e=e)

@app.route('/leavealike', methods = ["POST"])
def leave_like():
    form_sent = request.form
    #print(form_sent)

    if 'username' in session and 'password' in session and 'id' in session:

        city_id = form_sent.getlist('primarykey')[0]
        city = Cities.query.filter_by(id = city_id).first()
        
        #debug
        if not city:
            raise Exception('id not found, nso che cazzo è successo')
        
        user_id = session.get('id')
        
        like = Like.query.filter_by(users_id = user_id, cities_id = city_id).first()
        if like:
            city.like_messi -= 1
            db.session.delete(like)
            db.session.commit()
            print("ao rimuovo il like")
            status_code = {"code" : "201"}
        
        else:

            city.like_messi += 1

            like = Like()
            like.users_id = user_id
            like.cities_id = city_id
            db.session.add(like)
            db.session.commit()


            print("ao metto il like")
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
        
        #debug
        if not city:
            raise Exception('id not found, donno what happened')
            sys.exit(-1)        

        user_id = session.get('id')

        save = Saves.query.filter_by(users_id = user_id, cities_id = city_id).first()
        if save:
            city.save_messi -= 1
            db.session.delete(save)
            db.session.commit()
            print("ao rimuovo il save")
            status_code = {"code" : "202"}
        else:
            city.save_messi += 1

            save = Saves()
            save.users_id = user_id
            save.cities_id = city_id
            db.session.add(save)
            db.session.commit()


            print("ao metto il save")
            status_code = {'code' : '200'}

    else:
        print('utente non loggato!')
        status_code = {'code' : '400'}
    
    return jsonify(status_code)


@app.route('/postcomments', methods = ["POST"])
def post_comments():
    msg_sent = request.form.get('comments')
    city_id = request.form.get('city_key')
    user_id = session.get('id')

    '''
    INSERT INTO comments (users_id, cities_id, comment) VALUES (user_id, city_id, msg_sent);
    '''
    
    

    new_comment = Comments(users_id=user_id, cities_id=city_id, comment=msg_sent)
    db.session.add(new_comment)
    db.session.commit()
    user_name = Users.query.filter_by(id = user_id).first()
    name = user_name.username[:user_name.username.index('@')] #per trasformare abc@ex.com in abc
    # print(user_id)
    # print(user_name)
    # print("------------", name)

    status_code = {'name':name}
    print("tutto ok zi")
    return jsonify(status_code)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
