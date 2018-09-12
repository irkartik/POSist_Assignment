# POSist_Assignment

ABOUT THE PROJECT

1. The project has been implemented using Django Framework.
2. Project requires data to be fed using RESTFUL APIs.
3. Database models has been created in the core/models.py file
4. Application logic has been written in the core/views.py file
5. This project implements sqlite database



STEPS TO RUN:

1. Install dependencies
  <code>pip install -r requirements.txt</code>
2. Creating Migrations
  <code>python manage.py makemigrations</code>
3. Apply Migrations to Database
  <code>python manage.py migrate
4. Run the project
  <code> python manage.py runserver</code>
  
  
NOTE: Keep in mind that the web application created requires data to be fed into it via tha API as the UI/UX of the app isn't developed
