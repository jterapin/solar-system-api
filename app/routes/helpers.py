from app.models.planet import Planet
from flask import abort, make_response, jsonify

# helper function to validate
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response(jsonify(f"Planet {planet_id} is invalid"), 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        return abort(make_response(jsonify(f"Planet {planet_id} does not exist"), 404))
    return planet
