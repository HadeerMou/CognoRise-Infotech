from PIL import Image #pillow library to include image in the QR code
import qrcode
import qrcode.constants
import cv2

#QR code encode
qr = qrcode.QRCode(version=1, error_correction= qrcode.constants.ERROR_CORRECT_M, box_size= 10, border=2)
#add data to the QR code
qr.add_data("https://www.linkedin.com/in/hadeermouwad")
#make the QR code
qr.make(fit=True)
#create an image from the QR code
img = qr.make_image(fill_color='pink', back_color='white')
img.save('linkedinQRCode.png')
#open the image
image = Image.open('Anime.jpg')
#resize the image
image = image.resize((50,50))

#position the image in the center of QR code
img_w, img_h = img.size
image_w, image_h = image.size
pos = ((img_w - image_w) // 2 , (img_h - image_h) // 2)
#paste the imgae into the QR code
img.paste(image,pos)
#Save the QR code with image
img.save("qr_code_with_logo.png")

#Decoding QR code
detecor = cv2.QRCodeDetector()

data,points,s_qr = detecor.detectAndDecode(cv2.imread('qr_code_with_logo.png'))
print(data)
print('Points')
print(points)
print(s_qr)