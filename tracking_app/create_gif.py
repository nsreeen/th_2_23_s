from PIL import Image

image = Image.frombytes("RGB", (1,1), bytes("100", encoding="UTF-8"), decoder_name="raw")

image.save('gif.gif', save_all=True)
