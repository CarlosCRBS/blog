from flask import Flask, render_template, redirect, url_for # Por  convenção o nome da classe começa com letra maiúscula
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask("hello")
#app = Flask("index")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.String(512))
    #author = db.Column(db.String(32))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author')


db.create_all()

@app.route("/")
def index():
    #Busca no banco os posts
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/populate")
def populate():
    user = User(username="CarlosCRBS", email="carlos.crbs@gmail.com", password_hash='a')
    post1 = Post(title="Post 1", body="Texto do Post1", author=user)
    post2 = Post(title="Post 2", body="Texto do Post2", author=user)
    db.session.add(user)
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/login")
def login():
    return render_template("login.html")





#@app.route("/meucontato")
#def meuContato():
    #return render_template("index.html")
 #   return render_template("index.html", nome="Carlos R B Santos", email="carlos.crbs@yahoo.com.br", telefone="5133409628")
    
#    """
#            <html>
#                <head>
 #               <title> Contatos </title>
 #               </head>
  #              <body>
  #              <h1>Carlos Rafael Batista Santos</h1> 
  #              <h2>carlos.crbs@gmail.com</h2>
  #              <h3>51991957516</h3>
  #              <a href="https://www.oceanbrasil.com/"> Isso é um link </a>
  #              </body>
                
  #           </html>"""

#@app.route("/index")
#def index():
#    i = 1    
#    while (i <= 1000):
#        print(i)
#        i += 1
 
#    return "Cheguei Aqui!"