# Using Libraries
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Displaying image
img = cv2.imread('images/RDJ1.jpg')
cv2.imshow('imgage',img)

# Not to close image automatically
cv2.waitKey(0)

