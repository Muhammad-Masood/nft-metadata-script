import random
import json
from traits import traits, name, description, image
import os


# returns unique attribtes for single nft
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


# total supply of the collection
totalImages = 200

os.mkdir(f"./metadata/")


def generate_metadata():
    prev_attributes = []
    all_images_metadata = []
    for i in range(totalImages):
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

    return all_images_metadata


metadata = []
metadata = generate_metadata()
with open(f"./metadata/all_metadata.json", "w") as json_file:
    json.dump(metadata, json_file, indent=4)

