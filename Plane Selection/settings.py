class Config(object):
    DEBUG = False
    MONGO_URI = "mongodb+srv://RePozitive:Senkin1965@cluster0.euqll.mongodb.net/Project_planes?retryWrites=true&w=majority"
    MONGODB_SETTINGS = {
        "db": "Planes_project",
        "host": MONGO_URI,
    }
