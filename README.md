# webp-to-jpeg
Python program to convert webp images to jpeg/jpg format

# How it works
## Initial
```
imageFiles/
├── subdir1/
│   ├── image1.webp
│   ├── image2.webp
├── subdir2/
│   ├── image3.webp
│   ├── image4.webp
```
## Final
```
imageFiles/
├── subdir1/
│   ├── image1.webp
│   ├── image2.webp
├── subdir2/
│   ├── image3.webp
│   ├── image4.webp
└── converted_jpegs/
    ├── subdir1/
    │   ├── image1.jpg
    │   ├── image2.jpg
    ├── subdir2/
    │   ├── image3.jpg
    │   ├── image4.jpg
```

# Dependencies
- my_utils (custom library, `pip install git+https://github.com/ivamitran/my_utils`)
- Pillow