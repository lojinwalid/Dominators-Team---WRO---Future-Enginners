# Single Color RGB565 Blob Tracking Example
#
# This example shows off single color RGB565 tracking using the OpenMV Cam.

import sensor, image, time, math,pyb
from pyb import Servo
from pyb import UART
uart = UART(3, 19200)
s1 = Servo(2) # P7
# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# The below thresholds track in general red/green/blue things. You may wish to tune them...
thresholds = [(14, 69, 9, 57, -2, 44), # generic_red_thresholds
              (14, 63, -33, -13, -22, 73), # generic_green_thresholds
              (56, 77, -1, 24, 11, 35), #generic_orange_thresholds
              (36, 77, -10, 20, -40, -9),#generic_blue_thresholds
              (0, 36, -26, 26, -8, 14)] # generic_BLACKthresholds
left_wall_roi=(0,30,46,81)
right_wall_roi=(114,30,46,81)
line_roi=(1,78,160,43)
h_r="hr\n"
h_l="hl\n"
fwd="fs\n"
fm = "f\n"
s_r="sr\n"
s_l="sl\n"
m_r="mr\n"
m_l="ml\n"
first_line="u"
laps=0
counter=100
count_stop=0
red_last=0
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 500)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
sensor.set_auto_exposure(False,16000)
sensor.skip_frames(time = 500)
clock = time.clock()
# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. "merge=True" merges all overlapping blobs in the image.
left_wall_area=0
right_wall_area=0
while(True):
    if laps == 12:
        count_stop+=1
        if count_stop == 50:
            uart.write("s\n")
            time.sleep(17)
    uart.write(fm)
    counter+=1
    img = sensor.snapshot()
    red_blob=img.find_blobs([thresholds[0]], pixels_threshold=250, area_threshold=350, merge=True)
    #img.draw_rectangle(left_wall_roi, color = (255, 255, 0), thickness = 2, fill = False) #left wall
   # img.draw_rectangle(right_wall_roi, color = (255, 255, 0), thickness = 2, fill = False) #right wall
    #img.draw_rectangle(line_roi, color = (255, 255, 0), thickness = 2, fill = False) #left wall
    green_blob=img.find_blobs([thresholds[1]], pixels_threshold=250, area_threshold=350, merge=True)
    right_black_blob=img.find_blobs([thresholds[4]],roi=right_wall_roi, pixels_threshold=100, area_threshold=400, merge=True)
    left_black_blob=img.find_blobs([thresholds[4]], roi=left_wall_roi ,pixels_threshold=100, area_threshold=400, merge=True)
    orange_line_blob=img.find_blobs([thresholds[2]],roi=line_roi, pixels_threshold=200, area_threshold=350, merge=True)
    blue_line_blob=img.find_blobs([thresholds[3]],roi=line_roi, pixels_threshold=200, area_threshold=350, merge=True)

    if red_blob and red_blob[0].cy() <=70:
        largest_blob=max(red_blob,key=lambda b:b.pixels())
        red_last=1
        print(largest_blob.area())
        if largest_blob.area()>2800:
            uart.write(s_l)
            uart.write("b\n")
            print("Backward")
            time.sleep(0.2)

        elif largest_blob.cx()>88:
            print("hard right")
            uart.write("g\n") #fast left
            uart.write(h_r)
        elif 26<largest_blob.cx()<88:
            uart.write(fm)
            uart.write(m_r)
            time.sleep(0.2)
            uart.write(fwd)
            time.sleep(0.1)
            print("medium right")
        else:
            uart.write(fm)
            uart.write(fwd)
            print("forward")
        img.draw_rectangle(largest_blob.rect(), color = (255, 0, 0), thickness = 2, fill = False)
        # These values depend on the blob not being circular - otherwise they will be shaky.
        img.draw_cross(largest_blob.cx(), largest_blob.cy())
    if green_blob:
        largest_blob1=max(green_blob,key=lambda b:b.pixels())
        print(largest_blob1.area())
        print(largest_blob1.cx())
        if largest_blob1.area()>2800:
            uart.write(s_r)
            uart.write("b\n")
            print("Backward")
            time.sleep(0.2)
        elif largest_blob1.cx()<65:
            uart.write("g\n")
            uart.write(h_l)
            print("hard left")
        elif 65<largest_blob1.cx()<130:
            uart.write(fm)
            uart.write(m_l)
            time.sleep(0.2)
            print("medium left")
            uart.write(fwd)
            time.sleep(0.1)
        else:
            uart.write(fm)
            uart.write(fwd)
            print("forward")
        # Note - the blob rotation is unique to 0-180 only.
        img.draw_rectangle(largest_blob1.rect(), color = (0,255, 0), thickness = 2, fill = False)
        img.draw_cross(largest_blob1.cx(), largest_blob1.cy())
    if not(green_blob or red_blob or (orange_line_blob and first_line=="o") or (blue_line_blob and first_line=="b")) :
        if right_black_blob:
            largest_right=max(right_black_blob,key=lambda b:b.pixels())
            img.draw_rectangle(largest_right.rect(), color = (255, 255, 60), thickness = 2, fill = False)
            right_wall_area=largest_right.area()
            print("right:",largest_right.area())
        else:
            right_wall_area=0
        if left_black_blob:
            largest_left=max(left_black_blob,key=lambda b:b.pixels())
            img.draw_rectangle(largest_left.rect(), color = (255, 50, 255), thickness = 2, fill = False)
            left_wall_area=largest_left.area()
            print("left:",largest_left.area())
        else:
            left_wall_area=0
        '''
        if (left_wall_area>2500 or right_wall_area>2500)  :
            uart.write(fwd)
            uart.write("b\n")
            print("Back")
            time.sleep(0.15)
            uart.write(fm)
            uart.write(h_l)
            time.sleep(0.2)
        '''
        if left_wall_area>3000:
            uart.write(m_l)
            uart.write("b\n")
            print("Back")
            time.sleep(0.4)
        elif right_wall_area>3000:
            uart.write(fm)
            uart.write(m_r)
            uart.write('b\n')
            print("Back")
            time.sleep(0.4)
        elif left_wall_area and not(right_wall_area):
            print("go right")
            uart.write(m_r)
            uart.write(fm)
        elif right_wall_area and not(left_wall_area):
            print("go left")
            uart.write(m_l)
            uart.write(fm)
        elif right_wall_area and left_wall_area :
            print("Diff R-L",right_wall_area - left_wall_area )
            if  -350< (right_wall_area) - (left_wall_area) <350 :
                print("move forward")
                uart.write(fwd)
                uart.write(fm)
            elif -350 >(right_wall_area -left_wall_area)> -800 :
                print("go right now")
                uart.write(s_r)
                uart.write(fm)
            elif 350 <(right_wall_area - left_wall_area)< 800 :
                print("go left now")
                uart.write(s_l)
                uart.write(fm)
            elif (right_wall_area - left_wall_area) >800 :
                uart.write(h_l)
                uart.write(fm)
                print("go left gamed")
            elif (right_wall_area - left_wall_area) < -800 :
                uart.write(h_r)
                uart.write(fm)
                print("go right gamed")
    if first_line == "u":
        if orange_line_blob:
            first_line = "o"
        if blue_line_blob:
            first_line = "b"
    if orange_line_blob and first_line == "o" and counter >100 :
        largest_o_line=max(orange_line_blob,key=lambda b:b.pixels())
        img.draw_rectangle(largest_o_line.rect(), color = (255, 150, 0), thickness = 2, fill = False)
        uart.write(m_r)
        uart.write(fm)
        if not(red_blob or green_blob):
            time.sleep(0.2)
        else:
            time.sleep(0.1)
        if counter > 100:
            laps+=1
            counter = 0
    if blue_line_blob and first_line == "b" and counter >100:
        largest_b_line=max(blue_line_blob,key=lambda b:b.pixels())
        img.draw_rectangle(largest_b_line.rect(), color = (0, 50, 255), thickness = 2, fill = False)
        uart.write(m_l)
        uart.write(fm)
        if not(red_blob or green_blob):
            time.sleep(0.2)
        else:
            time.sleep(0.1)
        if counter > 100:
            laps+=1
            counter = 0
    print(counter)
    print("Laps",laps)
    #uart.write(5)
    #print(clock.fps())
