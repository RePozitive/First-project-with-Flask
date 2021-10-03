class Config(object):
    DEBUG = False
    MONGO_URI = "Your mongorurl here"
    MONGODB_SETTINGS = {
        "db": "Planes_project",
        "host": MONGO_URI,
    }
