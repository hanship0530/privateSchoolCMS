# PrivateSchoolCMS(감자스무디 공개SW대회)
PrivateSchoolCMS는 엑설과 데이터베이스를 통해 소규모 학원에서 학원관리시스템을 이용할 수 있는 프로그램입니다.   
단순히 해당 프로그램을 다운받아 실행시키면 추가적인 서버구매 없이 개인 데스크탑으로 구동이 가능하며 웹으로 손쉽게 동작시킬 수 가 있습니다.   
또한 엑셀을 연동하기에 회원차트나 시간표를 형식이 있는 엑셀 문서로 문서화가 가능합니다.  

## Getting Started    
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.      
###   Environment
Windows, Django 1.9
### Before Installing 
please download over python 3.0     
[python](https://www.python.org/downloads/)     
### Installing

What things you need to install the software and how to install them

- python package
```
open windowns cmd
pip install requirment.txt
```       
### Caution
This program only works on Windows, Django 1.9
Please check your django version with "pip list"
## Running

```
python manage.py runserver 0.0.0.0:8000 
```       
## Detail
### django.models
After modify django models

```
python manage.py makemigrations
python manage.py migrate
```

### templates
web html files
### students, attendance, payments, dashboard
django apps
### static
javascript files
### student_excel, tutor_excel
timetable, student lesson table excel files
## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - Excel Editor Library
* [pywin32](https://pypi.org/project/pywin32/) - Excel Editor Library
* [sb-admin2](https://github.com/code-geek/sbadmin-django) - bootstrap dashboard
* [sb-admin2](https://startbootstrap.com/template-overviews/sb-admin-2/) - bootstrap dashboard
* [bootstrap](http://getbootstrap.com/) - bootstrap
* [Loading jquery](https://www.jqueryscript.net/loading/jQuery-Plugin-To-Handle-CSS3-Powered-Spinners-Loaders-Loading-js.html) - bootstrap loading jquery
* [Lobibox](http://lobianijs.com/site/lobibox) - Lobibox

## References
* [https://simpleisbetterthancomplex.com/](https://simpleisbetterthancomplex.com/)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
