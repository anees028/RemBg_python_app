import os
from rembg import remove
from PIL import Image

def remove_background_folder(input_folder: str, output_folder: str):
    """
    Remove backgrounds from all images in a folder and save to output folder.
    Supports .jpg, .jpeg, and .png files.
    """
    if not os.path.exists(input_folder):
        print(f"❌ Input folder not found: {input_folder}")
        return

    os.makedirs(output_folder, exist_ok=True)
    supported_ext = (".jpg", ".jpeg", ".png")

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_ext)]

    if not image_files:
        print(f"⚠️ No images found in {input_folder}")
        return

    print(f"🔄 Processing {len(image_files)} image(s) from '{input_folder}'...\n")

    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_no_bg.png")

        try:
            with Image.open(input_path) as img:
                result = remove(img)
                result.save(output_path)
                print(f"✅ Saved: {output_path}")
        except Exception as e:
            print(f"❌ Failed for {filename}: {e}")

    print("\n🎉 All done! Backgrounds removed and saved to:", output_folder)


def main():
    # Example usage – change these paths as needed
    input_folder = "input-images"
    output_folder = "output-images"

    remove_background_folder(input_folder, output_folder)


if __name__ == "__main__":
    main()
