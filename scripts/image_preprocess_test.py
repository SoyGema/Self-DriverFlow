

def test_graysacle(img):
    output_value, error_value = grayscale(img)
    return plt.imshow(output_value, error_value, cmap='gray')

def test_canny(img, low_threshold, high_threshold):
    output_value, error_value = canny(img, low_threshold, high_threshold)
    return plt.imshow(cmap='gray')

def test_gaussian_blur(img, kernel_size):
    output_value, error_value = gaussian_blur(img, kernel_size)
    return plt.imshow(cmap='Blurred')

