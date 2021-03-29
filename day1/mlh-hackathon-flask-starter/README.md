# ToDo App

This is a simple REST API for a todo app created using hackathon boilerplate for new Flask web applications created by [Major League Hacking](https://github.com/MLH).

- [Installation Guide](#installation-guide) - How to get started with a new Flask app
- [User Guide](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/USER_GUIDE.md) - How to develop apps created with this starter project
- [Contributing Guide](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/CONTRIBUTING.md) - How to contribute to the project

# <a name='installation-guide'>Installation Guide</a>

This project requires the following tools:

- Python - The programming language used by Flask.
- SQLITE - A relational database system.

To get started, install Python and Postgres on your local computer if you don't have them already. A simple way for Mac OS X users to install Postgres is using [Postgres.app](https://postgresapp.com/). You can optionally use another database system instead of Postgres, like [SQLite](http://flask.pocoo.org/docs/1.0/patterns/sqlite3/).

## Getting Started

**Step 1. Clone the code into a fresh folder**

```
$ git clone git@github.com:roshanrajeev/lhd-share.git
$ cd mlh-hackathon-flask-starter
```

**Step 2. Create a Virtual Environment and install Dependencies.**

Create a new Virtual Environment for the project and activate it. If you don't have the `virtualenv` command yet, you can find installation [instructions here](https://virtualenv.readthedocs.io/en/latest/). Learn more about [Virtual Environments](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments).

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Next, we need to install the project dependencies, which are listed in `requirements.txt`.

```
(venv) $ pip install -r requirements.txt
```

Now we're ready to start our server which is as simple as:

```
(venv) $ flask run
```

Open http://localhost:5000 to view it in your browser.

The app will automatically reload if you make changes to the code.
You will see the build errors and warnings in the console.

# What's Included?

- [Flask](http://flask.pocoo.org/) - A microframework for Python web applications
- [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/) - A Flask extension for making modular applications
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - A Flask extension that adds ORM support for your data models.
- [Werkzeug](http://werkzeug.pocoo.org/) - A Flask framework that implements WSGI for handling requests.
- [Bootstrap 4](https://getbootstrap.com/) - An open source design system for HTML, CSS, and JS.
- [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.

# Code of Conduct

We enforce a Code of Conduct for all maintainers and contributors of this Guide. Read more in [CONDUCT.md](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/CONDUCT.md).

# License

The Hackathon Starter Kit is open source software [licensed as MIT](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/LICENSE.md).
