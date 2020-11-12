# _autodjango_basic_

#### What it do :
- creates a near-blank, one-page, **django web app** in `~/your_projects_directory/your_project_name`, hence forth writen as: _~/../_
- creates and activates a **virtual environment**
  - installs **django 3.0.8** and dependencies
  - starts a **django project** `project_master`
  - starts a **django app** `app_main`
  - creates and migrates **database :**\
    prompts for :\
    $ `user_name`\
    $ `user_password`\
    _~/../src/db.sqlite3_
  - creates and edits **html** templates :\
    _~/../src/templates/base.html_\
    _~/../src/templates/app_main/home.html_
  - and optionally, **starts the development server** ... there's a (y/n)\
    home page : **localhost:8000**\
    admin log in page : **localhost:8000/adimn**

#### How to do :
1. Clone this repo into
_.~/your_projects_directory/_
2. _~/$_ `cd` `your_projects_directory`
3. _~/$_ `python` `autodjango_basic.py` `your_project_name`
4. Autodgango makes and edits the following directories and files:
    -  _your_project_name / src / project_master / settings.py_
    -  _your_project_name / src / project_master /_
    -  _your_project_name / src / app_main /_
    -  _your_project_name / src / app_main / migrations /_
    -  _your_project_name / src / templates / base.html_
    -  _your_project_name / src / templates / app_main /_
    -  _your_project_name / src / templates / app_main / home.html_
    -  _your_project_name / src / static /_
    -  _your_project_name / src / static / css /_
    -  _your_project_name / src / static / css /main.css_
    -  _your_project_name / src / static / js /_
    -  _your_project_name / src / static / js /main.js_
    -  _your_project_name / src / static / media /_

5. _~/$_ `a_user_name` ... for the database and admin login

6. _~/$_ `an_email` ... or not ...

7. _~/$_ `a_password` ... twice

8. _~/$_ `y` ... to run the server now

9. Go to **localhost:8000** to see your empty home page.
  - _~/../src/templates/app_main/home.html_\
   is presented in a block, in the body of\
  _~/../src/templates/base.html_;\
 both of those files need `your_attention`.
  - _~/../src/static/css/main.css_\
  is styling those html files... nearly... `your_attention(main.css).also`.

10. Log into **localhost:8000 / admin**
11. Open _~/.../_ in a code editor and make stuff happen avec the html, css, js, and py.
Allons-y!
