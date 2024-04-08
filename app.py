from flask import Flask,render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "HOMEWORK LTW" #random secret key
db = SQLAlchemy() #inizializzo il db



login_manager = LoginManager()
login_manager.init_app(app)


#il tutorial: https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask-login/
#mette i modelli direttamente dentro al file app.py, non credo sia una buona pratica. Per adesso mi sa 
# che li possiamo lasciare qui, in caso poi spostiamoli.
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)


db.init_app(app)

with app.app_context():
    db.create_all()


# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

@app.route("/")
def main_route():
    return render_template("index.html")

@app.route("/home")
def renderize():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("home"))
        
    return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users(username=request.form.get("username"),
                     password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("sign_up.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


#runna l'app
if __name__ == '__main__':
    app.run(debug=True)