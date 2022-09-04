import pyrebase, json

class DBModule:
    def __init__(self):
        with open("./auth/auth.json") as f:
            config = json.load(f)
        
        
        self.firebase = pyrebase.initialize_app(config)
        
    def login(self, id, password):
        pass
    
    def signin(self, id, password, name, email):
        pass
    
    def sensor_data(self, sensordata, sensornumber):
        pass
    
    def get_user(self, uid):
        pass