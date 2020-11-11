Creates a blank-ish, one-page django project called `your_project_name` in a virtual environment and runs the server.     
- home page: ... _localhost:8000/_
- admin page: ... _localhost:8000/adimn/_
- database: ... _your_project_name /src / db.sqlite3_
- templates: ... _base.html_ ... _app_main / home.html_

#### How to:
1. Clone this repo into
_.~/your_projects_directory/_
2. On the command line
  - $ `cd` `your_projects_directory`

  - $ `python` `autodjango/autodjango.py` `your_project_name`

3. Autodgango makes the following directories and files:
  - _your_project_name / src / project_master / settings.py_
  - _your_project_name / src / project_master /_
  - _your_project_name / src / app_main /_
  - _your_project_name / src / app_main / migrations /_
  - _your_project_name / src / templates / base.html_
  - _your_project_name / src / templates / app_main /_
  - _your_project_name / src / templates / app_main / home.html_
  - _your_project_name / src / static /_
  - _your_project_name / src / static / css /_
  - _your_project_name / src / static / css /main.css_
  - _your_project_name / src / static / js /_
  - _your_project_name / src / static / js /main.js_
  - _your_project_name / src / static / media /_

4. $ `a_user_name`

5. $ `an_email` ... or not ...

6. $ `a_password` ... twice

7. $ `y` ... to run the server now

8. Log into _localhost:8000 / admin_
9. Go to _localhost:8000_ to see your empty home page.\
Styles from _your_project_name / src / static / css /main.css_ are being applied; go replace them
10. Open _~/ your_project_name /_ in a code editor and start <div>ing and .style{ ing }
