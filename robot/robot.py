# This is the code from Tim's laptop, the Mac Book code is more up-to-date 
import cv2
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image
import os
import pandas as pd
os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"
mpl.rcParams['figure.figsize'] = (10,10)
mpl.rcParams['axes.grid'] = False
import IPython.display
import time
from IPython.core.display import HTML
import io
from datetime import datetime
from BirdBrain import Finch
import numpy as np
import time
def robot_stay_connected():
    try: 
        myBird = Finch('A')
        myBird.setBeak(np.random.randint(0,100), np.random.randint(0,100), np.random.randint(0,100))
        myBird.stopAll()
        return
    except:
        print('Not connected to hummingbird')
        return
    
def robot_directions(ids_unordered=[]):
    if len(ids_unordered) == 0:
        print('No QR Codes')
    else:
        x = []
        ids = []
        y = []
        for i in ids_unordered:
            x.append(i[0])
            ids.append(i[1])
            y.append(i[2])
        df = pd.DataFrame({'col1': x,'col2': ids, 'col3':y})
        df2 = df.sort_values(by=['col1'], ascending=[False])
        code=[]
        for i in df2['col2']:
            if i==1:
                code.append('R')
            elif i==2:
                code.append('L')
            elif i==3:
                code.append('F')
            elif i==4:
                code.append('F')
                code.append('F')
            elif i==5:
                code.append('L')
                code.append('L')
            elif i==6:
                code.append('F')
                code.append('F')
            elif i==7:
                code.append('L')
            elif i==8:
                code.append('R')
            elif i==9:
                code.append('F')
            elif i==10:
                code.append('B')
        try: 
            myBird = Finch('A')
            for i in code:
                if i=='F': 
                    myBird.setMove(i,17.5,80)
                elif i=='R':
                    myBird.setTurn(i,90,80)
                elif i=='L':
                    myBird.setTurn(i,90,80)
                elif i=='B':
                    myBird.setMove(i,17.5,80)
            myBird.stopAll()
            return
        except:
            print(code)
            print('Not connected to hummingbird')
            return
        
if __name__ == "__main__":
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
    parameters =  cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)
    cap = cv2.VideoCapture(1, cv2.CAP_MSMF)
    # cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    x = 0
    while(cap.isOpened()):
        now =  int(datetime.now().strftime("%H:%M:%S")[3:5])
        ret, frame = cap.read()
        cv2.startWindowThread()
        try:
            if ret == True:
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
                cv2.imshow('frame', image)
                pressedKey = cv2.waitKey(1) & 0xFF
                if pressedKey == ord('s'):
                    print('fun function')
                    robot_directions(locs_and_ids)
                elif pressedKey == ord('q'):
                    break
                else:
                    if x != now:
                        robot_stay_connected()
                        x=now
            else:
                break
        except:
            break
    cv2.destroyAllWindows()
    for i in range(5):
        cv2.waitKey(1)
    cap.release()            
