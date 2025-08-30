from sqlalchemy.orm import sessionmaker
from .engine import engine

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)