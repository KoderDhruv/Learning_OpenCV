import cv2 as cv

# #reading an image
# img=cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)


# reading a video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    # isTrue is var that returns true if the file is read
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
