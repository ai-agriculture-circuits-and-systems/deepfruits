# DeepFruits Dataset

A comprehensive labeled dataset consisting of 21,122 fruit images of 20 diverse kinds of fruits based on 8 different fruit set combinations.

## Dataset Description

The DeepFruits dataset is designed for fruit recognition and calories estimation tasks. It contains images with various fruit combinations, making it suitable for computer vision, image classification, and deep learning research.

- **Number of images**: 21,122
- **Number of fruit types**: 20
- **Combinations**: 8 different fruit set combinations
- **Format**: Images with corresponding JSON annotation files for training and testing

## Dataset Structure

The dataset is organized as follows:

```
.
├── Fruits_Dataset_Train/
│   ├── 1/
│   │   ├── image1.jpg
│   │   ├── image1.json
│   │   └── ...
│   ├── 2/
│   │   └── ...
│   └── ... (up to 8)
├── Fruits_Dataset_Test/
│   ├── 1/
│   │   └── ...
│   └── ... (up to 8)
├── generate_json.py
└── README.md
```

- `Fruits_Dataset_Train/` and `Fruits_Dataset_Test/` contain 8 subfolders (`1` to `8`), each representing a fruit combination category.
- Each subfolder contains `.jpg` images and their corresponding `.json` annotation files with the same base name.

## JSON Annotation File Structure

Each image has a corresponding JSON file with the following structure:

```json
{
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
      "id": 1234567890,
      "width": 5184,
      "height": 3456,
      "file_name": "IMG_0248.JPG",
      "size": 10603464,
      "format": "JPG",
      "url": "",
      "hash": "",
      "status": "success"
    }
  ],
  "annotations": [],
  "categories": [
    {
      "id": 1,
      "name": "margo, grape, plum, kiwi, pear",
      "supercategory": "category_1"
    }
  ]
}
```

- `info`: General information about the dataset and license.
- `images`: Metadata for the image, including a unique id, dimensions, file name, and file size.
- `annotations`: Empty array (no bounding box or segmentation annotations).
- `categories`: Only the category for the current image, with both the category id and the fruit names.

## Category Mapping

| Category ID | Fruit Combination                                      |
|-------------|-------------------------------------------------------|
| 1           | margo, grape, plum, kiwi, pear                        |
| 2           | apple, orange, banana, pomegranate, strawberry        |
| 3           | pineapple, fig, peach, apricot, avocado               |
| 4           | summar, squash, lemon, lime, guava, raspberry         |
| 5           | banana, pomegranate, orange, grape                    |
| 6           | guava, pear, lime, apricot                            |
| 7           | apple, strawberry, plum, kiwi                         |
| 8           | avocado, lemon, raspberry                             |

## Contributors

- Ghazanfar Latif
- Jaafar Alghazo
- Nazeeruddin Mohammad

## Institution

Prince Mohammad Bin Fahd University

## Applications

This dataset can be used for:
- Fruit recognition
- Calories estimation
- Image classification
- Computer vision research
- Deep learning model training

## Categories

- Computer Science
- Artificial Intelligence
- Computer Vision
- Image Segmentation
- Machine Learning
- Diet
- Image Classification
- Decision Making
- Recognition
- Deep Learning

## Citation

```
Latif, G., Alghazo, J., & Mohammad, N. (2022). DeepFruits: Dataset of Fruits Images with different combinations for Fruit Recognition and Calories Estimation [Data set]. Mendeley Data. https://doi.org/10.17632/5prc54r4rt.1
```

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See the [LICENSE](LICENSE) file for details.

## Source

The original dataset is available at: [Mendeley Data](https://data.mendeley.com/datasets/5prc54r4rt/1) 