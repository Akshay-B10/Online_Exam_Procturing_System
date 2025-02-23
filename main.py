import cv2
# import imutils
import time
import winsound
from facial_detections import detectFace
# from blink_detection import isBlinking
from mouth_tracking import mouthTrack
from object_detection import detectObject
from eye_tracker import gazeDetection
from head_pose_estimation import head_pose_detection
from audio_detection import audio_detection
from datetime import datetime

global start
start = False
global data_record
data_record = []
global running
running = True


#For Beeping
frequency = 2500
duration = 1000

#Face Count If-else conditions
def faceCount_detection(faceCount):
    if faceCount > 1:
        time.sleep(3)
        remark = "Multiple faces has been detected."
        winsound.Beep(frequency, duration)
    elif faceCount == 0:
        remark = "No face has been detected."
        time.sleep(3)
        winsound.Beep(frequency, duration)
    else:
        remark = "Face detecting properly."
    return remark


#Main function 
def proctoringAlgo():
    global running
    global start

    running = True
    blinkCount = 0
    # audio_detection()
    # return
    #OpenCV videocapture for the webcam
    cam = cv2.VideoCapture(0)

    #If camera is already opened
    if (cam.isOpened() == False):
        cam.open()

    while running:
        ret, frame = cam.read()
        # frame = imutils.resize(frame, width=450)
        frame_copy = frame.copy()

        record = []

        #Reading the current time
        current_time = datetime.now().strftime("%H:%M:%S.%f")
        print("Current time is:", current_time)
        record.append(current_time)

        #Convert the frame to JPEG format
        _, buffer = cv2.imencode('.jpg', frame_copy)
        frame_copy = buffer.tobytes()
    
        yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame_copy + b'\r\n')

        #Returns the face count and will detect the face.
        if not start:
            continue
        faceCount, faces = detectFace(frame)
        print(faceCount_detection(faceCount))
        record.append(faceCount_detection(faceCount))
        # print(faceCount)

        if faceCount == 1:

            #Blink Detection
            # blinkStatus = isBlinking(faces, frame)
            # print(blinkStatus[2])

            # if blinkStatus[2] == "Blink":
            #     blinkCount += 1
            #     record.append(blinkStatus[2] + " count: " + str(blinkCount))
            # else:
            #     record.append(blinkStatus[2])


            # Gaze Detection
            # eyeStatus = (gazeDetection(faces, frame))
            # print(eyeStatus)
            # record.append(eyeStatus)

            # Mouth Position Detection
            print(mouthTrack(faces, frame))
            mouthStatus = mouthTrack(faces, frame)
            record.append(mouthStatus)
            # mouthTrack(faces, frame)

            # Object detection using YOLO
            objectName = detectObject(frame)
            print(objectName)
            record.append(objectName)

            # audio_detection()

            if len(objectName) > 1 or mouthStatus == 'Mouth Open':
                time.sleep(3)
                winsound.Beep(frequency, duration)
                continue

            # # Head Pose estimation
            # print(head_pose_detection(faces, frame))
            # record.append(head_pose_detection(faces, frame))

        
        else:
            data_record.append(record)
            continue

        data_record.append(record)


        # eyeStatus = gazeDetection(faces, frame)
        # print(eyeStatus)
        # print(objectName) 

    print("Destroying camera windows")
    cam.release()
    cv2.destroyAllWindows()

def startQuiz():
    global start
    start = True




def main_app():
    global running
    global start
    running = False
    start = False
    # print(data_record)
    # Convert the list to a string with each element on a new line
    activityVal = "\n".join(map(str, data_record))
    # print(activityVal)

    with open('activity.txt', 'w') as file:
        file.write(str(activityVal))


# print("Calling procturing algorithm")
# for _ in proctoringAlgo():  # This will start execution
#     pass