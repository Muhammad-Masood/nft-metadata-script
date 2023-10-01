# Define traits for the nft

name = "Punks #"  # + the tokenId -> Punks #121

description = "A test nft collection by Muhammad Masood"

image = "ipfs://"  # + cid -> ipfs://QmYz6pVx4xvP2N9gjv6Zz4nY9nqA2V2zZ1s5r4qTjZz9a.png

traits = [
    {"Face": ["White", "Black"], "face_weight": [60, 40]},
    {
        "Ears": ["No Earring", "Left Earring", "Right Earring", "Two Earrings"],
        "ears_weight": [25, 35, 39, 1],
    },
    {
        "Eyes": ["Regular", "Small", "Rayban", "Hipster", "Focused"],
        "eyes_weight": [30, 20, 20, 29, 1],
    },
    {
        "Hair": [
            "Up Hair",
            "Down Hair",
            "Mohawk",
            "Red Mohawk",
            "Orange Hair",
            "Bubble Hair",
            "Emo Hair",
            "Thin Hair",
            "Bald",
            "Blonde Hair",
            "Caret Hair",
            "Pony Tails",
        ],
        "hair_weights": [10, 10, 10, 10, 10, 10, 10, 10, 10, 7, 1, 2],
    },
    {
        "Mouth": [
            "Black Lipstick",
            "Red Lipstick",
            "Big Smile",
            "Smile",
            "Teeth Smile",
            "Purple Lipstick",
        ],
        "mouth_weights": [10, 10, 50, 10, 15, 5],
    },
    {"Nose": ["Nose", "Nose Ring"], "nose_weights": [90, 10]},
    {
        "Extras": [
            "No Beard",
            "Much Beard",
            "Half Beard",
            "Full Beard",
            "Cigarette",
            "Cigar",
        ],
        "extras_weights": [70, 15, 5, 5, 4, 1],
    },
]
