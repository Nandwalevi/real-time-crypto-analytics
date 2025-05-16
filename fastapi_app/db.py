import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Updated Supabase connection string
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the CryptoPrice table in the crypto_analytics schema
class CryptoPrice(Base):
    __tablename__ = "crypto_prices"
    __table_args__ = {"schema": "crypto_analytics"}
    id = Column(String, primary_key=True)
    coin_id = Column(String, index=True)
    price_usd = Column(Float)
    timestamp = Column(DateTime)

# Create the schema and table
with engine.connect() as connection:
    connection.execute("CREATE SCHEMA IF NOT EXISTS crypto_analytics")
Base.metadata.create_all(bind=engine)