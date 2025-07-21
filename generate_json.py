import os
import json
import random
import time
from PIL import Image

# Category to fruit names mapping
category_map = {
    "1": "margo, grape, plum, kiwi, pear",
    "2": "apple, orange, banana, pomegranate, strawberry",
    "3": "pineapple, fig, peach, apricot, avocado",
    "4": "summar, squash, lemon, lime, guava, raspberry",
    "5": "banana, pomegranate, orange, grape",
    "6": "guava, pear, lime, apricot",
    "7": "apple, strawberry, plum, kiwi",
    "8": "avocado, lemon, raspberry"
}

def gen_id():
    rand_part = random.randint(10**6, 10**7-1)  # 7 digits
    ts_part = int(str(int(time.time()))[-3:])   # last 3 digits of timestamp
    return int(f"{rand_part}{ts_part:03d}")

def process_image(img_path, category_id, out_json_path):
    with Image.open(img_path) as img:
        width, height = img.size
    size = os.path.getsize(img_path)
    file_name = os.path.basename(img_path)
    img_id = gen_id()
    data = {
        "info": {
            "description": "data",
            "version": "1.0",
            "year": 2025,
            "contributor": "search engine",
            "source": "no_augmentation",
            "license": {
                "name": "Creative Commons Attribution 4.0 International",
                "url": "https://creativecommons.org/licenses/by/4.0/"
            }
        },
        "images": [
            {
                "id": img_id,
                "width": width,
                "height": height,
                "file_name": file_name,
                "size": size,
                "format": "JPG",
                "url": "",
                "hash": "",
                "status": "success"
            }
        ],
        "annotations": [],
        "categories": [
            {
                "id": int(category_id),
                "name": category_map[category_id],
                "supercategory": f"category_{category_id}"
            }
        ]
    }
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    dataset_dirs = ["Fruits_Dataset_Train", "Fruits_Dataset_Test"]
    for dataset_root in dataset_dirs:
        for category_id in map(str, range(1, 9)):
            folder = os.path.join(dataset_root, category_id)
            if not os.path.isdir(folder):
                continue
            for fname in os.listdir(folder):
                if fname.lower().endswith(".jpg"):
                    img_path = os.path.join(folder, fname)
                    json_path = os.path.splitext(img_path)[0] + ".json"
                    process_image(img_path, category_id, json_path)
                    print(f"Processed {img_path}")

if __name__ == "__main__":
    main() 