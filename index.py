def read_and_write_file():
    import os
    
    try:
        # Prompt the user to enter the input file name
        input_filename = input("Enter the name of the file to read: ").strip()

        # Check if the input file exists
        if not os.path.exists(input_filename):
            print(f"Error: The file '{input_filename}' does not exist. Please try again.")
            return

        # Open the input file and read its content
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
            if not lines:
                print(f"Error: The file '{input_filename}' is empty. Nothing to process.")
                return
        
        # Prompt the user to enter the output file name
        output_filename = input("Enter the name of the new file to write to: ").strip()

        # Check if the output file already exists and confirm overwriting
        if os.path.exists(output_filename):
            confirm = input(f"The file '{output_filename}' already exists. Overwrite it? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Operation cancelled. No changes made.")
                return

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            for i, line in enumerate(lines, start=1):
                outfile.write(f"{i}: {line}")
        
        print(f"Success: File '{output_filename}' has been created with modified content!")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for the file '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == "__main__":
    print("Welcome to the File Read & Write Program! 🖋️")
    print("This program will read a file, modify its content, and save it to a new file.")
    print("-" * 50)
    read_and_write_file()
