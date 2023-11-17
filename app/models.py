from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    user_type = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Crop(Base):
    __tablename__ = "crops"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    image_id = Column(Integer, nullable=False)


class Disease(Base):
    __tablename__ = "diseases"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    crop_id = Column(Integer, ForeignKey(
        "crops.id", ondelete="CASCADE"), nullable=False)
    crop = relationship("Crop")  # Fetches relationship data for us


class Remedy(Base):
    __tablename__ = "remedies"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    image_id = Column(Integer, nullable=False)
    disease_id = Column(Integer, ForeignKey(
        "diseases.id", ondelete="CASCADE"), nullable=False)
    disease = relationship("Disease")  # Fetches relationship data for us
