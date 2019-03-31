# Popit
Intro to django framework w/jquery (Login/Logout)


TO RUN: ##(First Time OR or if you delete migrate files and/or database FILE)
python manage.py makemigrations
python manage.py migrate
python manage.py runserver ##(This line alone is sufficent for running app and being able to view in web broswer)

TO access admin portal:
if admin  doesnt exist create a superuser. Otherwise go straight to step 3
1)To Create a super user go to command prompt navigate to app folder containing manage.py file and type: python manage.py createsuperuser
2) Follow messages on command prompt for creating account. Once done go to step 3
##NOTE: SUPER USER is still a user so you can also log into web app with account you created as super user
3)Go to admin page and login

