from PIL import Image

def encode_image(image_path, message, output_path):
    image = Image.open(image_path).convert('RGB')
    img_data = list(image.getdata())

    binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'
    total_bits = len(binary_message)
    binary_index = 0

    new_data = []

    for i in range(len(img_data)):
        if binary_index >= total_bits:
            new_data.extend(img_data[i:])
            break

        r, g, b = img_data[i][:3]
        rgb = [r, g, b]

        for j in range(3):
            if binary_index < total_bits:
                bit = int(binary_message[binary_index])
                rgb[j] = (rgb[j] & ~1) | bit
                binary_index += 1

        new_data.append(tuple(rgb))

    encoded_img = Image.new("RGB", image.size)
    encoded_img.putdata(new_data)
    encoded_img.save(output_path)

def decode_image(image_path):
    image = Image.open(image_path).convert('RGB')
    img_data = list(image.getdata())

    binary_message = ''
    for pixel in img_data:
        for value in pixel[:3]:
            binary_message += str(value & 1)

    all_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]

    decoded_message = ''
    for byte in all_bytes:
        if byte == '00000000':
            break
        decoded_message += chr(int(byte, 2))

    return decoded_message
