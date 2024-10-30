import cv2
import numpy as np
import os
#os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"
from PIL import Image, ImageFont, ImageDraw
import time
import io
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

poppy = ImageFont.truetype("/home/lhsexhibits/Downloads/Poppins-Black.ttf", 72, encoding="unic")
# [h, f, d, sa, s, a]
h1 = [1,0,0,0,0,0]
h2 = [1,0,0,0,0,0]
h3 = [.2, .15, 0, 0, .65, 0]
h4 = [1, 0, 0, 0, 0, 0]
f1 = [.25, .6, 0, 0, .15, 0]
f2 = [.02, .85, 0, 0, .13, 0]
f3 = [0, .65, 0, 0, .35, 0]
f4 = [.1, .65, 0, 0, .22, .03]
d1 = [0, 0, .95, 0, 0, .05]
d2 = [0, 0, .7, 0, 0, .3]
d3 = [0, 0, .9, 0, 0, .1]
d4 = [.15, 0, .7, 0, 0, .15]
sa1 = [0, .02, .01, .97, 0, 0]
sa2 = [0, .07, .06, .84, 0, .03]
sa3 = [0, 0, 0, .51, 0, .49]
sa4 = [.02, 0, 0, .92, .01, .05]
s1 = [.2, .05, 0, 0, .75, 0]
s2 = [.02, .05, 0, 0, .93, 0]
s3 = [.8, 0, 0, 0, .2, 0]
s4 = [0, .6, 0, 0, .4, 0]
a1 = [.2, 0, .7, 0, 0, .1]
a2 = [0, 0, .7, 0, 0, .3]
a3 = [.3, .04, .3, .04, 0, .32]
a4 = [0, 0, .1, 0, 0, .9]
kids = [h1, h2, h3, h4, f1, f2, f3, f4, d1, d2, d3, d4, sa1, sa2, sa3, sa4, s1, s2, s3, s4, a1, a2, a3, a4]

width_s = 1920
height_s = 1080

happy_face=cv2.imread("./1x/happy.png")
happy_face=cv2.resize(happy_face, (int(width_s/13), int(width_s/13)))
fear_face=cv2.imread("./1x/fear.png")
fear_face=cv2.resize(fear_face, (int(width_s/13), int(width_s/13)))
disgust_face=cv2.imread("./1x/disgust.png")
disgust_face=cv2.resize(disgust_face, (int(width_s/13), int(width_s/13)))
sad_face=cv2.imread("./1x/sad.png")
sad_face=cv2.resize(sad_face, (int(width_s/13), int(width_s/13)))
surprise_face=cv2.imread("./1x/surprise.png")
surprise_face=cv2.resize(surprise_face, (int(width_s/13), int(width_s/13)))
anger_face=cv2.imread("./1x/anger.png")
anger_face=cv2.resize(anger_face, (int(width_s/13), int(width_s/13)))
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

base = 40
the_max = 1040
the_diff = the_max - base - 200
happy = base
sad = base
fear = base
anger = base
disgust = base
surprise = base

happy_goal = base
sad_goal = base
fear_goal = base
anger_goal = base
disgust_goal = base
surprise_goal = base

happy_perc = 0
sad_perc = 0
fear_perc = 0
anger_perc = 0
disgust_perc = 0
surprise_perc = 0

markerID = 0
counter = 0

# setup text
font = cv2.FONT_HERSHEY_SIMPLEX
text1 = "Place one of the face cards in the stand"
text2 = "to see what an AI thinks the expression is"
(wid1, bas1), (off_x1, off_y1) = poppy.font.getsize(text1)
(wid2, bas2), (off_x2, off_y2) = poppy.font.getsize(text1)
# get boundary of this text
textsize1 = cv2.getTextSize(text1, font, 2.2, 2)[0]
textsize2 = cv2.getTextSize(text2, font, 2.2, 2)[0]
# get coords based on boundary
textX1 = int(width_s/2 - (wid1/ 2))
textX2 = int(width_s/2 - (wid2 / 2))
textY1 = int(0)
textY2 = int((bas1))
#textX1 = int(width_s/2 - (textsize1[0] / 2))
#textX2 = int(width_s/2 - (textsize2[0] / 2))
#textY1 = int(100 + (textsize1[1] / 2))
#textY2 = int(100 + (textsize2[1]+textsize1[1]))
# add text centered on image
if __name__ == "__main__":
    # cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    
    while(True):
        frame = picam2.capture_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.startWindowThread()
        try:
            if True:
                locs_and_ids = []
                image = frame.copy()
                corners, ids, rejectedCandidates = detector.detectMarkers(image)
                if len(corners) > 0:
                    # flatten the ArUco IDs list
                    ids = ids.flatten()
                    # loop over the detected ArUCo corners
                    for (markerCorner, markerID) in zip(corners, ids):
                        # extract the marker corners (which are always returned in
                        # top-left, top-right, bottom-right, and bottom-left order)
                        corners = markerCorner.reshape((4, 2))
                        (topLeft, topRight, bottomRight, bottomLeft) = corners
                        # convert each of the (x, y)-coordinate pairs to integers
                        topRight = (int(topRight[0]), int(topRight[1]))
                        bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                        bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                        topLeft = (int(topLeft[0]), int(topLeft[1]))
                        cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
                        cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
                        cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
                        cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
                        # compute and draw the center (x, y)-coordinates of the ArUco
                        # marker
                        cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                        cY = int((topLeft[1] + bottomRight[1]) / 2.0)
                        cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
                        # draw the ArUco marker ID on the image
                        cv2.putText(image, str(markerID), (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
                        locs_and_ids.append((cX, markerID, cY))
                # cv2.imshow('frame', image)
                
                img = np.zeros((height_s, width_s, 3), dtype = np.uint8)
                
                cv2.rectangle(img, (int(width_s/13), height_s-happy), (int(width_s/13+width_s/13), height_s), (0,255,255), -1)
                cv2.rectangle(img, (int(3*width_s/13), height_s-fear), (int(3*width_s/13+width_s/13), height_s), (255,0,255), -1)
                cv2.rectangle(img, (int(5*width_s/13), height_s-disgust), (int(5*width_s/13+width_s/13), height_s), (0,255,0), -1)
                cv2.rectangle(img, (int(7*width_s/13), height_s-sad), (int(7*width_s/13+width_s/13), height_s), (255,0,0), -1)
                cv2.rectangle(img, (int(9*width_s/13), height_s-surprise), (int(9*width_s/13+width_s/13), height_s), (255,255,0), -1)
                cv2.rectangle(img, (int(11*width_s/13), height_s-anger), (int(11*width_s/13+width_s/13), height_s), (0,0,255), -1)
                
                img[height_s-happy-happy_face.shape[0]:height_s-happy, int(width_s/13):int(width_s/13)+happy_face.shape[0]]=happy_face
                img[height_s-fear-fear_face.shape[0]:height_s-fear, int(3*width_s/13):int(3*width_s/13)+happy_face.shape[0]]=fear_face
                img[height_s-disgust-disgust_face.shape[0]:height_s-disgust, int(5*width_s/13):int(5*width_s/13)+happy_face.shape[0]]=disgust_face
                img[height_s-sad-sad_face.shape[0]:height_s-sad, int(7*width_s/13):int(7*width_s/13)+happy_face.shape[0]]=sad_face
                img[height_s-surprise-surprise_face.shape[0]:height_s-surprise, int(9*width_s/13):int(9*width_s/13)+happy_face.shape[0]]=surprise_face
                img[height_s-anger-anger_face.shape[0]:height_s-anger, int(11*width_s/13):int(11*width_s/13)+happy_face.shape[0]]=anger_face
                cov_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                pil_img = Image.fromarray(cov_img)
                draw = ImageDraw.Draw(pil_img)
                draw.text((textX1, textY1 ), text1, font = poppy)
                draw.text((textX2, textY2 ), text2, font = poppy)
                cv2_im_process = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
                # cv2.putText(img, text1, (textX1, textY1 ), font, 1, (255, 255, 255), 2)
                # cv2.putText(img, text2, (textX2, textY2 ), font, 1, (255, 255, 255), 2)
                cv2.imshow('image', cv2_im_process)
                
                if int(str(markerID))>=1 and int(str(markerID))<=24:
                    # print(int(str(markerID)))
                    counter = 0
                    happy_perc = kids[int(str(markerID))-1][0]
                    fear_perc = kids[int(str(markerID))-1][1]
                    disgust_perc = kids[int(str(markerID))-1][2]
                    sad_perc = kids[int(str(markerID))-1][3]
                    surprise_perc = kids[int(str(markerID))-1][4]
                    anger_perc = kids[int(str(markerID))-1][5]
                    markerID = 0
                    # print(happy_perc)
                happy_goal = int(happy_perc*the_diff)
                fear_goal = int(fear_perc*the_diff)
                disgust_goal = int(disgust_perc*the_diff)
                sad_goal = int(sad_perc*the_diff)
                surprise_goal = int(surprise_perc*the_diff)
                anger_goal = int(anger_perc*the_diff)
                if counter >= 100:
                    happy_goal = base
                    fear_goal = base
                    disgust_goal = base
                    sad_goal = base
                    surprise_goal = base
                    anger_goal = base
                    if happy>happy_goal:
                        happy-=int((happy-happy_goal)/20)
                    if fear>fear_goal:
                        fear-=int((fear-fear_goal)/20)
                    if disgust>disgust_goal:
                        disgust-=int((disgust-disgust_goal)/20)
                    if sad>sad_goal:
                        sad-=int((sad-sad_goal)/20)
                    if surprise>surprise_goal:
                        surprise-=int((surprise-surprise_goal)/20)
                    if anger>anger_goal:
                        anger-=int((anger-anger_goal)/20)
                else:
                    if happy<=happy_goal:
                        happy+=int((happy_goal-happy)/20)
                    else:
                        happy-=int((happy-happy_goal)/20)
                    if fear<=fear_goal:
                        fear+=int((fear_goal-fear)/20)
                    else:
                        fear-=int((fear-fear_goal)/20)
                    if disgust<=disgust_goal:
                        disgust+=int((disgust_goal-disgust)/20)
                    else:
                        disgust-=int((disgust-disgust_goal)/20)
                    if sad<=sad_goal:
                        sad+=int((sad_goal-sad)/20)
                    else:
                        sad-=int((sad-sad_goal)/20)
                    if surprise<=surprise_goal:
                        surprise+=int((surprise_goal-surprise)/20)
                    else:
                        surprise-=int((surprise-surprise_goal)/20)
                    if anger<=anger_goal:
                        anger+=int((anger_goal-anger)/20)
                    else:
                        anger-=int((anger-anger_goal)/20)
                    counter +=1
                    
                pressedKey = cv2.waitKey(1) & 0xFF
                if pressedKey == ord('q'):
                    break
            else:
                break
        except Exception as error:
            print(error)
            break
    cv2.destroyAllWindows()
    for i in range(5):
        cv2.waitKey(1)
    # cap.release()
