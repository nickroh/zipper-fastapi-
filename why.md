# Framework 

<p align="center">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdexkRa%2Fbtry6FomFPq%2FKHDq7e0ksrKHm2mR5X3naK%2Fimg.png" width="50%" alt="Cloudtype"/>
</p>

python 으로 api 서버를 만들때 사용할만한 프레임워크로는 **flask**, **django**, **fastapi** 정도가 있다

## Django (장고)

### Django 프레임워크란?
Django는 무료 오픈 소스인 python 웹 프레임워크이다.
Adrian Holovaty와 Simon Willison이 2003년에 만들어졌다.
Django 주요 목표 중 하나가 복잡한 데이터베이스 기반의 웹 사이트를 개발할 수 있도록 하는 것
적은 코드, 낮은 결합 및 재사용성, 연결 가능성 등 빠른 개발에 도움이 됨

### Django 구축 사례
Instagram, Mozilla, Nextdoor 및 clubhouse와 같은 일부 대형 웹사이트에서 사용됨

### Django 장점
MVC (모델-뷰-컨트롤러) 아키텍처를 활용한 데이터 베이스 접근 용이성
ORM (객체 관계형 맵핑), 관계형 데이터베이스, 웹 템플릿, URL 디스패처 등의 여러 가지 구성
Django의 contib 패키지를 활용하여 여러 애플리케이션을 번들로 묶어 재사용 가능하게 함
CSRF (사이트간 요청 위조), 사이트 간 스크립팅, SQL Injection 등의 보안 모듈 제공
구글 사이트맵, GIS 애플리케이션 생성하는 도구
강력한 API 제공하며 인증 및 권한 규칙 기능을 제공
Django 단점
Django 프레임워크의 규칙이 별도로 존재하지 않는다.
소규모 프로젝트에는 적합하지 않다.
단일 패키지로 간주해야 하는 모놀리식 아키텍처이다.
많은 기능과 구성으로 인해 빠른 학습이 어렵다.
개별 프로세스에 대한 요청은 Django 개발 프로세스를 느리게 할 수 있다.

## Flask (플라스크)

### Flask 프레임워크란?
웹 개발에 특정 라이브러리나 도구가 필요하지 않는 마이크로 프레임워크이다.
쉽고 빠른 방법으로 더 낮은 기능을 가진 경량 애플리케이션을 개발하는 것이다.

### Flask 구축 사례
werkzeug , jinja , MarkupSafe , ItsDangerous 등

### Flask 장점
단순하고 간단하게 일부를 쉽게 안전하게 변경할 수 있다.
대규모 네트워크에 배포할 수 있는 모듈식의 응용 프로그램이나 서버를 만들 수 있다.
파이썬을 잘 이해하면 쉽게 응용 프로그램을 개발할 수 있다.
모놀리식 애플리케이션이 아니므로 확장성이 뛰어나다.
Flask 단점
표준화되어 있지 않기때문에 Django 등의 프레임워크 전환이 어려울 수 있다.
개발 확장과 배포를 위해서 라이브러리 및 확장을 많이 검색해봐야 한다.

## FastAPI

### FastAPI 프레임워크란?
python 3.6+ 버전으로 API를 빌드하는데 도움이 되는 현대적인 프레임워크이다.
가장 빠른 파이썬 프레임워크 중 하나로 간주된다. 개발자가 유발하는 버그가 적고 빠르게 개발할 수 있다.

빠른 개발
버그 감소
높고 빠른 성능
FastAPI 구축 사례
Netflix, Uber 등

### FastAPI 장점
웹 서버 WSGI (Web Server Gateway Interface) 및 비동기 ASGI (Asynchronous Server Gateway Interface)을 완벽하게 지원함
OpenAPI, JSON 스키마 등의 제공
graphene-python이라는 Python 라이브러리로 GraphQL API를 쉽게 구축 가능함
Oauth 2.0 및 외부 공급자와 잘 통합된다.
더 적은 노력과 디버깅 시간으로 애플리케이션을 생성하는 데 도움이 되는 자동 완성 기능을 제공
중첩된 JSON 요청에도 개발자의 데이터 유형을 검증하는 도움이 됨
### FastAPI 단점
FastAPI는 새로운 프로임워크라서 커뮤니티 등의 교육 정보가 매우 적다.
응용 프로그램을 개발할 때 FastAPI 응용 프로그램에서 모든 것을 같이 패키징 해야 하기 때문에 기본 파일이 매우 길거나 복잡해질 수 있다.

## Django vs Flask vs FastAPI 비교

### 패키지
Django 라이브러리에는 전체 스택 웹 개발 프레임워크로 간주될 수 있는 2500개 이상의 패키지가 있다.
Flask < FastAPI < Django 순이다.

### 커뮤니티
Django 프레임워크는 다양한 용도로 사용되기 때문에 Flask, FastAPI 보다 먼저 출시되어 가장 많은 커뮤니티를 보유하고 있다.
Flask도 여러 교육 정보가 있으며 FastAPI가 최신 프레임워크로 외부 정보 수가 매우 적다.
FastAPI < Flask < Django 순이다.

### 성능
FastAPI는 고성능에 중점을 두고 있기 때문에 모든 프레임워크 중에서 가장 빠른 프레임워크이다.
Flask는 마이크로 프레임워크 기능으로 Django 보다는 더 높은 성능을 제공한다.
Djagno < Flask < FastAPI 순이다.

### 유연성
업데이트 변경 사항이 필요할 경우 응용 프로그램 일부를 변경할 수 있는데 Flask가 거의 모든 부분에서 지원하고 있으므로 가장 유연하다고 볼 수 있다.
Djagno < FastAPI < Flask 순이다.





### References
[https://yscho03.tistory.com/109](https://yscho03.tistory.com/109)


# Database

파이썬 프레임워크들이 전반적으로 postgresql을 좋아하는듯하니 이걸 쓰는게 좋지않나 싶다

