  ## Django REST API para processo WORKALOVE (03/2021) -
 ### Cheff & Receip Backend
 ### Stack: Python + Django Rest Framework + SQlite3 + SwaggerUI
 asgiref + pillow + pytz + sqlparse 

<img src="https://img.icons8.com/dusk/128/000000/python.png"/> <img src="https://github.com/mendesbayout/RestAPI/blob/master/django.svg"/> <img src="https://github.com/mendesbayout/RestAPI/blob/master/swagger.svg"/> <img src="https://github.com/mendesbayout/DjangoRestApi/blob/master/giticons/sqlite.svg"/> 

 #### Introdução

The purpose of this project is to present a simple solution for a Backend position in the company WORKALOVE. Feel Free to download & edit.

The Challenge was basically; as an admin(Cheff), CRUD receips. As an user, request for receips filtering by level of complexity or time consumed, and any other field. Well, as the position is for backend and I have few time; please make sure your user reads the documentation because his frontend is the Swagger itself, and the information he requests, will be in returned in JSON.


:one:Make sure python is installed (included env paths) 

2️⃣ Initialize a new virtual environment: py -m venv env

3️⃣ Activate your virtual env: source venv/bin/activate(Activate1)

4️⃣ Intall dependencies: pip install -r requirements.txt

5️⃣ make sure you have sqlite3 & the dbcheff(from the rep) is on the source

8️⃣ Create superuser : py manage.py createsuperuser ⚠️

9️⃣ Start the local server: py manage.py runserver

Durante esse processo, se tudo estiver de acordo como esperado, teremos as seguintes opções

🔗 https://127.0.0.1:8000/> SWAGGER UI Pagina para consulta de usuario.   
▶️ GET - all cheffs (ler as ids)  
▶️ GET Cheff recipes
▶️ GET specific recipes
   
⚠️
🔗 https://127.0.0.1:8000/admin/ > Pagina de management padrão do Django Rest Framework. Aqui 0 Cheff tem o poder de editar e postar novas receitas, e até incluir novos cheffs

Além de uma documentação o SwaggerUI provém interface a CRUD operations e também opera com o package openAPI para fornecer um endpoint para trabalhos em front end como exemplo. Esse projeto pode ser usado como template para infinitos tipos de RESTfull API's graças a flexibilidade do framework. 

### HEROKU QUICKLY DEPLOY

<img src="https://github.com/mendesbayout/DjangoRestApi/blob/master/giticons/heroku_original_wordmark_logo_icon_146482.svg"/>

As we already have Procfile installed, heroku deploy will only take few seconds... caso não tenha instalado. https://devcenter.heroku.com/articles/heroku-cli

:one: heroku login

2️⃣ heroku git:clone -a apicheff

:three: cd apicheff

:four: git add .

:five: commit -am "make it better"

:six: push heroku master


