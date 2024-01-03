import os
from difflib import get_close_matches

# Get user input for the search keyword and desired percentage accuracy
var = input("Search for: ")
percentage_accuracy = input("What percentage accuracy would you like to index: ")
cut_off = int(percentage_accuracy) / 100  # Convert percentage to decimal
path = os.getcwd()  # Get the current working directory
result_index = 0  # Initialize the result index counter

# Function to check if a keyword is a close match to a file name
def is_close_match(keyword, file_name):
    matches = get_close_matches(keyword, [file_name], n=1, cutoff=cut_off)
    return bool(matches) and len(matches[0]) >= len(keyword) - 1

print("The top results are:")
for root, directories, files in os.walk(path):

    for file_name in files:

        # Check if the file name is a close match to the search keyword
        if is_close_match(var, file_name):
            result_index += 1  # Increment the result index counter
            file_path = os.path.join(root, file_name)  # Get the full path of the file

            # Display the result and ask the user if they want to open the file
            print(f'\n{result_index}. {file_name}\n')
            choice = input("Would you like to open the file? Y/N: ")

            if choice.upper() == "Y":
                os.startfile(file_path)  # Open the file using the default application
                break  # Exit the loop if the file is opened
            else:
                break  # Exit the loop if the user chooses not to open the file

