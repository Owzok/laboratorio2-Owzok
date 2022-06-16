from flask_sqlalchemy import SQLAlchemy
import os

db_name = 'lab20'
port = 9173
passw = os.environ.get('pg_pass')
db_path='postgresql://postgres:{}@localhost:{}/{}'.format(passw,port,db_name)
db = SQLAlchemy()

def setup_db(app, db_path=db_path):
    app.config['SQLALCHEMY_DATABASE_URI']=db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app=app
    db.init_app(app)
    db.create_all()
    print('db setted up!')

class Example(db.Model):
    __tablename__ = 'example1'
    id = db.Column(db.Integer, primary_key=True)
    
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def __repr__(self):
        return f'Todo: id={self.id}'

    def format(self):
        return{
            'id': self.id,

        }