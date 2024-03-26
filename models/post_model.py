from app import db


class UserModel(db.Model):

    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key = True)
    model = db.Column(db.String, nullable = False)
    make = db.Column(db.String, nullable = False)

    def save_car(self):
        db.session.add(self)
        db.session.commit()


    def del_car (self):
        db.session.delete(self)
        db.session.commit()

    
    def from_dict(self, car_dict):
        for k, v in car_dict.items():
            setattr(self, k, v)
    # id = fields.Str(dump_only=True)
    # model = fields.Str(required=True)
    # make = fields.Str(required=True)