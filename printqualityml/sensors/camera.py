import cv2

class CameraSensor:
    def __init__(self, source):
        self.cam = cv2.VideoCapture(source)
        
    def capture(self):
        ret, frame = self.cam.read()
        return frame if ret else None
