# coding: utf-8
from __future__ import print_function

import numpy as np
import cv2

# This should help with the assignment:
# * Indexing numpy arrays http://scipy-cookbook.readthedocs.io/items/Indexing.html


def parseArguments():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', help='Input video file name.')
    parser.add_argument('-i', '--image', help='Input image file name.')
    args = parser.parse_args()
    return args


def image(imageFileName):
    # read image
    img = cv2.imread("church.JPG")
    if img is None:
        print("Error: Unable to read image file", imageFileName)
        exit(-1)

    # print image width, height, and channel count
    print("Image dimensions: " + str(img.shape)) ## FILL

    # Resize to width 400 and height 500 with bicubic interpolation.
    img = cv2.resize(img, (400,500), fx=400, fy=500, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("church_resized.JPG", img)

    # Print mean image color and standard deviation of each color channel
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]

    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    mean_values = list()
    mean_values.append(b_mean)
    mean_values.append(g_mean)
    mean_values.append(r_mean)

    b_std = np.std(b)
    g_std = np.std(g)
    r_std = np.std(r)

    std_values = list()
    std_values.append(b_std)
    std_values.append(g_std)
    std_values.append(r_std)

    print('Image mean and standard deviation' + str(mean_values) + ", " + str(std_values)) ## FILL

    # Fill horizontal rectangle with color 128.
    # Position x1=50,y1=120 and size width=200, height=50
    ## FILL
    img_backup = img.copy()
    img_backup2 = img.copy()

    img = cv2.rectangle(img, (50,120), (250,170), 128, 2)

    # write result to file
    cv2.imwrite('rectangle.png', img)

    # Fill every third column in the top half of the image black.
    # The first column sould be black.
    # The rectangle should not be visible.
    ## FILL
    cv2.imwrite('backup.png', img_backup)
    top_half = img_backup.shape[0] / 2

    for i in range(img_backup.shape[0]):
        for j in range(img_backup.shape[1]):
            if (j % 3 == 0 and i < top_half):
                img_backup[i,j] = 0


    # write result to file
    img = img_backup
    cv2.imwrite('striped.png', img)

    # Set all pixels with any a value of any collor channel lower than 100 to black (0,0,0).
    ## FILL
    for i in range(img_backup2.shape[0]):
        for j in range(img_backup2.shape[1]):
            condition = np.any(img_backup2[i,j] < 100)
            if (condition == True):
                img_backup2[i,j] = 0


    #write result to file
    img = img_backup2
    cv2.imwrite('clip.png', img)


def video(videoFileName):
    # open video file and get basic information
    videoCapture = cv2.VideoCapture(videoFileName)
    frameRate = videoCapture.get(cv2.CAP_PROP_FPS)
    frame_width = int (videoCapture.get(3))
    frame_height = int (videoCapture.get(4))
    print(frameRate)
    print(frame_width)
    print(frame_height)
    if not videoCapture.isOpened():
        print("Error: Unable to open video file for reading", videoFileName)
        exit(-1)

    # open video file for writing
    videoWriter  = cv2.VideoWriter(
    'videoOut.avi', cv2.VideoWriter_fourcc('M','J','P','G'),
        frameRate, (frame_width, frame_height))
    if not videoWriter.isOpened():
        print("Error: Unable to open video file for writing", videoFileName)
        exit(-1)

    while videoCapture.isOpened():
        ret, frame = videoCapture.read()
        if not ret:
            break;

        # Flip image upside down.
        ## FILL
        frame = cv2.rotate(frame, cv2.ROTATE_180)

        # Add white noise (additive noise with normal distribution).
        # Standard deviation should be 5.
        # use np.random
        ## FILL
        gauss = np.random.normal(0,5,frame.size)
        gauss = gauss.reshape(frame.shape[0],frame.shape[1],frame.shape[2]).astype('uint8')
        # Add the Gaussian noise to the image
        frame = cv2.add(frame,gauss)

        # Add gamma correction.
        # y = x^1.2 -- the image to the power of 1.2
        ## FILL

        corrected_pixels = [((i / 255) ** (1/1.2)) * 255 for i in range(256)]
        corrected_pixels = np.array(corrected_pixels, np.uint8)

        frame = cv2.LUT(frame, corrected_pixels)

        # Dim blue color to half intensity.
        ## FILL
        b = frame[:,:,0]
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                pixel_value = frame[i,j]
                frame[i,j][2] = pixel_value[2] / 2


        # Invert colors.
        ## FILL
        frame = cv2.bitwise_not(frame)

        # Display the processed frame.
        cv2.imshow("Output", frame)
        # Write the resulting frame to the video file.
        videoWriter.write(frame)

        # End the processing on pressing Escape.
        ## FILL
        cv2.waitKey(10)

    cv2.destroyAllWindows()
    videoCapture.release()
    videoWriter.release()


def main():
    args = parseArguments()
    np.random.seed(1)
    image(args.image)
    video(args.video)

if __name__ == "__main__":
    main()
