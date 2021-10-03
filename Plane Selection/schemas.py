import marshmallow as ma

class PlaneSchema(ma.Schema):
    plane_type = ma.fields.String()                         # Названия полей в модели и схеме должны совпадать
    model = ma.fields.String()
    weight = ma.fields.Integer()
    speed = ma.fields.Integer()
    height = ma.fields.Integer()
    color = ma.fields.String()
    count_place = ma.fields.Integer()
    image_url = ma.fields.String()
    id = ma.fields.String()

class Military(PlaneSchema):
    count_rockets = ma.fields.Integer()
    count_guns = ma.fields.Integer()

class Civilians(PlaneSchema):
    cargo_hold = ma.fields.Integer()
    flight_range = ma.fields.String()

class ModelCivlians(ma.Schema):
    model = ma.fields.String()
    image_url = ma.fields.String()
    model_civilians = ma.fields.List(ma.fields.Nested(Civilians))

class ModelMilitary(ma.Schema):
    model = ma.fields.String()
    image_url = ma.fields.String()
    model_military = ma.fields.List(ma.fields.Nested(Military))   
    
class MakePlanes(ma.Schema):
    model_military = ma.fields.List(ma.fields.Nested(Military))         # создать такую же конструкцию, как в моделе, только с Nested. Логически схема и модель должны совпадать с их объектами
    model_civilians = ma.fields.List(ma.fields.Nested(Civilians))  