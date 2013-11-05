# App in Django with MongoDB

App in [Django](https://docs.djangoproject.com) for to host MovieManiacs at iic2173.
It uses [Django mongodb engine](http://django-mongodb-engine.readthedocs.org)


## Instalation 

Requires: PIP & Python 2.7.1 (at least, I used that )
### Django
```bash
#  https://docs.djangoproject.com/en/dev/topics/install/
$ pip install Django==1.5.5
```

### MongoDB
```bash
# http://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/
$ brew update
$ brew install mongodb

#to run
$ mongob
$ mongo
```
Examples at http://docs.mongodb.org/manual/tutorial/getting-started/

### Django mongodb engine
```bash
# http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html

# uses virtualenv, so be careful where your python is running. It is useful to not be interfering with your other Django apps
$ sudo pip install virtualenv
$ sudo virtualenv myproject
$ source myproject/bin/activate

# requiered dependencies
$ sudo pip install git+https://github.com/django-nonrel/django@nonrel-1.3
$ sudo pip install git+https://github.com/django-nonrel/djangotoolbox@toolbox-1.3
$ sudo pip install git+https://github.com/django-nonrel/mongodb-engine@mongodb-engine-1.3

```

## Usage

### Start
```bash
# if you instaled with virtual env and have Python Command already fixed in the Bash , run  the follow to start :
$ gojango/bin/python manage.py shell

# Remember mongo must be running
$ mongod
```


### Examples
```bash
#create some movie in the Python console
>>> from movies.models import Movie, Actor, Tag, Director
>>> m = Movie(title="Iron Man", 
...     text = "hen wealthy industrialist Tony Stark is forced to build an armored suit after a life-threatening incident, he ultimately decides to use its technology to fight against evil.",
...     year = "2008",
...     director = Director(name = "Jon Favreau"),
...     actors = [Actor(name = "Robert Downey Jr.", character="Tony Stark" ),
...     Actor(name = "Gwyneth Paltrow", character="Pepper Potts") ],
...     tags = [Tag(name="Action"), Tag(name="Adventure"), Tag(name="Sci-Fi")]
...     ).save()
>>> Movie.objects.get(title="Iron Man")
```



