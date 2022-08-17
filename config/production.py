from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xfc\xb3\xd0rc\xa9i\xd4f\xb9\xbao\xda\xe5\t\x19'
