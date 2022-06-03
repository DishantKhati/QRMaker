import qrcode
import cv2
def codemake():    
    img = qrcode.make(input("enter the string for qr: "))
    a=input("enter the save file name: ")+'.jpg'
    img.save(a)
def codescan():
    d = cv2.QRCodeDetector()
    a=input("enter the save file name: ")+'.jpg'
    val= d.detectAndDecode(cv2.imread(a))
    print("Decoded text is: ", val)
u=int(input("Welcome to database:\n\n\tMenu\n1-Make\n2-Scan\nEnter your choice: "))
if u==1:
    codemake()
else:
    codescan()    