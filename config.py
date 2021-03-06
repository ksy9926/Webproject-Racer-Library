import os
BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI : 데이터베이스 접속 주소
# SQLALCHEMY_TRACK_MODIFICATIONS : SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'main.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# secret_key 설정 (session을 사용하기 위해서 필요, 설정안하면 에러남)
SECRET_KEY="dev"
