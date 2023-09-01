
# Multiple Facematching with Python

![Demo Image](demo.png)

This project is a simple Python script that demonstrates face recognition using the Face Recognition library. It allows you to compare a known face with faces in a folder of unknown images and print the filenames of the matching images.

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3.x

You can install the required libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the code to your computer.

2. Place the reference image (known face) in the root directory with the filename `tom.png`. You can replace this image with your own.

3. Create a folder named `images` in the root directory. This folder should contain the images you want to compare against the known face.

4. Run the script:

```bash
python match_list.py
```

The script will compare the known face with all the faces in the `images` folder and print the filenames of the matching images.

## Example

Here's a brief example of how to use this code:

1. Place `tom.png` (known face) in the root directory.

2. Create a folder named `images` and add multiple images of faces you want to compare.

3. Run the script:

```bash
python match_list.py
```

You will see a list of filenames of images in the `images` folder where a match is found with the known face.
