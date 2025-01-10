import cv2
import numpy as np

def add_block_noise(image_path, noise_weight=0.1, block_size=8):
    """
    Adds block-level Gaussian noise to an image with controlled weight and block size.
    The noise is normalized to fit within valid pixel value range [0, 255].

    Args:
        image_path (str): The path to the input image.
        noise_weight (float): The weight for Gaussian noise, a value between 0 and 1.
                              Higher values introduce more noise.
        block_size (int): The size of the blocks for the noise. Larger blocks make noise more intense and noticeable.

    Returns:
        np.ndarray: The noisy image.
    """
    # Read the image
    image = cv2.imread(image_path)

    # Ensure the image is read properly
    if image is None:
        raise ValueError("Could not read the image, please check the path.")

    # Get the image dimensions
    h, w, c = image.shape

    # Generate low-resolution Gaussian noise with a mean of 0 and standard deviation of 25
    small_noise = np.random.normal(0, 25, (h // block_size, w // block_size, c)).astype(np.float32)

    # Resize the small noise to the size of the original image, creating blocky noise
    large_noise = cv2.resize(small_noise, (w, h), interpolation=cv2.INTER_NEAREST)

    # Normalize the noise to fit in the range [0, 255]
    noise_min = large_noise.min()
    noise_max = large_noise.max()
    normalized_noise = 255 * (large_noise - noise_min) / (noise_max - noise_min)

    # Add noise with a weighted balance between the original image and block noise
    noisy_image = cv2.addWeighted(image.astype(np.float32), 1 - noise_weight, normalized_noise, noise_weight, 0)

    # Clip the image to ensure valid pixel values [0, 255] and convert back to uint8
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    return noisy_image

# Usage example
input_image_path = 'alpaca.jpg'
output_image_path = 'alpaca-1.jpg'

# Adjust block_size to control the size of noise blocks
noise_weight = 1.0  # Adjust noise weight
block_size = 4  # Use larger block sizes for more pronounced noise patterns

# Apply the block noise function and save the output
noisy_image = add_block_noise(input_image_path, noise_weight=noise_weight, block_size=block_size)
cv2.imwrite(output_image_path, noisy_image)
