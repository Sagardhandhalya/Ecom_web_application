## Ecom project set up

### Install pgadmin and postgres app

create database with name __ecom__ in the in the postgress user and update password for the postgress to 9081606040. otherwise you can update settings.py file.

### Install node js 

### Clone this repo 
```c++
git clone -b master <repo url>
```
### Backend Set up 

#### Create virtual env

```c++
$ cd django_ecomerce_backend
$ python3 -m venv new-env 
$ source new-env/bin/activate
```

After this step you will see virtual env name on your terminal.

#### Install deps

```c++
$ pip install -r require.txt 
```
you might run into psycopg2-binary build error refer stackoverflow for that.

#### Run backend server 
```c++
 $ cd ecom
 $ python manage.py migrate
 $ python manage.py runserver
 ```
 Now your server is runnig at 8080 port.


### Frontend Setup

#### install deps 

```c++
$ cd Ecommerceproject 
$ npm install
```

#### run the dev server
```c++
npm run start
```
you will see you UI on http://localhost:3000

#### Cors Error 

You will run into cors error to avoid that add https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?hl=en extention and update this ectentions option accordingly.

