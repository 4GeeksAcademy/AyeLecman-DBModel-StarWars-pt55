from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=True)

    favourites_characters: Mapped[List["Favourites_Character"]] = relationship(back_populates="user")
    favourites_planets: Mapped[List["Favourites_Planet"]] = relationship(back_populates="user")

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    skin_color: Mapped[str] = mapped_column(nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[int] = mapped_column(nullable=False)

    favourite: Mapped["Favourites_Character"] = relationship(back_populates="character", uselist=False)

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    diameter: Mapped[int] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    gravity: Mapped[int] = mapped_column(nullable=False)
    population: Mapped[int] = mapped_column(nullable=False)

    favourite: Mapped["Favourites_Planet"] = relationship(back_populates="planet", uselist=False)
    
    
class Favourites_Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False, index=True)
    user: Mapped["User"] = relationship(back_populates="favourites_characters")

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False, index=True, unique=True)
    character: Mapped["Character"] = relationship(back_populates="favourite", uselist=False) 

class Favourites_Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False, index=True)
    user: Mapped["User"] = relationship(back_populates="favourites_planets")

    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False, index=True, unique=True)
    planet: Mapped["Planet"] = relationship(back_populates="favourite", uselist=False) 

