# Yin-Yang-Website

This is the source code for my Yin-Yang Solver Website. For a deployed version of this Solver, please visit https://computing-telu.com/products/yin-yang/

## Local Installation

With this instruction, you will get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The website application requires:

* [Python 3.9.0](https://www.python.org/downloads/release/python-390/) - The Language
* [Django 3.2.10](https://www.djangoproject.com/download/) - The Web Framework
* [pycosat 0.6.3](https://pypi.org/project/pycosat/) - The Library

You need to install those in a virtual environment.

### Creating a Virtual Environment

Choose a folder for the website to run in, and copy the repositories content. Then run the command:

```
python3 -m venv myvenv
```
This results in a new virtual environment called myvenv.

Start the virtual environment by running the activate file in the cmd:
```
myvenv\Scripts\activate
```

### Installing Web Framework and Libraries

Install Django and Pycosat in the virtual environment by running:
```
pip install Django~=3.2.10
pip install pycosat=0.6.3
```
or
```
pip install requirements.txt
```

You can run the app locally by running:
```
python manage.py runserver
```

You can access the running website with the link http://127.0.0.1:8000/.

### Additional note

If you want to learn more about the django framework used in this app, please visit [this tutorial](https://tutorial.djangogirls.org/en/).
