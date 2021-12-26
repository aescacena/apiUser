# Example API Rest with Flask

# Index

- [Database](#Database)
- [Endpoints](#endpoints)
- [Requisitos](#requisitos)
- [Steps to start](#run)

# Database <a name="database"></a>

The database contains the users table, it contains the following fields:

* `id`: INTEGER PRIMARY KEY AUTOINCREMENT
* `name`: TEXT NOT NULL
* `last_name`: TEXT NOT NULL
* `user_name`: TEXT NOT NULL,
* `email`: TEXT NOT NULL

# Endpoints <a name="endpoints"></a>

## GET /users

Gets all users

**Response**

```json
[
    [
        1,
        "User_1",
        "User_1_1",
        "u_1",
        "u_1@users.com"
    ],
    [
        1,
        "User_2",
        "User_2_1",
        "u_2",
        "u_2@users.com"
    ]
]
```

## POST /user

Add user with the indicated parameters

**Parameters**

|          Name | Required |  Type   |
| -------------:|:--------:|:-------:|
|     `name` | required | string  |
|     `last_name` | required | string  |
|     `user_name` | required | string  |  
|     `email` | required | string  |  

**Response**

```
True
```


## DELETE /user/<user_name>

Removes the user received as a parameter from the database

**Parameters**

|          Name | Required |  Type   |
| -------------:|:--------:|:-------:|
|     `user_name` | required | string  |

**Response**

```
True
```

## GET /user/<user_name>

Get user indicated by parameter

**Parameters**

|          Name | Required |  Type   |
| -------------:|:--------:|:-------:|
|     `user_name` | required | string  |

**Response**

```json
[
    [
        1,
        "User_1",
        "User_1_1",
        "u_1",
        "u_1@users.com"
    ]
]
```

# Requirements <a name="requirements"></a>

Used libraries

```python
alembic==1.7.5
aniso8601==9.0.1
click==8.0.3
Flask==2.0.2
Flask-Admin==1.5.8
Flask-Cors==3.0.10
Flask-Jsonpify==1.5.0
flask-marshmallow==0.14.0
Flask-Migrate==3.1.0
Flask-RESTful==0.3.9
Flask-SQLAlchemy==2.5.1
flask-swagger==0.2.14
greenlet==1.1.2
importlib-metadata==4.10.0
importlib-resources==5.4.0
itsdangerous==2.0.1
Jinja2==3.0.3
Mako==1.1.6
MarkupSafe==2.0.1
marshmallow==3.14.1
marshmallow-sqlalchemy==0.27.0
pytz==2021.3
PyYAML==6.0
six==1.16.0
SQLAlchemy==1.4.29
Werkzeug==2.0.2
WTForms==3.0.1
zipp==3.6.0

```

# Steps to start <a name="run"></a>


1. Download project

```
git clone https://github.com/aescacena/apiUser.git
```

2. Go to directory:

```
cd apiUser
```

3. Install * pip * to be able to install packages in python and install * virtualenv * as a virtual environment.

```
sudo apt install python-pip
sudo pip install virtualenv
```

4. Create virtual environment and activate it

```
python3 -m venv env
source env/bin/activate
```

5. Install libraries indicated in the requirements.txt file

```
sudo env/bin/pip install -r requirements.txt
```

6. Run application

```
python3 users/main.py
```


