from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import os 
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL) 

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)