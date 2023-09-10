import random
import json

face = ["White","Black"]
face_weight = [60,40] # for rarity

ears = ["No Earring","Left Earring","Right Earring","Two Earrings"]
ears_weight = [25,35,39,1]

eyes = ["Regular","Small","Rayban","Hipster","Focused"]
eyes_weight = [30,20,20,29,1]

hair = ['Up Hair', 'Down Hair', 'Mohawk', 'Red Mohawk', 'Orange Hair', 'Bubble Hair', 'Emo Hair',
 'Thin Hair',
 'Bald',
 'Blonde Hair',
 'Caret Hair',
 'Pony Tails']
hair_weights = [10 , 10 , 10 , 10 ,10, 10, 10 ,10 ,10, 7 , 1 , 2]

mouth = ['Black Lipstick', 'Red Lipstick', 'Big Smile', 'Smile', 'Teeth Smile', 'Purple Lipstick']
mouth_weights = [10, 10,50, 10,15, 5]

nose = ['Nose', 'Nose Ring']
nose_weights = [90, 10]

extras = ['No Beard','Much Beard','Half Beard','Full Beard','Cigarette','Cigar']
extras_weights = [70,15,5,5,4,1]

totalImages = 200

all_images = []

def create_new_image():
    new_image = {}

    new_image["Face"] = random.choices(face,face_weight)[0]
    new_image["Ears"] = random.choices(ears,ears_weight)[0]
    new_image["Eyes"] = random.choices(eyes,eyes_weight)[0]
    new_image["Hairs"] = random.choices(hair,hair_weights)[0]
    new_image["Mouth"] = random.choices(mouth,mouth_weights)[0]
    new_image["Nose"] = random.choices(nose,nose_weights)[0]
    new_image["Extras"] = random.choices(extras,extras_weights)[0]
    
    if new_image not in all_images:
        return new_image
    else:
        return create_new_image()

for i in range(totalImages):
    all_images.append(create_new_image())


none_images = 0
for i in all_images:
    if i is None: none_images+=1

print(all_images,all_images.__len__(),"none images = ",none_images)



# validate that all images are unique

def are_images_unique(allImages):
    seen = list()
    for i in allImages:
        if(i in seen) : 
            return False
        seen.append(i)
    return True

# adding token Id

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i+1

print(all_images,all_images.__len__())
print ("Are all images unique?",are_images_unique(all_images))

if(are_images_unique(all_images)):
    with open('image_data.json','w') as file:
        json.dump(all_images,file)




