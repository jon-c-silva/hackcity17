from flask import *
from flask_sqlalchemy import SQLAlchemy
import math

restapi = Flask(__name__)
restapi.config.from_object('config')
db = SQLAlchemy(restapi)

from restapi.models import BikeShop

#Roughly 1 degree of latitude = 110km
#Roughly 1 degree of longitude == 111 * cos(latitude) km

predefinedRadius = [0.5, 1, 2, 3]
predefinedLatRadius = [x/110 for x in predefinedRadius] #in KM
predefinedLonRadius = [lat/(111*math.cos(predefinedLatRadius[i])) for i,lat in enumerate(predefinedRadius)]


@restapi.route('/index')
def index():
    return render_template('Index.html')


@restapi.route('/bikeShops', methods=['GET'])
def get_bikeShops():
    userLatitude = request.args.get('lat',None)
    userLongitude = request.args.get('lon',None)
    print(userLatitude, userLongitude)
    if userLatitude is None or userLongitude is None:
        abort(400)
    userLatitude = float(userLatitude)
    userLongitude = float(userLongitude)
    userJson = {
        'type'      : 'User',
        'geometry'  : {
            'type'          : 'Point',
            'coordinates'   : [userLatitude, userLongitude]
        },
        'properties': {
            'name'  : 'Your location'
        }
    }
    returnList = [bs.serialize for bs in BikeShop.query.all()]
    returnList.append(userJson)

    return jsonify(json_list=returnList)

@restapi.route('/bikeShops/<int:bikeShopId>', methods=['GET'])
def get_bikeShop(bikeShopId):
    bikeShop = BikeShop.query.get(bikeShopId)
    print(bikeShop)
    return jsonify({'bikeShop': bikeShop.serialize})

@restapi.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@restapi.route('/bikeShops', methods=['POST'])
def create_bikeShop():
    if not request.json or not all(field in request.json for field in ['name', 'latitude', 'longitude']):
        abort(400)

    bikeShop = BikeShop(
        name=request.json.get('name'), address=request.json.get('address',''),
        postcode=request.json.get('postcode',''),website=request.json.get('website',''),
        phone=request.json.get('phone',''),latitude=request.json.get('latitude'),
        longitude=request.json.get('longitude'))

    db.session.add(bikeShop)
    db.session.commit()
    return jsonify({'bikeShop': bikeShop.serialize}), 201

@restapi.route('/bikeShops/<int:bikeShopId>', methods=['PUT'])
def update_bikeShop(bikeShopId):
    bikeShop = BikeShop.query.get(bikeShopId)
    bikeShop.name = request.json.get('name', bikeShop.name)
    bikeShop.latitude = request.json.get('latitude', bikeShop.latitude)
    bikeShop.longitude = request.json.get('longitude', bikeShop.longitude)
    bikeShop.address = request.json.get('address', bikeShop.address)
    bikeShop.phone = request.json.get('phone', bikeShop.phone)
    bikeShop.website = request.json.get('website', bikeShop.website)
    db.session.commit()
    return jsonify({'bikeShop': bikeShop.serialize})

@restapi.route('/bikeShops/<int:bikeShopId>', methods=['DELETE'])
def delete_bikeShop(bikeShopId):
    bikeShop = BikeShop.query.get(bikeShopId)
    db.session.delete(bikeShop)
    db.session.commit()
    return jsonify({'result': True})

#@restapi.route('/bikeShops/locate', methods=['GET'])
#def get_nearest_bikeShops():
#    userLatitude = request.args.get('lat',None)
#    userLongitude = request.args.get('lon',None)
#    print(userLatitude, userLongitude)
#    if userLatitude is None or userLongitude is None:
#        abort(400)
#    userLatitude = float(userLatitude)
#    userLongitude = float(userLongitude)
#
#    bikeShops = []
#    for i in range(len(predefinedRadius)):
#        bikeShops = db.session.query(BikeShop).filter(BikeShop.latitude <= userLatitude+predefinedLatRadius[i])# &
#                             # latitude >= userLatitude-predefinedLatRadius[i] &
#                            #  longitude <= userLongitude+predefinedLonRadius[i] &
#                            #  longitude >= userLongitude-predefinedLonRadius[i])
#        if(len(bikeShops) > 0):
#            break;
#    return jsonify(json_list=[bs.serialize for bs in bikeshops])


if __name__ == '__main__':
    restapi.run(debug=True)




