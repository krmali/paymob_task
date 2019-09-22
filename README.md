***Paymob Messages***  

***API endpoints:***
  	- *api/token/* : to acquire JWT  
  	- *api/token/refresh/* : to refresh JWT  
  	- *api/messages/* : get all messages  
  	- *api/messages/#*: to get message detail of specific message  
  	- *api/users/*: get all users  
  	- *api/user/#/*: to get message detail of specific user  
  	- *api/user/1/messages/*: get messages of that specific user  


***Webapp endpoints:***  
	- *admin/* : admin  
  	- *wall/*  : home page of the app.  
  		-authed and non-authed user can see list of messages order by date descendingly.  
  	- *signup/* : go to signup page.  
  		-**if signup is completed successfully, activation url is printed to server log**  
  	- *activate/+token*: to activate account after signup. **url should be printed to prompt**  
  	- *new_msg/*: get new message page and post new message  
  	- *django authentication urls*  


***Packages Used:***  
	- *django*  
	- *djangorestframework*  
	- *djangorestframework_simplejwt*: for JWT implementation for the API endpoints  


***Running Commands:***  
	- *git clone https://github.com/KareemAliRahman/paymob_task.git*  
	- *pip install pipenv*  
	- *pipenv install*  
	- *pipenv shell*  
	- *python manage.py makemigrations*  
	- *python manage.py migrate*  
  	- *python manage.py loaddata users.json*  
  	- *python manage.py loaddata messages.json*  
	- *python manage.py runserver*  
  
