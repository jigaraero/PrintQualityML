import random
class TemperatureSensor:
    def __init__(self, port):
        self.port = port
    def read(self):
        # Replace with actual sensor integration
        return {'hotend': random.uniform(200,220), 'bed': random.uniform(60,70)}
