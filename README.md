# FnF-REST-API

A REST-API for storing and finding Family and Friends info, built using Django REST Framework.

## How to Access:
Auth Endpoints: 
* http://s4dman.pythonanywhere.com/api/token/
* http://s4dman.pythonanywhere.com/<br>username: guest<br>password: hidjango

## Features
- JSON Web Token Authentication
- GET/POST/PUT/DELETE friends info eg. name, dob, address, facebook, instagram etc.


*User getting refresh and access token using username and passowrd:*
![image](https://user-images.githubusercontent.com/9642377/78633196-f1ff5680-786e-11ea-90dc-062157e19505.png)

*User sending access token as Bearer to authenticate and access the API:*
![image](https://user-images.githubusercontent.com/9642377/78633213-02173600-786f-11ea-875f-9f8a9a365ecb.png)

*API returning friend's information :*
![image](https://user-images.githubusercontent.com/9642377/78633254-1ce9aa80-786f-11ea-92e2-7917b647309f.png)


## Thanks:

Django REST Framework: https://www.django-rest-framework.org/ 

Simple JWT: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html

**_For learning purpose only_!**


