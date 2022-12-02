from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

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
class Ratings(Base):
    __tablename__ = 'ratings'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    student_organization_id = Column(Integer, ForeignKey(Student_Organization.id), nullable=False)
    racial_identity_inclusivity = Column(Integer, nullable=True)
    ethnic_identity_inclusivity = Column(Integer, nullable=True)
    gender_identity_inclusivity = Column(Integer, nullable=True)
    sexual_orientation_inclusivity = Column(Integer, nullable=True)
    socioeconomic_status_inclusivity = Column(Integer, nullable=True)
    religious_identity_inclusivity = Column(Integer, nullable=True)
    disability_identity_inclusivity = Column(Integer, nullable=True)

    def __init__(self, user_id=None, student_organization_id=None, racial_identity_inclusivity=None, ethnic_identity_inclusivity=None, gender_identity_inclusivity=None, sexual_orientation_inclusivity=None, socioeconomic_status_inclusivity=None, religious_identity_inclusivity=None, disability_identity_inclusivity=None):
        self.user_id = user_id
        self.student_organization_id = student_organization_id
        self.racial_identity_inclusivity = racial_identity_inclusivity
        self.ethnic_identity_inclusivity = ethnic_identity_inclusivity
        self.gender_identity_inclusivity = gender_identity_inclusivity
        self.sexual_orientation_inclusivity = sexual_orientation_inclusivity
        self.socioeconomic_status_inclusivity = socioeconomic_status_inclusivity
        self.religious_identity_inclusivity = religious_identity_inclusivity
        self.disability_identity_inclusivity = disability_identity_inclusivity

    def __repr__(self):
        return f'<User {self.id, self.user_id, self.student_organization_id, self.racial_identity_inclusivity, self.ethnic_identity_inclusivity, self.gender_identity_inclusivity, self.sexual_orientation_inclusivity, self.socioeconomic_status_inclusivity, self.religious_identity_inclusivity, self.disability_identity_inclusivity!r}>'
    