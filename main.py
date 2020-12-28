import glob
import os

from spotit.utilities import generate_images
from spotit import create_sheets

# Variables
output_filename = "cards"  # filename of the PDF
order = 5  # number of images at each card
images_path = "./template_images"
backside_image_file = "./template_images/01.png"
generate_template_images = True
use_template_images = True

# Generate Template Images
if generate_template_images:
    if not os.path.isdir("./template_images"):
        os.makedirs("./template_images")
    generate_images("./template_images", order=order)  # generate images with numbers
if use_template_images: 
    images_path = "./template_images"

images = sorted(glob.glob(os.path.join(images_path, '*')))  # list of the images
create_sheets(output_filename, order, images, backside_image_file)  # create the PDF with cards
