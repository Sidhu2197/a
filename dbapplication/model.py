from model import db

class person(db.model):
    __tablename__='people'

    pid=db.Column(db.Integer,primary_key=True)
    name=db.column(db.Text,nullable=false)
    age=db.column(db.Integer,nullable=false)
    job=db.column(db.Text,nullable=false)


    def __repr__(self):
        return f'person with name{self.name} and age {self.age}'
    