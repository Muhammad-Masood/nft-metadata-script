import json
import os
from PIL import Image
import random
from traits import traits, name, description, image, totalNfts
from traits_files import (
    face_files,
    eyes_files,
    ears_files,
    hair_files,
    mouth_files,
    nose_files,
    extras_files,
)


def create_unique_attribute(existing_attributes):
    attributes = []
    for i, trait_obj in enumerate(traits):
        key, value = list(trait_obj.items())[0]
        w_key, w_value = list(trait_obj.items())[1]
        attributes.append(
            {"trait_type": key, "value": random.choices(value, w_value)[0]}
        )
    if attributes not in existing_attributes:
        return attributes
    else:
        print("Creating new attribute list due to duplication of traits...")
        return create_unique_attribute(existing_attributes)


def generate_metadata():
    prev_attributes = []
    all_images_metadata = []
    os.mkdir(f"./metadata/")
    os.mkdir(f"./images")
    for i in range(totalNfts):
        new_image = {}
        new_image["name"] = name + str(i)
        new_image["description"] = description
        new_image["image"] = image
        new_image["tokenId"] = i
        new_image["attributes"] = create_unique_attribute(prev_attributes)
        prev_attributes.append(new_image["attributes"])
        all_images_metadata.append(new_image)

        filename = str(i) + ".json"
        with open(f"./metadata/{filename}", "w") as json_file:
            json.dump(new_image, json_file, indent=4)

        ##################
        # generating image
        ##################

        ###############
        # Replace Paths
        ###############

        image_traits = {}
        for trait in new_image["attributes"]:
            image_traits[trait["trait_type"]] = trait["value"]  # Face : White
        img1 = Image.open(
            f'./components/face/{face_files[image_traits["Face"]]}.png'
        ).convert("RGBA")
        img2 = Image.open(
            f'./components/ears/{ears_files[image_traits["Ears"]]}.png'
        ).convert("RGBA")
        img3 = Image.open(
            f'./components/eyes/{eyes_files[image_traits["Eyes"]]}.png'
        ).convert("RGBA")
        img4 = Image.open(
            f'./components/mouth/{mouth_files[image_traits["Mouth"]]}.png'
        ).convert("RGBA")
        img5 = Image.open(
            f'./components/nose/{nose_files[image_traits["Nose"]]}.png'
        ).convert("RGBA")
        img6 = Image.open(
            f'./components/hair/{hair_files[image_traits["Hair"]]}.png'
        ).convert("RGBA")
        img7 = Image.open(
            f'./components/extras/{extras_files[image_traits["Extras"]]}.png'
        ).convert("RGBA")

        # Creating composites
        com1 = Image.alpha_composite(img1, img3)
        com2 = Image.alpha_composite(com1, img2)
        com3 = Image.alpha_composite(com2, img6)
        com4 = Image.alpha_composite(com3, img4)
        com5 = Image.alpha_composite(com4, img5)
        com6 = Image.alpha_composite(com5, img7)

        # Converting to RGB
        # rgb_im = com6.convert('RGB')

        img_name = str(new_image["tokenId"])  # 1.png, 2.png, 3.png, etc

        file_name = img_name + ".png"
        # rgb_im.save("./images/" + file_name)
        com6.save("./images/" + file_name)

    return all_images_metadata


metadata = []
metadata = generate_metadata()
with open(f"./metadata/all_metadata.json", "w") as json_file:
    json.dump(metadata, json_file, indent=4)
