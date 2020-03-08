
from face_detection import DetectLandmarks
from makeup_image import ApplyMakeup

if __name__ == '__main__':
    AM = ApplyMakeup()
    #output_file = AM.apply_lipstick('/Users/meytalguetta/Desktop/photos/meytal/meytalProfile.jpg', 220,20,60)
    output_file = AM.apply_lipstick('C:\\Users\\Sariel\\PycharmProjects\\DigitalMakeup\\before.jpg', 220, 20, 60)
    #C:\Users\Sariel\Documents\DigitalMakeupProject