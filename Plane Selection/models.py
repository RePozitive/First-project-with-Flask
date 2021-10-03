import mongoengine as me

class Plane(me.Document):           
    plane_type = me.StringField()               
    model = me.StringField()
    weight = me.IntField()
    speed = me.IntField()
    height = me.IntField()
    color = me.StringField()
    count_place = me.IntField()
    image_url = me.StringField()
    meta = {'allow_inheritance': True}                                              # Становится мета классом (наследуется в другие классы)

class MilitaryPlanes(Plane):                                
    count_rockets = me.IntField()
    count_guns = me.IntField()

class CiviliansPlanes(Plane):                                      
    cargo_hold = me.IntField()
    flight_range = me.StringField()
