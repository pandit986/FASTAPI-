
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from fastapi import FastAPI, Depends

# 1. Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 2. Create database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# 3. Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 4. Create base class for database models
Base = declarative_base()


# 5. Create User table model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


# 6. Create database tables
Base.metadata.create_all(bind=engine)

# 7. Create FastAPI application
app = FastAPI()


# 8. Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 9. GET API to fetch all users
@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
