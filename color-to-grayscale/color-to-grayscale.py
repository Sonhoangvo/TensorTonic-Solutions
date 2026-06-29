def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    print(image[0])
    print(image[0][0])
    result = []
    for i in image:
        temp_2 = []
        for j in i:
            temp_2.append(j[0] * 0.299 + j[1] * 0.587 + j[2] * 0.114)
        result.append(temp_2)
    return result