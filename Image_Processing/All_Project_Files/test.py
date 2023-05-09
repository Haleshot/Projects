import numpy as np
import cv2

def laplacian_filter(img, kernel_size=3):
    # Define the Laplacian kernel
    kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ], dtype=np.float32)
    
    # Pad the image with zeros
    padded_img = np.pad(img, pad_width=kernel_size//2, mode='constant')
    
    # Apply the Laplacian filter to the image
    filtered_img = np.zeros_like(img, dtype=np.float32)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            filtered_img[i, j] = np.sum(padded_img[i:i+kernel_size, j:j+kernel_size] * kernel)
    
    # Normalize the filtered image to the range [0, 255]
    filtered_img = cv2.normalize(filtered_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    return filtered_img


img = cv2.imread('All_Test_Images\Image_2.jpg', cv2.IMREAD_GRAYSCALE)

# Apply the Laplacian filter to the image
filtered_img = laplacian_filter(img)

# Display the original and filtered images side by side
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()