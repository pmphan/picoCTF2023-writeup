import argparse
from itertools import permutations
from PIL import Image

def write_to_file(file_path, bytels):
    with open(file_path, 'w') as f:
        for byte in bytels:
            f.write(chr(byte))
        f.write('\n')

def msb_decode(image_path, order, channels) -> list[int]:
    mask = 0b10000000           # MSB mask
    with Image.open(image_path) as image_file:
        if order == 'yx':
            image_file.transpose(Image.Transpose.TRANSPOSE)
        W, H = image_file.size
        final_bytes = []
        a_byte = 0
        i = 0
        for x in range(H):
            for y in range(W):
                r, g, b = image_file.getpixel((y, x))

                for c in channels:
                    # Extract MSB to 0b1 or 0b0
                    if c == 'r':
                        msb = r // mask
                    elif c == 'g':
                        msb = g // mask
                    else:
                        msb = b // mask

                    # Assemble 8 bits into a byte 
                    a_byte += msb * (2**(7-i))
                    i += 1
                    if i == 8:
                        final_bytes.append(a_byte)
                        a_byte = 0
                        i = 0
        return final_bytes

def main():
    parser = argparse.ArgumentParser(description="MSB script for PicoCTF2023")
    parser.add_argument("image_file", help="Path to the image file")
    parser.add_argument("--write", "-w", default="decoded",
                        help="Path to output file")
    parser.add_argument("--order", "-o", choices=["xy", "yx"], default="xy",
                        help="Pixel iteration order")

    valid_channels = []
    channels = "rgb"
    for i in range(len(channels)):
        valid_channels.extend(["".join(p) for p in permutations("rgb", i+1)])

    parser.add_argument("--channels", "-c", choices=valid_channels, default="rgb",
                        help="Selected channels")


    args = parser.parse_args()
    extracted_bytes = msb_decode(args.image_file, args.order, args.channels)
    write_to_file(args.write, extracted_bytes)

main()
