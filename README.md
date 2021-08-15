# Optical character recognition (OCR) with help of R-tree
Optical character recognition or optical character reader is the electronic or mechanical conversion of images of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document, a scene-photo or from subtitle text superimposed on an image.


Steps:
1. convert pdf to image, if multiple pdf pages then each page into the individual image file.
2. convert the colour image into a grayscale image
3. read/create target bounding boxes
4. with help of tesseract to recognize the character in the image
5. create an r-tree index for each bounding box of tesseract output data.
6. find the intersection of the target bounding box in an r-tree index.
7. get the required target index from the data frame, continue processing text if necessary.
8. repeat above step remaining pages.

Refrence:
1. [ocr wiki](https://en.wikipedia.org/wiki/Optical_character_recognition)
1. [bbox stackoverflow](https://stackoverflow.com/questions/20831612/getting-the-bounding-box-of-the-recognized-words-using-python-tesseract)