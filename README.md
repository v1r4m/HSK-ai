# HSK-ai
HSK 기출 지문을 통해 새로운 HSK 문제를 만들어 냅니다. ㅇㅅㅇ~ 

### ?
* pythonanywhere wsgi에 문제가 있는 것 같습니다... wsgi를 고치거나 다른곳에 배포하고싶다...

## quick start
### build tailwindcss
You don't need to specifically run this on node 20, but I didn't tested on other versions.
```
nvm use 20
npm install
npm run build:css
``` 
### run django
```
source /venv/bin/activate
(venv) python3 manage.py runserver
```

### tech stack
* python 3.11
* django 4.2
* node 20