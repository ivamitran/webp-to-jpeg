from my_utils import MenuProgram as MP

class ImageConverter:
    @staticmethod
    def prompt_for_subdirectory():
        import os
        
        # Directory where imageFiles is expected to exist
        image_files_dir = "imageFiles"

        # Ensure the imageFiles directory exists
        if not os.path.isdir(image_files_dir):
            print(f"Directory '{image_files_dir}' not found. Please ensure it exists.")
            return None

        # List subdirectories
        subdirs = [d for d in os.listdir(image_files_dir) if os.path.isdir(os.path.join(image_files_dir, d))]
        if not subdirs:
            print("No subdirectories found within 'imageFiles'.")
            return None

        # Display subdirectory options
        print("Select a subdirectory:")
        for i, subdir in enumerate(subdirs, start=1):
            print(f"{i}. {subdir}")

        # Get user selection
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(subdirs):
                return os.path.join(image_files_dir, subdirs[choice - 1])
            else:
                print("Invalid choice.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    @staticmethod
    def convert_webp_to_jpeg():
        import os
        from PIL import Image

        # Prompt the user for a subdirectory
        subdir_path = ImageConverter.prompt_for_subdirectory()
        if not subdir_path:
            return

        # Create an output directory for converted JPEGs
        converted_dir = os.path.join(subdir_path, "converted_jpegs_webp")
        os.makedirs(converted_dir, exist_ok=True)

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

                        # Save the .jpg file in the converted_jpegs_webp directory
                        jpg_file_name = os.path.splitext(file_name)[0] + ".jpg"
                        jpg_path = os.path.join(converted_dir, jpg_file_name)
                        img.save(jpg_path, "JPEG")
                        print(f"Converted: {webp_path} -> {jpg_path}")
                except Exception as e:
                    print(f"Failed to convert {webp_path}: {e}")

        print(f"All .webp files in '{subdir_path}' have been converted.")

    @staticmethod
    def convert_heic_to_jpeg():
        import os
        from PIL import Image
        import pillow_heif  # Import pillow-heif to enable HEIC support

        # Register HEIF format with Pillow
        pillow_heif.register_heif_opener()

        # Prompt the user for a subdirectory
        subdir_path = ImageConverter.prompt_for_subdirectory()
        if not subdir_path:
            return

        # Create a "converted_jpegs_heic" directory within this subdirectory
        converted_dir = os.path.join(subdir_path, "converted_jpegs_heic")
        os.makedirs(converted_dir, exist_ok=True)

        # Iterate through files in the subdirectory
        for file_name in os.listdir(subdir_path):
            if file_name.lower().endswith(".heic"):
                # Full path to the .heic file
                heic_path = os.path.join(subdir_path, file_name)

                # Convert .heic to .jpg
                try:
                    with Image.open(heic_path) as img:
                        # Convert to RGB mode (JPEG doesn't support transparency)
                        img = img.convert("RGB")

                        # Save the .jpg file in the converted_jpegs_heic directory
                        jpg_file_name = os.path.splitext(file_name)[0] + ".jpg"
                        jpg_path = os.path.join(converted_dir, jpg_file_name)
                        img.save(jpg_path, "JPEG")
                        print(f"Converted: {heic_path} -> {jpg_path}")
                except Exception as e:
                    print(f"Failed to convert {heic_path}: {e}")

        print(f"All .heic files in '{subdir_path}' have been converted.")

    @staticmethod
    def delete_contents_of_imageFiles():
        import os
        import shutil

        # Directory where imageFiles is expected to exist
        image_files_dir = "imageFiles"

        # Ensure the imageFiles directory exists
        if not os.path.isdir(image_files_dir):
            print(f"Directory '{image_files_dir}' not found. Nothing to delete.")
            return

        # Iterate through all contents of imageFiles
        for item in os.listdir(image_files_dir):
            item_path = os.path.join(image_files_dir, item)

            # Skip placeholder.txt
            if os.path.basename(item_path) == "placeholder.txt":
                print(f"Skipping: {item_path}")
                continue

            try:
                # If it's a directory, delete it recursively
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Deleted directory: {item_path}")
                # If it's a file, delete it
                elif os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"Deleted file: {item_path}")
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")

        print(f"All contents of '{image_files_dir}' have been deleted.")

if __name__ == "__main__":
    menuProgram = MP.MenuProgram()
    menuProgram.add_option("Convert .webp to .jpg", ImageConverter.convert_webp_to_jpeg)
    menuProgram.add_option("Convert .heic to .jpg", ImageConverter.convert_heic_to_jpeg)
    menuProgram.add_option("Delete all content w/i imageFiles", ImageConverter.delete_contents_of_imageFiles)
    menuProgram.run()