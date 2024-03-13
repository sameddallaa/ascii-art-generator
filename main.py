from ascii_gen import grayscale_to_ascii, grayscale_image, resize_image, display_ascii_art
import PIL.Image

while True:
    try:
        path = input("Enter path to image: ")
        image = PIL.Image.open(path)
        break
    except Exception:
        print("Bad path. Try again: \n")
        continue

new_image = grayscale_to_ascii(grayscale_image(resize_image(image)))

pixel_count = len(new_image)
new_width = 100
ascii_image = "\n".join(new_image[i:i+new_width] for i in range(0, pixel_count, new_width))

print(ascii_image)

display_ascii_art(ascii_image, 'Consolas', 6)
with open('output.txt', 'w') as output:
    output.write(ascii_image)