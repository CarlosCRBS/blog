from flask import Flask, render_template # Por  convenção o nome da classe começa com letra maiúscula
from datetime import datetime

app = Flask("hello")
#app = Flask("index")

#mock do banco de dados -- simulação
posts = [
    {
        "title": "O meu primeiro Post",
        "body": "Aqui é o texto do 1º Post",
        "author": "CarlosCRBS",
        "created": datetime(2022,7,25)
    },
     {
        "title": "O meu segundo Post",
        "body": "Aqui é o texto do 2º Post",
        "author": "CarlosCRBS",
        "created": datetime(2022,7,26)
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

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