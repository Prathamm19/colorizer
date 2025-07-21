# Add your cartoonization model logic here
import cv2
import numpy as np
from PIL import Image

def cartoonize(pil_image):
    img = np.array(pil_image)
    # 1. Edge Mask
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 9
    )
    # 2. Color Quantization
    data = np.float32(img).reshape((-1, 3))
    k = 8
    compactness, labels, centers = cv2.kmeans(
        data, k, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001), 10, cv2.KMEANS_RANDOM_CENTERS
    )
    centers = np.uint8(centers)
    quant = centers[labels.flatten()].reshape(img.shape)
    # 3. Combine Color + Edge Mask
    blurred = cv2.bilateralFilter(quant, d=9, sigmaColor=300, sigmaSpace=300)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    return Image.fromarray(cartoon)
