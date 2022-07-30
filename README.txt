    1  pyenv shell 3.8.13
    2  curl https://cli-assets.heroku.com/install.sh | sh
    3  heroku -v
    4  pip install gunicorn psycopg2
    5  pip freeze > requirements.txt 

    # Faz login
    7  heroku login -i
    #Cria app
    8  heroku create blog-curso-ocean
  
    #Cria Banco
   13  heroku addons:create heroku-postgresql:hobby-dev --app blog-curso-ocean

   14  history > README.txt 
    # Vê a config do app
        heroku config --app blog-curso-ocean
