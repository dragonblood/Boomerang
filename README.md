# Boomerang [![Django CI](https://github.com/dragonblood/Boomerang/actions/workflows/django.yml/badge.svg)](https://github.com/dragonblood/Boomerang/actions/workflows/django.yml)
[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dragonblood/Boomerang&page=editor&open_in_editor=README.md
## 1. About:

A Beautifully animated sentiment and Entity responsive analyser. Designed using SCSS, JavaScript. This project is built using Google’s natural language API which processes User-given text and returns a JSON response, which is presented pleasingly using chartsJS to a user. The Project is deployed using Google Cloud AppEngine.

## 2. Steps To Follow:
```
### Conda method
git clone https://github.com/dragonblood/Boomerang.git
cd Boomerang
conda env create --file boomerang.yml
conda activate boomerang
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### OR (PIP method)
```
git clone https://github.com/dragonblood/Boomerang.git
cd Boomerang
pipenv shell
pipenv install
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## 3. Screenshots

<img src="https://github.com/dragonblood/Boomerang/blob/master/screenshot/Screenshot%20from%202021-01-26%2010-17-46.png"/>
<img src="https://github.com/dragonblood/Boomerang/blob/master/screenshot/Screenshot%20from%202021-01-26%2010-16-52.png"/>

### Please Feel Free to raise an issue.
### Take Permission Before using it in your work.

