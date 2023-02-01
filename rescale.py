import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height, brightness):
    # Works only on live video
    capture.set(3, width)
    capture.set(4, height)
    capture.set(10, brightness)

    '''
  0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
  1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
  2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
  3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
  4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
  5. CV_CAP_PROP_FPS Frame rate.
  6. CV_CAP_PROP_FOURCC 4-character code of codec.
  7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
  8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
  9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
  10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
  11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
  12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
  13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
  14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
  15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
  16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
  17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
  18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
  '''


# reading a video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    # isTrue is var that returns true if the file is read
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# #reading an image
# img=cv.imread('Photos/cat_large.jpg')
# img_rescaled=rescaleFrame(img)
# cv.imshow('Cat_resized', img_rescaled)
# cv.imshow('Cat', img)
# cv.waitKey(0)
