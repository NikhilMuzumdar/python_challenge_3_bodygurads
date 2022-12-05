# Text check 1
from input_string import string

caps = [chr(i) for i in range(65, 91)]
small = [chr(i) for i in range(97, 123)]
output = ""

# Iterate through a substring of 9 consecutive chars to check for following:
# 1) If the center element is a small letter
# 2) If the center element is surrounded by a Caps letter
# 3) Weather extremities are not in caps (Since we need exactly 3 caps)
# If above conditions are met, we have our letter

n = 9
while n <= len(string):
    current_string = string[n - 9:n]
    # We define the left, right and centre string
    # We also define the left and right extreme letters to check if they are not in caps
    left = current_string[1:4]
    right = current_string[5:-1]
    center = current_string[4]
    extreme_l = current_string[0]
    extreme_r = current_string[-1]

    # Check if all the 3 letters in left and right are caps
    if all([(element in caps) for element in left + right]):
        # Check if letters in extreme left and right are not caps
        if all([(element not in caps) for element in extreme_r + extreme_l]):
            # if the center letter is a small letter
            if center in small:
                output += center

    n += 1
print(output)
