from flask import Flask, render_template # Por  convenção o nome da classe começa com letra maiúscula

app = Flask("hello")
#app = Flask("index")

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/meucontato")
def meuContato():
    return render_template("index.html")
    
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