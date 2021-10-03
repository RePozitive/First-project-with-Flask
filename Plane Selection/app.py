from flask import Flask, request, abort, jsonify
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

from models import MilitaryPlanes, CiviliansPlanes
from schemas import MakePlanes, ModelCivlians, ModelMilitary, PlaneSchema, Military, Civilians
from settings import Config

make_schema = MakePlanes()
planes_schema = PlaneSchema()
military_schema = Military()
civilians_schema = Civilians()
model_civilians_schema = ModelCivlians()
model_military_schema = ModelMilitary()

def creat_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db = MongoEngine(app)
    register_routes(app)
    if __name__ == "__main__":
        app.run()
    return app  

def register_routes(app):
    @app.route("/military_plane", methods=["POST"])
    def creat_military_plane():
        plane_text = request.get_json()
        plane_military = military_schema.load(plane_text)

        military_plane = MilitaryPlanes(**plane_military)                       # способ 1 по заполнению БД по полям из класса

        military_plane.save()
        return {"id": str(military_plane.id)}

    @app.route("/civilians_plane", methods=["POST"])
    def creat_civilians_plane():
        plane_text = request.get_json()
        plane_civilians = civilians_schema.load(plane_text)

        civilians_plane = CiviliansPlanes(
            plane_type = plane_civilians["plane_type"],                          # заполнить для каждого класса конструктор и вернуть свой уникальный айди
            model = plane_civilians["model"],                                    # способ 2 по заполнению БД по полям из класса
            weight = plane_civilians["weight"],
            speed = plane_civilians["speed"],
            height = plane_civilians["height"],
            color = plane_civilians["color"],
            count_place = plane_civilians["count_place"],
            image_url = plane_civilians["image_url"],
            cargo_hold = plane_civilians["cargo_hold"],
            flight_range = plane_civilians["flight_range"]
            )
        civilians_plane.save()
        return {"id": str(civilians_plane.id)} 

    @app.route("/civilians_plane/<make>", methods=["GET"])
    def make_civilians(make):
        make = CiviliansPlanes.objects(plane_type = make).all()
        if make == None:
            raise abort(404)
        return {"planes": [model_civilians_schema.dump(i) for i in make]}, 200

    @app.route("/military_plane/<make>", methods=["GET"])
    def make_military(make):
        make = MilitaryPlanes.objects(plane_type = make).all()
        if make == None:
            raise abort(404)
        return {"planes": [model_military_schema.dump(i) for i in make]}, 200

    @app.route("/military_plane/<make>/<id>", methods=["GET"])
    def military_plane_id(make, id):
        plane = MilitaryPlanes.objects(plane_type = make, id = id).first()
        if plane == None:
            raise abort(404)
        return military_schema.dump(plane), 200

    @app.route("/civilians_plane/<make>/<id>", methods=["GET"])
    def civiliams_plane_id(make, id):
        plane = CiviliansPlanes.objects(plane_type = make, id = id).first()
        if plane == None:
            raise abort(404)
        return civilians_schema.dump(plane), 200

    @app.route("/civilians_plane/<make>/<id>", methods=["PUT"])
    def update_civilians_plane(make, id):
        update_text = request.get_json()
        update_civilians = civilians_schema.load(update_text)

        plane = CiviliansPlanes.objects(plane_type = make, id = id).update_one(upsert=False, **update_civilians)
        if not plane:
            return {"message": "plane not found"}, 404
        return {"messsage": "Successfully updated"}, 200

    @app.route("/military_plane/<make>/<id>", methods=["PUT"])
    def update_military_plane(make, id):
        update_text = request.get_json()
        update_military = military_schema.load(update_text)

        plane = MilitaryPlanes.objects(plane_type = make, id = id).update_one(upsert=False, **update_military)
        if not plane:
            return {"message": "plane not found"}, 404
        return {"messsage": "Successfully updated"}, 200

    @app.route("/civilians_plane/<make>/<id>", methods=["DELETE"])
    def delet_civilians_plane(make, id):
        plane = CiviliansPlanes.objects(plane_type = make, id = id).delete()
        if not plane:
            return {"message": "plane not found"}, 404
        return {"messsage": "Successfully deleted"}, 200

    @app.route("/military_plane/<make>/<id>", methods=["DELETE"])
    def delet_military_plane(make, id):
        plane = MilitaryPlanes.objects(plane_type = make, id = id).delete()
        if not plane:
            return {"message": "plane not found"}, 404
        return {"messsage": "Successfully deleted military plane"}, 200  

creat_app()


   