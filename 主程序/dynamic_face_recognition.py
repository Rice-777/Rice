import cv2
import face_recognition


class FaceRecognition:
    def __init__(self):
        pass

    def face_recognition_fun(self):
        me = cv2.imread("Rice_1.jpg")
        me_face_encoding = face_recognition.face_encodings(me)[0]
        me_face_list = [me_face_encoding]
        target_name_list = ['Right']

        vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            ret, img = vc.read()
            if not ret:
                return False
            else:
                locations = face_recognition.face_locations(img)
                face_encodings = face_recognition.face_encodings(img, locations)
                for (top, right, bottom, left), face_encoding in zip(locations, face_encodings):
                    matchs = face_recognition.compare_faces(me_face_list, face_encoding, tolerance=0.5)
                    target_names = 'unknown'
                    for match, target_name in zip(matchs, target_name_list):
                        if match:
                            target_names = target_name
                            cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 3)
                            cv2.putText(img, target_names, (left, top - 20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2,
                                        (255, 0, 0), 2)
                            cv2.imshow('face_recognition', img)
                            key = cv2.waitKey(1) & 0xFF
                            if key == ord('e'):
                                vc.release()
                                cv2.destroyAllWindows()
                                return True
                        else:
                            cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 3)
                            cv2.putText(img, target_names, (left, top - 20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2,
                                        (255, 0, 0), 2)
                            cv2.imshow('face_recognition', img)
                            key = cv2.waitKey(1) & 0xFF
                            if key == ord('e'):
                                vc.release()
                                cv2.destroyAllWindows()
                                return False


if __name__ == '__main__':
    dfr = FaceRecognition()
    print(dfr.face_recognition_fun())
