import argparse
from PIL import Image

def list_supported_formats():
    supported_formats = Image.registered_extensions()
    print("Supported Image Formats (.extension: format_name):")
    for ext, format_name in supported_formats.items():
        print(f"{ext}: {format_name}")

def is_format_supported(format):
    supported_formats = Image.registered_extensions()
    return format.lower() in supported_formats.keys()

def convert_image(input_path, output_path, output_format):
    try:
        image = Image.open(input_path)

        # Convert to RGB mode if the image has an alpha channel (transparency)
        # some file types don't support alpha channel/transparency
        if image.mode == "RGBA":
            image = image.convert("RGB")
        
        image.save(output_path, format=output_format)
        print(f"Image converted to format: {output_format} and saved under: {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")

def main():
    parser = argparse.ArgumentParser(description="Image file converter command line interface :)")

    # --list option will list supported formats
    parser.add_argument("--list", action="store_true", help="List supported image formats")

    # --convert option will perform image conversion
    parser.add_argument("--convert", nargs=3, metavar=("input_path", "output_path", "output_format"), help="Convert an image to a different format")

    # --supported option will check if a user-specified file type is supported for conversion
    parser.add_argument("--supported", help="Check if specific extension type is supported")


    args = parser.parse_args()

    if args.list:
        list_supported_formats()
    
    if args.convert:
        input_path, output_path, output_format = args.convert
        convert_image(input_path, output_path, output_format)
    
    if args.supported:
        is_supported = is_format_supported(args.supported)
        if is_supported:
            print(f"Extension type: {args.supported} is supported!")
        else:
            print(f"Extension type: {args.supported} is NOT supported :(")

if __name__ == "__main__":
    main()
