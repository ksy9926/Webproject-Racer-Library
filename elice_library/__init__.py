# -- coding: utf-8 --
from flask import Flask, render_template, url_for, jsonify, session, request, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# 전역변수로 db, migrate 객체를 만들어준다. create_app() 함수 안에서 init_app 메서드를 이용해 초기화한다.
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, static_url_path='/static')

    # config.py에 작성한 항목을 app.config 환경 변수로 부르기 위해 app.config.from_object(config) 코드 추가
    app.config.from_object(config)

    # secret_key 설정 (session을 사용하기 위해서 필요, 설정안하면 에러남)
    app.secret_key = 'super secret key'
    
    # db객체를 create_app 함수 안에서 생성하면 블루프린트와 같은 다른 모듈에서 불러올 수 없다.
    # 따라서 db, migrate와 같은 객체는 create_app 함수 밖에서 생성하고, 객체 초기화는 create_app 함수에서 수행한다.
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    from . import load_data

    from . import main_views
    app.register_blueprint(main_views.bp)
    
    return app

# ssh azure@elice-kdt-ai-track-vm-racer-12.koreacentral.cloudapp.azure.com (ssh 접속 끊기 : exit)
# YKHKQyRtrKoixQfA4bzFpw0hmWWIFDZk
# cd racer-library
# source python-env/bin/activate (가상환경 벗어나기 : deactivate)

# export FLASK_APP=elice_library
# export FLASK_ENV=development
# export FLASK_RUN_RELOAD=False
# flask run --host=0.0.0.0 --port=80

# sudo python app.py runserver 0.0.0.0:80

# gunicorn 실행
# gunicorn --bind 0:5000 "elice_library:create_app()"
# 실행중인 gunicorn 보기
# ps -ef | grep gunicorn
# 해당 서버 끄기
# kill -9 process_number(ex. kill -9 3893)


# 또는 
# if __name__ == '__main__':
#    app.run(debug=True, use_reloader=False)

# elice-kdt-ai-track-vm-racer-12.koreacentral.cloudapp.azure.com:5000 주소창 입력