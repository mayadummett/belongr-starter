from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

engine = create_engine('sqlite:///belongr.db')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
    db_session.commit()

# This is the table of users.
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.id, self.email!r}>'

# This is the table of student organizations.
class Student_Organization(Base):
    __tablename__ = 'student_organizations'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f'<User {self.id, self.name!r}>'

# This is the table of ratings.
class Rating(Base):
    __tablename__ = 'ratings'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    student_organization_id = Column(Integer, ForeignKey(Student_Organization.id), nullable=False)
    racial_identity = Column(Integer, nullable=True)
    ethnic_identity = Column(Integer, nullable=True)
    gender_identity = Column(Integer, nullable=True)
    sexual_orientation = Column(Integer, nullable=True)
    socioeconomic_status = Column(Integer, nullable=True)
    religious_identity = Column(Integer, nullable=True)
    disability_identity = Column(Integer, nullable=True)

    def __init__(self, user_id=None, student_organization_id=None, racial_identity=None, ethnic_identity=None, gender_identity=None, sexual_orientation=None, socioeconomic_status=None, religious_identity=None, disability_identity=None):
        self.user_id = user_id
        self.student_organization_id = student_organization_id
        self.racial_identity = racial_identity
        self.ethnic_identity = ethnic_identity
        self.gender_identity = gender_identity
        self.sexual_orientation = sexual_orientation
        self.socioeconomic_status = socioeconomic_status
        self.religious_identity = religious_identity
        self.disability_identity = disability_identity

    def __repr__(self):
        return f'<User {self.id, self.user_id, self.student_organization_id, self.racial_identity, self.ethnic_identity, self.gender_identity, self.sexual_orientation, self.socioeconomic_status, self.religious_identity, self.disability_identity!r}>'
    