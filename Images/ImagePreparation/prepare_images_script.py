
def run():
    import os
    import sys
    import glob
    import ImagePreparer

    # Define constants
    input_path = "../input/"
    output_path = "../output/"
    resize_to_width = 360

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print("Output directory created.")
    if not os.path.exists(input_path):
        os.makedirs(output_path)
        print("Input directory created.")


    print("Loading images from input directory...")
    all_input_files = glob.glob(input_path + "*.jpg")
    print(f"Found {len(all_input_files)} images.")

    if len(all_input_files) == 0:
        print("No images found in input directory. Exiting.")
        sys.exit(1)


    first_command_argument = sys.argv[1] if len(sys.argv) > 1 else None
    remove_input_files = False
    if first_command_argument and first_command_argument.lower() == "delete":
        remove_input_files = True
        print("All input files will be deleted.")


    print("Processing images...")
    ImagePreparer.ImagePreparer.prepare_images(
        all_input_files,
        output_path,
        resize_to_width,
        remove_input=remove_input_files
    )
    print("Images processed and saved to output directory.")

    sys.exit(0)

if __name__ == '__main__':
    run()
