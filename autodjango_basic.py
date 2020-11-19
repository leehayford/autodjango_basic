## _autodjango_basic_
##### What it do :
#- creates a near-blank, one-page, **django web app** in `~/your_projects_directory/your_project_name`, hence forth writen as: _~/../_
#- creates and activates a **virtual environment**
#  - installs **django 3.0.8** and dependencies
#  - starts a **django project** `project_master`
#  - starts a **django app** `app_main`
#  - creates and migrates **database :**\
#    prompts for :\
#    $ `user_name`\
#    $ `user_password`\
#    _~/../src/db.sqlite3_
#  - creates and edits **html** templates :\
#    _~/../src/templates/base.html_\
#    _~/../src/templates/app_main/home.html_
#  - and optionally, **starts the development server** ... there's a (y/n)\
#    home page : **localhost:8000**\
#    admin log in page : **localhost:8000/adimn**
##### How to do :
#1. Clone this repo into
#_.~/your_projects_directory/_
#2. _~/$_ `cd` `your_projects_directory`
#3. _~/$_ `python` `autodjango_basic.py` `your_project_name`
#4. Autodgango makes and edits the following directories and files:
#    -  _your_project_name / src / project_master / settings.py_
#    -  _your_project_name / src / project_master /_
#    -  _your_project_name / src / app_main /_
#    -  _your_project_name / src / app_main / migrations /_
#    -  _your_project_name / src / templates / base.html_
#    -  _your_project_name / src / templates / app_main /_
#    -  _your_project_name / src / templates / app_main / home.html_
#    -  _your_project_name / src / static /_
#    -  _your_project_name / src / static / css /_
#    -  _your_project_name / src / static / css /main.css_
#    -  _your_project_name / src / static / js /_
#    -  _your_project_name / src / static / js /main.js_
#    -  _your_project_name / src / static / media /_
#5. _~/$_ `a_user_name` ... for the database and admin login
#6. _~/$_ `an_email` ... or not ...
#7. _~/$_ `a_password` ... twice
#8. _~/$_ `y` ... to run the server now
#9. Go to **localhost:8000** to see your empty home page.
#  - _~/../src/templates/app_main/home.html_\
#   is presented in a block, in the body of\
#  _~/../src/templates/base.html_;\
# both of those files need `your_attention`.
#  - _~/../src/static/css/main.css_\
#  is styling those html files... nearly... `your_attention(main.css).also`.
#10. Log into **localhost:8000 / admin**
#11. Open _~/.../_ in a code editor and make stuff happen avec the html, css, js, and py.
#Allons-y!


import sys
import os
import fileinput

os.system( f'clear' )

# set constants according to platform
SL = ''
MAKE_FILE = ''
PROJECT = str(sys.argv[1]) # project_name
START_APP_MAIN = ''
START_CHROME = ''
CREATE_SUPER_USER = ''
if(sys.platform == 'win32'):
    SL = '\\'
    MAKE_FILE = f'type nul >'
    ACTIVATE_VENV = f'{ PROJECT }{ SL }scripts{ SL }activate_this.py'# project_name\\sripts\\activate
    CREATE_SUPER_USER =  f'winpty python'
    START_CHROME = f'start chrome 127.0.0.1:8000 127.0.0.1:8000/admin'

elif(sys.platform == 'linux'):
    SL = '/'
    MAKE_FILE = f'touch'
    ACTIVATE_VENV = f'{ PROJECT }{ SL }bin{ SL }activate_this.py'
    CREATE_SUPER_USER = f'python'
    START_CHROME = f'start chrome localhost:8000 localhost:8000/admin'

# virtual environment
PROJECT_SRC = f'{ PROJECT }{ SL }src{ SL }'

# django project
PROJECT_MASTER = f'{ PROJECT_SRC }project_master{ SL }'
MANAGE_PY = f'{PROJECT_SRC}manage.py'
CREATE_SUPER_USER += f' { MANAGE_PY } createsuperuser'
SETTINGS_PY = f'{ PROJECT_MASTER }settings.py'
URLS_PY = f'{ PROJECT_MASTER }urls.py'
DATABASE = f'{ PROJECT_SRC }db.sqlite3'

# django app
APP_MAIN = f'{ PROJECT_SRC }app_main'
APP_MAIN_MODELS_PY = f'{ APP_MAIN }{ SL }models.py'
APP_MAIN_ADMIN_PY = f'{ APP_MAIN }{ SL }admin.py'
APP_MAIN_VIEWS_PY = f'{ APP_MAIN }{ SL }views.py'
DJANGO_START_APP = f'django-admin startapp app_main'
# templates
TEMPLATES = f'{ PROJECT_SRC }templates{ SL }'
TEMPLATES_APP_MAIN = f'{ TEMPLATES }app_main{ SL }'

# static
STATIC = f'{ PROJECT_SRC }static{ SL }'
CSS = f'{ STATIC }css{ SL }'
JS = f'{ STATIC }js{ SL }'
MEDIA = f'{ STATIC }media{ SL }'

os.system( f'mkdir { PROJECT }' )
os.system( f'virtualenv { PROJECT }' )

# activate virtual environment
with open(ACTIVATE_VENV) as f:
    code = compile(f.read(), ACTIVATE_VENV, 'exec')
    exec(code, dict(__file__=ACTIVATE_VENV))

    print(f'project: { PROJECT_SRC }')

    os.system( f'pip install django==3.0.8')

    os.system( f'mkdir { PROJECT_SRC }')
    os.system( f'django-admin startproject project_master { PROJECT_SRC }')
    print( f'django-admin startproject project_master { PROJECT_SRC } ... OK')

# create requirements file for deployment ...
    os.system(f'pip freeze > { PROJECT_SRC }requirements.txt')

# create database
    os.system(f'{ MAKE_FILE } { DATABASE }')
    os.system( f'python { MANAGE_PY } makemigrations')
    os.system( f'python { MANAGE_PY } migrate')
    os.system( f'{ CREATE_SUPER_USER }')

# create main django application
    os.system( f'mkdir { APP_MAIN }{ SL }')
    os.system( f'{ DJANGO_START_APP } { APP_MAIN }')

# create html templates
    os.system( f'mkdir { TEMPLATES }')
    os.system( f'mkdir { TEMPLATES_APP_MAIN }')

    #edit { TEMPLATES }base.html
    basehtml ='{% load static %}\n'
    basehtml +='<!doctype html>\n'
    basehtml +='<html  lang="en">\n'
    basehtml +='\t\t<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">\n'
    basehtml +='\t<head>\n'
    basehtml +='\t\t<script src="{% static "js/main.js" %}"></script>\n'
    basehtml +='\t\t<link rel="stylesheet" href="{% static "css/main.css" %}" type="text/css">\n'
    basehtml +='\t</head>\n'
    basehtml +='\t<body>\n'
    basehtml +=f'\t\t<header id="base-header"><div>{ TEMPLATES } base.html header - { sys.platform }</div></header>\n'
    basehtml +='\t\t{% block main %}{% endblock main %}\n'
    basehtml +=f'\t\t<footer id="base-footer"><div>{ TEMPLATES } base.html footer - { sys.platform }</div></footer>\n'
    basehtml +='\t</body>\n'
    basehtml +='</html>\n'
    with open( f'{ TEMPLATES }base.html', "a") as b:
        b.write(basehtml)

    #edit { TEMPLATES_APP_MAIN }home.html"
    homehtml ='{% extends "base.html" %}\n'
    homehtml +='{% block main %}\n'
    homehtml +='\t<div id=app-main-home>app_main/home.html content</div>\n'
    homehtml +='{% endblock main %}\n'
    with open(f'{ TEMPLATES_APP_MAIN }home.html', "a") as h:
        h.write(homehtml)

#create static/css, static/js, atatic/media
    os.system( f'mkdir { STATIC }')

    maincss ='body { \nfont-family: Roboto; \ndisplay: flex; \nflex-direction: column;\n}\n'
    maincss +='#base-header { \ncolor: rgb(28, 101, 173); \n}\n'
    maincss +='#base-footer { \ncolor: rgb(22, 165, 58); \n}\n'
    maincss +='#app-main-home { \ncolor: rgb(209, 135, 24); \n}\n'
    os.system( f'mkdir { CSS }')
    with open(f'{ CSS }main.css', "a") as h:
        h.write(maincss)

    os.system( f'mkdir { JS }')
    with open(f'{ JS }main.js', "a") as h:
        h.write(f'console.log("javascript")')

    os.system( f'mkdir { MEDIA }')

    def replacetxt(file, srch, rep):
        fin = open(file, 'rt')
        data = fin.read()
        data = data.replace(srch, rep)
        fin.close()
        with open(file, 'wt') as fw:
            fw.write(data)
        print( f'edit { file } ... OK')

#edit { SETTINGS_PY }
    replacetxt(
        SETTINGS_PY,
        'INSTALLED_APPS = [',
        "INSTALLED_APPS = [\n\t'app_main',\n"
        )
    replacetxt(
        SETTINGS_PY,
        "'DIRS': []",
        "'DIRS': [\n\tos.path.join(BASE_DIR, 'templates')\n]"
        )
    replacetxt(
        SETTINGS_PY,
        "STATIC_URL = '/static/'",
        "STATIC_URL = '/static/'\nSTATICFILES_DIRS = ( \n\tos.path.join(BASE_DIR, 'static'),\n)\nSTATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')"
        )

#edit { URLS_PY }
    replacetxt(
        URLS_PY,
        'from django.urls import path',
        "from django.urls import path\nfrom app_main.views import (\n\tapp_main_view\n)\n\n"
        )
    replacetxt(
        URLS_PY,
        "urlpatterns = [",
        "urlpatterns = [\n\tpath('', app_main_view, name='app-main-home'),"
        )

#edit { VIEWS_PY }
    replacetxt(
        APP_MAIN_VIEWS_PY,
        '# Create your views here.',
        "from django.http import HttpResponse\n\ndef app_main_view(request, *args, **kwargs):\n\treturn render(request, 'app_main/home.html', {})"
        )

#slap ass
    print(f'***\nproject directory:\n { os.getcwd() }{ SL }{ PROJECT }\n***\n')

    # TODO: open common code editors...
    #print(f'***\n< enter > to skip\n\t< a > to open in atom\n\t< v > to open vscode\n\t< s > to open in sublime\n***\n')
    #if(input() == 'a'): os.system(f'atom  { PROJECT }')
    #elif(input() == 'v'): os.system(f'code { PROJECT }')
    #elif(input() == 's'): os.system(f'sub { PROJECT }')

    print(f'shall we run the server now? y/n:')
    if(input() == 'y'):

        os.system( START_CHROME ) # TODO: open common browsers... add, test browser options...
        os.system( f'python { MANAGE_PY } runserver')
