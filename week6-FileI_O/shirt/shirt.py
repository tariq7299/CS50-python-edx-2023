import sys
from PIL import Image
from PIL import ImageOps

# Check the number of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

for arg in sys.argv[1:]:
    if ".jpg" not in arg and ".png" not in arg and ".jpeg" not in arg:
        sys.exit("Invalid images format")

input_extension_point_index =  sys.argv[1].find(".")
input_extension = sys.argv[1][input_extension_point_index+1:]

output_extension_point_index =  sys.argv[2].find(".")
output_extension = sys.argv[2][output_extension_point_index+1:]

if input_extension_point_index == -1 or output_extension_point_index == -1:
        sys.exit("No extensions found for provided images")

if input_extension != output_extension:
    sys.exit("Input and output have different extensions")

try:
    #shirt.png
    shirt_image = Image.open("./shirt.png")
    #before1.jpg
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

input_image = ImageOps.fit(input_image, (600, 600))
input_image.paste(shirt_image, (0, 0), mask=shirt_image)
input_image.save(sys.argv[2])
