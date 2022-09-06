def findAngle(hh, mm):
    hh = hh % 12 
    h = (hh * 360) / 12 + (mm * 360) / (12 * 60)  
    m = (mm * 360) / (60) 
    angle = abs(h - m) 
    if angle > 180:
        angle = 360 - angle 
    return angle 
if __name__ == '__main__': 
    time = input()
    hh, mm = [int(i) for i in time.split(":")]
    print(findAngle(hh, mm))