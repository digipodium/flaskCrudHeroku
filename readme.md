to deploy the content to heroku

- create a .gitignore file
    - add flask gitignore content using gitignore.io

- create a Procfile
    - `web: gunicorn app:app`

- heroku account creation
- heroku cli download
- on terminal, inside correct folder
    - `heroku login`
    - `git init`
    - `git add .`
    - `git commit "done and done"`
    - `heroku create flaskappmpt`
    - `git push heroku master`
    - `heroku open`