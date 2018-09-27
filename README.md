# PrivateSchoolCMS
PrivateSchoolCMS는 엑설과 데이터베이스를 통해 소규모 학원에서 학원관리시스템을 이용할 수 있는 프로그램입니다. 단순히 해당 프로그램을 다운받아 실행시키면 추가적인 서버구매 없이 개인 데스크탑으로 구동이 가능하며 웹으로 손쉽게 동작시킬 수 가 있습니다. 또한 엑셀을 연동하기에 회원차트나 시간표를 형식이 있는 엑셀 문서로 문서화가 가능합니다.

## Getting Started    
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
User Guide: 
###   Environment
```
Windows, Windows Office Excel, python, web   
```
### Before Installing 
[python](https://www.python.org/downloads/)   
```
please download over python 3.0   
```
### Installing

What things you need to install the software and how to install them

1. python package
```
  git clone 
  open windowns cmd
  cd cloned location
  pip install -r requirment.txt
  or
  just use pip_install.bat
  finally
  check yout djang version with pip list
  django must be 1,9 if not pip uninstall and then pip install django==.19 
  ```      
2. running server
```
  python manage.py runserver:8000
  or
  excute runserver.bat file
  ``` 
3. Get to server site
```
  open your browser
  put "localhost:8000"
  and then create user select timetable of yours
  ```
4. Admin Site
```
  localhost:8000/admin
  you can control whole database
  ```     

## Caution
```
  When you create or edit excel sheets you can get some errors
  Thoes are from pywin32.com libraries
  5 handling guide in below
  ``` 
  ### 1. Check your task manager
```
  Check you
  ``` 
## Excel files
### student_excel folder
```
it's created when you make student data in web
```
### tutor_excel/timetable_master.xlsx
```
it's built in
when making a user just select yout timetable
copy and paste
```
### tutor_excel/sales.xlsx
```
daily sales report not timetable 
please don't choose this file user's timetable
```
## Questions
Please make a issues

## Libraries
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

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
