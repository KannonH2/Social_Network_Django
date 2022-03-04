# Social Network application

This application is a social network. It is a simple application that allows users to create an account, login, and post messages.
allows users to follow other users and see their posts, like posts and see a list of users who liked the post, comment on posts and see a list of comments
and see a list of users who have followed the user.

---

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/KannonH2/Social_Network_Django.git
$ cd Social_Network_Django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Walkthrough

Before you interact with the application, go to 
```sh
$ python manage.py createsuperuser
```
after that you can login in `http://127.0.0.1:8000/admin` and manage the site  
  
---
  
## Terms of use:

This Application was maded with learning purpose. Feel free to use it for your own projects.

---

## Created by: 

### KannonH2
### [LinkedIn](https://www.linkedin.com/in/fernando-haring-dev/)