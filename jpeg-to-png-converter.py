from PIL import Image
import os

def jpeg_to_png_converter():
    print("JPEG to PNG Converter")
    
    # Input JPEG file
    while True:
        input_file = input("Enter the path to your JPEG file: ")
        if os.path.isfile(input_file) and input_file.lower().endswith(('.jpg', '.jpeg')):
            break
        else:
            print("Invalid file path or not a JPEG file. Please try again.")
    
    # Output PNG file
    output_file = os.path.splitext(input_file)[0] + ".png"
    
    try:
        # Open the JPEG image
        with Image.open(input_file) as img:
            # Save as PNG
            img.save(output_file, 'PNG')
        
        print(f"Conversion complete! PNG file saved as: {output_file}")
    
    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")

if __name__ == "__main__":
    jpeg_to_png_converter()
