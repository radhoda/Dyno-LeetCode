import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:smith2000@localhost:5432/postgres')
session = sessionmaker(bind=engine)

Base = sqlalchemy.orm.declarative_base()

question_tags = Table(
    'question_tags', Base.metadata,
    Column('question_id', Integer, ForeignKey('question.qid'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    slug = Column(String, unique=True, nullable=False)

    questions = relationship("Questions", secondary="question_tags", back_populates="topicTags")


class Question(Base):
    __tablename__ = 'questions'
    qid = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    difficulty = Column(String)
    acceptanceRate = Column(Float)
    paidOnly = Column(Boolean)
    topicTags = relationship("Tags", secondary=question_tags, back_populates="questions")


class DatabaseHandler:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session()

    def add_questions(self, questionData):
        for data in questionData:
            newQuestion = Question(
                qid=data['QID'],
                title=data['title'],
                difficulty=data['difficulty'],
                acceptanceRate=data['acceptanceRate'],
                paidOnly=data['paidOnly'],
            )

            for tag_data in data['topicTags']:
                tag_slug = tag_data["slug"]
                tag = self.session.query(Tags).filter_by(slug=tag_slug).first()

                if not tag:
                    tag = Tags(slug=tag_slug)
                    self.session.add(tag)

                newQuestion.topicTags.append(tag)
            self.session.add(newQuestion)

        self.session.commit()
