from app import db

class BikeShop(db.Model):
    latitude = db.Column(db.Float, primary_key=True)
    longitude = db.Column(db.Float, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    website = db.Column(db.String(120), index=True, unique=True)
    postcode = db.Column(db.String(7), index=True)

    def __repr__(self):
        return '<Bike shop %r>' % (self.name)
