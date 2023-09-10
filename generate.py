import json
import os
from PIL import Image
from traits_files import face_files,eyes_files,ears_files,hair_files,mouth_files,nose_files,extras_files

with open('image_data.json','r') as file:
    get_image_data = json.load(file)

os.mkdir(f'./images')

for image in get_image_data:
    img1 = Image.open(f'./scripts/face_parts/face/{face_files[image["Face"]]}.png').convert("RGBA")
    img2 = Image.open(f'./scripts/face_parts/ears/{ears_files[image["Ears"]]}.png').convert("RGBA")
    img3 = Image.open(f'./scripts/face_parts/eyes/{eyes_files[image["Eyes"]]}.png').convert("RGBA")
    img4 = Image.open(f'./scripts/face_parts/mouth/{mouth_files[image["Mouth"]]}.png').convert("RGBA")
    img5 = Image.open(f'./scripts/face_parts/nose/{nose_files[image["Nose"]]}.png').convert("RGBA")
    img6 = Image.open(f'./scripts/face_parts/hair/{hair_files[image["Hairs"]]}.png').convert("RGBA")
    img7 = Image.open(f'./scripts/face_parts/extras/{extras_files[image["Extras"]]}.png').convert("RGBA")

    # Creating composites
    com1 = Image.alpha_composite(img1,img3)
    com2 = Image.alpha_composite(com1,img2)
    com3 = Image.alpha_composite(com2,img6)
    com4 = Image.alpha_composite(com3,img4)
    com5 = Image.alpha_composite(com4,img5)
    com6 = Image.alpha_composite(com5,img7)

    # Converting to RGB
    # rgb_im = com6.convert('RGB')
    file_name = str(image["tokenId"]) + ".png"
    # rgb_im.save("./images/" + file_name)
    com6.save("./images/" + file_name)