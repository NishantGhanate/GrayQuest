## GreyQuest Assignment


### ToDo List 

- [x] MemeApp
    - [x] Create Register page functionality with fields validations 
    - [x] Login Auth 
    - [x] Ask cookie consent and store in db  if declined then alert message & logout
    - [x] Consume Meme Api , show 5 me me 
    - [x] Session cookie / temp cookie 
    - [x] If consent accepted show cookie stored

----
### Demo  :-

| Website       | URL                  |
| ------------- | ------------------------------ |
|    Heroku     | https://grayquestmeme.herokuapp.com/|

&nbsp;

### Run project

```sh
 > git clone https://github.com/NishantGhanate/GrayQuest

 > cd GrayQuest

 > virtualenv venv

 > venv\Scripts\activate

 > pip install -r requirements.txt

 > python manage.py makemigrations

 > python manage.py migrate 

 > python manage.py createsuperuser

 > python manage.py runserver
```

### Run project on heroku

```sh
 > Create app in Heroku 

 > Connect via Github add git repo & branch

 > Deploy Brach 
```
# Debug Heroku
> Check project has ( runtime.txt , procfile ) and correct content
[runtime.txt](https://github.com/NishantGhanate/GrayQuest/blob/main/runtime.txt)
[procfile](https://github.com/NishantGhanate/GrayQuest/blob/main/Procfile)

> For Static files check whitenoise setup in [settings.py](https://github.com/NishantGhanate/GrayQuest/blob/main/GrayQuest/settings.py)

> If using DB makesure its connected to its other online batabase or any other batabase

