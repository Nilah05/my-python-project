def read_and_write_file():
    # Ask the user for the input filename
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")

    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            # Read all content from the input file
            content = file.read()
        
        # Modify the content (example: converting all text to uppercase)
        modified_content = content.upper()  # You can change this modification as needed

        # Open the output file in write mode and save the modified content
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"File '{input_file}' was successfully read, modified, and written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read or write the file '{input_file}' or '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
read_and_write_file()
