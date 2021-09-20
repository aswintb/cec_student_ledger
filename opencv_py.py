import cv2
import csv

from pyzbar import pyzbar
from datetime import datetime as dt



now = dt.now()

def row_append(barcode):    
    with open('test.csv', 'a+', newline='') as fd:
        
        datenow= now.strftime("%d-%b-%y")
        timenow = now.strftime("%H:%M:%S")
        csvwriter=csv.writer(fd)   
        
        csvwriter.writerow([datenow, timenow, barcode])

'''
barcode_no=input("Enter some crap ")            
row_append(barcode_no)  
'''    
   



def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        print(barcode_text)
        row_append(barcode_text) 
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame


camera = cv2.VideoCapture(0)
ret, frame = camera.read()
while ret:
    ret, frame = camera.read()
    frame = read_barcodes(frame)
    cv2.imshow('Barcode reader', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()

