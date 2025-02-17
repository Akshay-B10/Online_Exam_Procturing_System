import dlib
import cv2
from math import hypot

predictorModel = 'shape_predictor_model/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictorModel)

def calcDistance(pointA, pointB):

    #calc the Eucledian distance between point A and B
    dist = hypot((pointA[0]-pointB[0]), (pointA[1]-pointB[1]))
    return dist


def mouthTrack(faces, frame):

    for face in faces:

        facialLandmarks = predictor(frame, face)

         # Outer lip distance (51, 57)
        outerDist = calcDistance(
            (facialLandmarks.part(51).x, facialLandmarks.part(51).y),
            (facialLandmarks.part(57).x, facialLandmarks.part(57).y)
        )

        # Inner lip distance (62, 66)
        innerDist = calcDistance(
            (facialLandmarks.part(62).x, facialLandmarks.part(62).y),
            (facialLandmarks.part(66).x, facialLandmarks.part(66).y)
        )

        # #outer lip top point
        # outerTopX = facialLandmarks.part(51).x
        # outerTopY = facialLandmarks.part(51).y

        # #outer lip bottom point
        # outerBottomX = facialLandmarks.part(57).x
        # outerBottomY = facialLandmarks.part(57).y

        # dist = calcDistance((outerTopX, outerTopY), (outerBottomX, outerBottomY))

        # Normalize by face height
        faceHeight = face.bottom() - face.top()
        outerRatio = outerDist / faceHeight
        innerRatio = innerDist / faceHeight

        # Adaptive threshold based on face height
        mouth_open = outerRatio > 0.15 or innerRatio > 0.08

        status = "Mouth Open" if mouth_open else "Mouth Closed"
        cv2.putText(frame, status, (50, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        return status

        # if (dist > 23):
        #     cv2.putText(frame, "Mouth Open", (50,80), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        #     return "Mouth Open"
        # else:
        #     return "Mouth Close"
        # return -1

        # cv2.putText(frame, "Threshold - "+ str(30), (50,400), cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),5)
        