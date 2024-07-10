# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 

str = input("Enter the string you want to convert")
 
QR_CODE = pyqrcode.create(str) 
 
QR_CODE.png('QR_IMG.png', scale = 8) 