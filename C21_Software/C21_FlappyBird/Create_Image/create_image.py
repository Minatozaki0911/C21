# vim: set ai et ts=4 sw=4:

import cv2

img = cv2.imread("images.png")
img = cv2.resize(img,(15,15))
# img = cv2.flip(img,1)
cv2.imshow('BGR Image',img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB Image',img_rgb )
# cv2.waitKey(0)
f= open("bird.h","w+")
f.write("const uint16_t bird[][15] = {")

for y in range(0, img.shape[1]):
    s = "{"
    for x in range(0, img.shape[0]):
        (b, g, r) = img[x,y,:]
        color565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | ((b & 0xF8) >> 3)
        # for right endiness, so ST7735_DrawImage would work
        color565 = ((color565 & 0xFF00) >> 8) | ((color565 & 0xFF) << 8)
        s += "0x{:04X},".format(color565)
    s += "},"
    f.write(s)

f.write("};")
f.close()