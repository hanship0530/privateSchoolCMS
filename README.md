# PrivateSchoolCMS
PrivateSchoolCMS는 엑설과 데이터베이스를 통해 소규모 학원에서 학원관리시스템을 이용할 수 있는 프로그램입니다. 단순히 해당 프로그램을 다운받아 실행시키면 추가적인 서버구매 없이 개인 데스크탑으로 구동이 가능하며 웹으로 손쉽게 동작시킬 수 가 있습니다. 또한 엑셀을 연동하기에 회원차트나 시간표를 형식이 있는 엑셀 문서로 문서화가 가능합니다.
## Overview
[![Watch the video](main.PNG)](https://www.youtube.com/watch?v=S06boWP3hNE&feature=youtu.be)
### [데모 영상 보러가기](https://www.youtube.com/watch?v=S06boWP3hNE&feature=youtu.be)

## User Guide direct

## 시작하기  
단순히 개인용 데스크탑에 다운 받아 바로 사용이 가능합니다.
###   작동 환경
```
Windows, Windows Office Excel, python, web   
```
### 설치전에
[python](https://www.python.org/downloads/)   
```
3.0이상 버전의 파이썬 설치가 필요합니다.
```
### 설치 하기

프로그램 시작전에 몇가지 설치가 필요합니다.

1. 파이썬 패키지
```
  git clone을 하여 프로젝트를 다운 받습니다. 
  cmd창을 엽니다.
  cd 명령어를 통해 클론한 폴더의 위치로 이동합니다.
  "pip install -r requirment.txt" 명령어를 실행합니다.
  또는
  다운 받은 폴더에서 pip_install.bat 파일을 클릭하여 실행할 수 있습니다.
  마지막으로 
  설치된 장고의 버전을 확인해봅니다. pip list
  장고의 버전은 1.9이여 합니다. 그렇지 않다면 pip uninstall 그리고 pip install django==.19 통해 설치합니다.
  ```      
2. 서버 구동
```
  python manage.py runserver:8000
  or
  excute runserver.bat file
  ``` 
3. 사이트 접속하기
```
  브라우저를 열고
  주소창에 "localhost:8000"
  그리고 회원가입을 하여 아이디를 생성 생성 시 자신의 시간표 파일을 선택합니다.
  그리고 로그인
  ```
4. Admin Site
```
  아래의 주소로 접속하여 데이터베이스를 관리자 권한으로 관리가 가능합니다.
  localhost:8000/admin
  아이디: admin 비밀번호: privatecms
  ```     

## 주의사항
 come to this link to 
```
  프로그램 에러는 대부분 pywin32의 라이브러리 동작에서 일어납니다.
  오류를 해결하는 5가지 방법이 있습니다. 오류시 참고 바랍니다.
  ``` 
  ### 1. 작업관리자 확인
```
  Check you
  ``` 
## Excel files
### student_excel folder
```
학생정보를 생성하면 생기는 파일 입니다. 학생의 수업차트를 기록하는 엑셀 파일입니다.
```
### tutor_excel/timetable_master.xlsx
```
처음부터 내제되어 있는 엑셀 파일입니다.
각 선생님이름으로 파일을 만들며 해당 시간표파일에 시간표를 작성하여 사용자계정 생성시 등록하여야 합니다.
해당 파일을 토대로 시간표를 조회합니다.
```
### tutor_excel/sales.xlsx
```
일 매출대장표입니다.
```
## 오류 해결 
이슈를 요청해주세요. 오류 해결에 대한 요청은 언제든지 환영합니다. 또한
pywin32가 아닌 openpyxl로 엑셀을 편집가능하다면 연락바랍니다. 

## 라이브러리들
* ['Django'](https://www.djangoproject.com/) - 장고 웹프레임워크
* ['openpyxl'](https://openpyxl.readthedocs.io/en/stable/) - 엑셀 읽기 라이브러리
* ['pywin32'](https://pypi.org/project/pywin32/) - 엑셀 편집, 생성 라이브러리
* ['sb-admin2'](https://github.com/code-geek/sbadmin-django) - 장고 호환 깃헙주소
* ['sb-admin2'](https://startbootstrap.com/template-overviews/sb-admin-2/) - 대쉬보드 사이트
* ['bootstrap'](http://getbootstrap.com/) - 부트스트랩
* ['Loading jquery'](https://www.jqueryscript.net/loading/jQuery-Plugin-To-Handle-CSS3-Powered-Spinners-Loaders-Loading-js.html) - 로딩 화면 Jquery
* ['Lobibox'](http://lobianijs.com/site/lobibox) - 부트스트랩 알림창 

## 참고 사이트 
* ['https://simpleisbetterthancomplex.com/'](https://simpleisbetterthancomplex.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
