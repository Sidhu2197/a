from flask import Flask


from models import person


def register_routes(app,db):


    @app.route('/')
    def index():
        people=person.query.all()
        return str(people)