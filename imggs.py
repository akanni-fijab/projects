import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)  # creates pil obj

images[0].save(
    "timenow.gif",
    save_all=True,
    append_images=[images[1], images[2]],
    duration=300,
    loop=0,
)
