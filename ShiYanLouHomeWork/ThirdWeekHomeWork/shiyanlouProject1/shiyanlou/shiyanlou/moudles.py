from sqlalchemy import Date

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)
