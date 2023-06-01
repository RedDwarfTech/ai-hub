from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os

db_conn = os.environ.get('CLUSTER_POSTGRESQL_CONN')

Base = declarative_base(class_registry={

})

engine = create_engine(db_conn, echo=False)
Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    scope_session = Session()
    try:
        yield scope_session
        scope_session.commit()
    except Exception as e:
        scope_session.rollback()
    finally:
        scope_session.close()
