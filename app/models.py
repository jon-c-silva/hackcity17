from app import db

class BikeShop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    name = db.Column(db.String(120), index=True, unique=True)
    address = db.Column(db.String(120), index=True)
    phone = db.Column(db.String(10), index=True)
    website = db.Column(db.String(120), index=True)
    postcode = db.Column(db.String(7), index=True)

    @property
    def serialize(self):
        """Return object data in serializable format"""
        return {
            'id'        : self.id,
            'latitude'  : self.latitude,
            'longitude' : self.longitude,
            'name'      : self.name,
            'address'   : self.address,
            'phone'     : self.phone,
            'website'   : self.website,
            'postcode'  : self.postcode
        }
