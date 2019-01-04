# PrivateSchoolCMS
PrivateSchoolCMS는 엑설과 데이터베이스를 통해 소규모 학원에서 학원관리시스템을 이용할 수 있는 프로그램입니다. 단순히 해당 프로그램을 다운받아 실행시키면 추가적인 서버구매 없이 개인 데스크탑으로 구동이 가능하며 웹으로 손쉽게 동작시킬 수 가 있습니다. 또한 엑셀을 연동하기에 회원차트나 시간표를 형식이 있는 엑셀 문서로 문서화가 가능합니다.
## Overview
### [Watch Demo Video](https://youtu.be/yk7QZ5b2Udo)
[![Watch the video](main.PNG)](https://youtu.be/yk7QZ5b2Udo)

## User's Guide
[To User's Guide](https://github.com/dxdiag20/privateSchoolCMS/wiki)
## Bootcamp  
개인용 데스크탑에 다운 받아 바로 사용이 가능합니다.
### Operating Environment
```
Windows over 10,    
Windows Office Excel over 2013,     
python over 3.5 64bit,    
chrome recommended       
```
### Installation
Please install [python 3.5](https://www.python.org/downloads/)     
1. Python packages
```
 - Project download
 $ git clone
 - Open CMD WINDOWS as administor.   
 - move to download location.     
 $ cd download location    
 - install libraries    
 $ pip install -r requirment.txt
 - 위 방법이 아닌 한번에 하는 방법
   다운 받은 폴더로 이동 하여 "pip_install.bat"을 클릭하여 실행
 - 마지막으로 설치 된 장고의 버전 확인 
 $ pip list
 - Django must be 1.9 version. So if it is NOT please re install django.      
   Use this option when you install "pip install django==1.9      
  ```      
2. Run 
```
  $ python manage.py runserver:8000
  Or
  Click runserver.bat    
  ``` 
3. Access "Private CMS" on browser   
```
  Open your browser    
  put "localhost:8000" on browser    
  sign up and register your time sechdule file    
  finally click login    
  ```
4. Admin Site
```
  You can access admin site below address   
  localhost:8000/admin
  ID: admin Password: privatecms
  ```     
## Caution!
 [To Caution Guide](https://github.com/dxdiag20/privateSchoolCMS/wiki/4.-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0%EA%B0%80%EC%9D%B4%EB%93%9C)
```
  프로그램 사용시 에러가 날 수 있습니다.   
  그에 관련하여 대처방법을 기술 해놓았습니다.   
  ``` 
## Excel files
1. student_excel folder
```
Writing student's lesson tables    
```
2. tutor_excel/timetable_master.xlsx
```
This is time scheudle of teacher and built in program.     
Make this file as teacher and register this file to teacher's account.     
```
3. tutor_excel/sales.xlsx
```
Daily sales note    
```
## Issue   
Please make issue when problem exist.     
If you have further solution, please pull-request       

## Tech
reference following sources
- [Django](https://www.djangoproject.com/) - 장고 웹프레임워크
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - 엑셀 읽기 라이브러리
- [pywin32](https://pypi.org/project/pywin32/) - 엑셀 편집, 생성 라이브러리
- [sb-admin2](https://startbootstrap.com/template-overviews/sb-admin-2/) - 대쉬보드 사이트
- [bootstrap](http://getbootstrap.com/) - 부트스트랩
- [Loading jquery](https://www.jqueryscript.net/loading/jQuery-Plugin-To-Handle-CSS3-Powered-Spinners-Loaders-Loading-js.html) - 로딩 화면 Jquery
- [Lobibox](http://lobianijs.com/site/lobibox) - 부트스트랩 알림창     

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
