import cv2

def findEmotion():
    pass


if __name__ == "__main__":  # test
    vc = cv2.VideoCapture(0)
    rval, frame = vc.read()

    cv2.namedWindow("test")
    cv2.imshow("test", frame)
    cv2.waitKey(0)

    vc.release()
    cv2.destroyAllWindows()
