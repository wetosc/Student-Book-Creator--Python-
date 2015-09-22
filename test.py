import os
from PIL import Image
from fpdf import FPDF


def editImage(imagename):
    image = Image.open(imagename).convert("L")
    size_x, size_y = image.size

    if size_y > size_x:
        image=image.rotate(90)

    paper = 230

    def x1coord(data, size):
        size_x, size_y = size
        k = []
        for i in range(size_y):
            for j in range(size_x):
                if data[size_x * i + j] > paper: break;
            k.append(j)
        return min(k)

    def y1coord(data, size):
        size_x, size_y = size
        k = []
        for i in range(size_x):
            for j in range(size_y):
                if data[size_x * j + i] > paper: break;
            k.append(j)
        return min(k)

    def x2coord(data, size):
        size_x, size_y = size
        k = []
        for i in range(size_y):
            for j in range(size_x, 0, -1):
                if data[size_x * (i) - j - 1] > 195:
                    # print i,j
                    break;
            k.append(j)
        return max(k)

    def y2coord(data, size):
        size_x, size_y = size
        k = []
        for i in range(size_x):
            for j in range(size_y - 1, 0, -1):
                if data[size_x * j + i] > paper: break;
            k.append(j)
        return max(k)

    def crop_box(image):
        size = image.size
        data = image.getdata()
        return (x1coord(data, size), y1coord(data, size), x2coord(data, size), y2coord(data, size))

    size=crop_box(image)
    if size[0]<size[0] and size[1]<size[3]:
        image = image.crop()
    return image


path = os.getcwd() + "\\temp\\"
if not os.path.exists(path):
    os.makedirs(path)

pdf = FPDF(orientation='L',format=[670,1180])
for file in os.listdir(path):
    os.remove(path+file.title())

old_path=os.getcwd()
os.chdir(path)
for file in os.listdir(old_path):
    if os.path.isfile(old_path+"\\"+file):
        if file.split(".")[1] == "jpg":
            image=editImage(old_path+"\\"+file)
            image.save(file.title())
            arr=[image.size[0],image.size[1]]
            pdf.add_page()
            pdf.image(file.title(),x=0,y=0)
pdf.output("wasea.pdf", "F")
