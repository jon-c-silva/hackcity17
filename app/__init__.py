from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

bike_shops = [
    {
		'id': 1,
		'name': u'East Central Cycles',
		'address=': u'18 Exmouth Market, Clerkenwell, London EC1R 4QE',
		'latitude' : 51.5254231,
		'longitude' : -0.1097451
    },
    {
		'id': 2,
		'title': u'FULLCITY CYCLES',
		'address': u'72 Leather Ln, Clerkenwell, London EC1N 7TR',
		'latitude' : 51.5210264,
		'longitude' : -0.1097559
    }
]

@app.route('/bike-shops', methods=['GET'])
def get_bike_shops():
    return jsonify({'bike_shops': bike_shops})

@app.route('/bike-shops/<int:bike_shop_id>', methods=['GET'])
def get_bike_shop(bike_shop_id):
	bike_shop = [bike_shop for bike_shop in bike_shops if bike_shop['id'] == bike_shop_id]
	if len(bike_shop) == 0:
		abort(404)
	return jsonify({'bike_shop': bike_shop[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/bike-shops', methods=['POST'])
def create_bike_shop():
	if not request.json or not all(field in request.json for field in ['name', 'address', 'latitude', 'longitude']):
		abort(400)
	bike_shop = {
		'id': bike_shops[-1]['id'] + 1,
		'name': request.json['name'],
		'address': request.json.get('address'),
		'latitude': request.json.get('latitude'),
		'longitude': request.json.get('longitude')
	}
	bike_shops.append(bike_shop)
	return jsonify({'bike_shop': bike_shop}), 201

@app.route('/bike-shops/<int:bike_shop_id>', methods=['PUT'])
def update_bike_shop(bike_shop_id):
	bike_shop = [bike_shop for bike_shop in bike_shops if bike_shop['id'] == bike_shop_id]
	if len(bike_shop) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'name' in request.json and not isinstance(request.json['name'],str):
		abort(400)
	if 'address' in request.json and not isinstance(request.json['address'],str):
		abort(400)
	if 'latitude' in request.json and not isinstance(request.json['latitude'],float):
		abort(400)
	if 'longitude' in request.json and not isinstance(request.json['longitude'],float):
		abort(400)
	bike_shop[0]['name'] = request.json.get('name', bike_shop[0]['name'])
	bike_shop[0]['address'] = request.json.get('address', bike_shop[0]['address'])
	bike_shop[0]['latitude'] = request.json.get('latitude', bike_shop[0]['latitude'])
	bike_shop[0]['longitude'] = request.json.get('longitude', bike_shop[0]['longitude'])
	return jsonify({'bike_shop': bike_shop[0]})

@app.route('/bike_shops/<int:bike_shop_id>', methods=['DELETE'])
def delete_bike_shop(bike_shop_id):
	bike_shop = [bike_shop for bike_shop in bike_shops if bike_shop['id'] == bike_shop_id]
	if len(bike_shop) == 0:
		abort(404)
	bike_shops.remove(bike_shop[0])
	return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)




