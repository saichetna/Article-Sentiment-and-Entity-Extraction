from sqlalchemy import create_engine, Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLite database
DATABASE_URL = "sqlite:///articles.db"
Base = declarative_base()

# Define the Articles table schema
class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    entities = Column(JSON, nullable=False)
    sentiment = Column(String, nullable=False)

# Create a new SQLite engine and session
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Create the table if it doesn't exist
Session = sessionmaker(bind=engine)
session = Session()

def store_article_data(url, content, entities, sentiment):
    # Create a new article record
    article = Article(
        url=url,
        content=content,
        entities=entities,
        sentiment=sentiment
    )
    
    # Add the article to the database and commit the changes
    session.add(article)
    session.commit()
