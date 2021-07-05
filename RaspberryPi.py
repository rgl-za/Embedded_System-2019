import cv2
import sys
import math
import video
import cv2 as cv
import numpy as np
import serial
import time
import math

 
ser = serial.Serial('/dev/ttyUSB0',115200) #�Ƶ��̳�� �ø��� ����

if __name__ == '__main__':

    print(__doc__)

    try:
        fn = sys.argv[1]

    except IndexError:
        fn = 0

    def nothing(*arg):
        pass

    cap = video.create_capture(fn)


    i = 0
    counter = 0
    width = 0
    height = 0
    color = 0 

#���� ũ�� �޾ƿ��� �Լ�
    def check_img_info():
        while(True):
            ret, img = cap.read()

            if ret:
                x = img.shape[1] #������ ���� �ʺ� ũ��
                y = img.shape[0] #������ ���� ���� ũ��
                break

        return x, y

#���󿡼� RGB�� �޾Ƽ� HSL �� ��ȯ�� ���� ��� ������ �� ��ȯ���ִ� �Լ�
    def check_color_pattern(src1):
        hls = cv2.cvtColor(src1, cv2.COLOR_BGR2HLS) # BGR color -> HSL �� ��ȯ
        counter = 1
        sum_hue = 0

        # ��� ��ġ ����   
        for i in range(50, width-50, 20):
            for j in range(50, height-50, 20):
                sum_hue = sum_hue + (hls[j, i, 0]*2)
                counter = counter + 1
        hue = sum_hue/counter #���� �� ����
        print('Average Hue: ', hue)

        if ( 0 <= hue <= 30 ) or ( 280 <= hue <= 360): # RED
            print("R")
            str='R'
            ser.write(bytes(str.encode()))
            time.sleep(5)
            return 0

        elif( 90 <= hue <= 150): #GREEN
            print("G")
            str='G'
            ser.write(bytes(str.encode()))
            time.sleep(0.1)
            return 1

        elif( 40 <= hue <= 80): #YELLOW
            print("Y")
            str='Y'
            ser.write(bytes(str.encode()))
            time.sleep(0.1)
            return 2

        else:
            print(" Can't check color")
            time.sleep(1)
            return 3

    width, height = check_img_info()

    while (True):
        ret, src = cap.read() #�ǽð� ���� �о����
        src1 = np.copy(src)
        src = cv2.resize(src, (640, 380)) #������ ������ â ũ�� ����   

        if ret:
            cv2.imshow('Video', src1)
            counter = counter + 1
            hls = cv2.cvtColor(src1, cv2.COLOR_BGR2HLS)
            color = check_color_pattern(src1) #�Լ��� ��ȯ ���� ����

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()