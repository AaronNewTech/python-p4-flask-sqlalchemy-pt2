#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Owner, Pet

fake = Faker()

# will cause the program to fail quickly when not cofigured this context. The is diffrent from vanilla sqlalchemy
with app.app_context():

    # deletes the records in the database. This is also different from vanilla sqlalchemy
    Pet.query.delete()
    Owner.query.delete()

    # everything here is the same as sqlalchemy

    # creates a new owner and a new pet with the new owner and the new pet arrays to commit the changes to the database
    owners = []
    for n in range(50):
        owner = Owner(name=fake.name())
        owners.append(owner)

    db.session.add_all(owners)

    pets = []
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    for n in range(100):
        pet = Pet(name=fake.first_name(), species=rc(species), owner=rc(owners))
        pets.append(pet)

    db.session.add_all(pets)
    db.session.commit()