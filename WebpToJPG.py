from my_utils import MenuProgram as MP

class WebpToJPG():
    def convert_webp_to_jpeg():
        import os
        from PIL import Image
        
        # The directory where imageFiles is expected to exist
        image_files_dir = "imageFiles"

        # Ensure the imageFiles directory exists
        if not os.path.isdir(image_files_dir):
            print(f"Directory '{image_files_dir}' not found. Please ensure it exists.")
            return

        # Create an output directory for converted JPEGs
        output_dir = os.path.join(image_files_dir, "converted_jpegs")
        os.makedirs(output_dir, exist_ok=True)

        # Iterate through each subdirectory in imageFiles
        for subdir_name in os.listdir(image_files_dir):
            subdir_path = os.path.join(image_files_dir, subdir_name)

            # Ensure it's a directory (ignore files in the root of imageFiles)
            if os.path.isdir(subdir_path) and subdir_name != "converted_jpegs":
                # Iterate through files in the subdirectory
                for file_name in os.listdir(subdir_path):
                    if file_name.lower().endswith(".webp"):
                        # Full path to the .webp file
                        webp_path = os.path.join(subdir_path, file_name)

                        # Convert .webp to .jpg
                        try:
                            with Image.open(webp_path) as img:
                                # Convert to RGB mode (JPEG doesn't support transparency)
                                img = img.convert("RGB")

                                # Save in the output directory, preserving the subdirectory name
                                output_subdir = os.path.join(output_dir, subdir_name)
                                os.makedirs(output_subdir, exist_ok=True)

                                # Save as .jpg
                                jpg_file_name = os.path.splitext(file_name)[0] + ".jpg"
                                jpg_path = os.path.join(output_subdir, jpg_file_name)
                                img.save(jpg_path, "JPEG")
                                print(f"Converted: {webp_path} -> {jpg_path}")
                        except Exception as e:
                            print(f"Failed to convert {webp_path}: {e}")

        print(f"All .webp files have been converted. Check the directory: {output_dir}")

if __name__ == "__main__":
    menuProgram = MP.MenuProgram()
    menuProgram.add_option("Synthesize directory of webp to jpg", WebpToJPG.convert_webp_to_jpeg)
    menuProgram.run()