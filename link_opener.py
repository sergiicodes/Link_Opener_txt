import webbrowser

def get_file_path():
    file_path = input("Please enter the file path: ")
    return file_path

# Open the text file
with open(get_file_path()) as f:
    contents = f.read()

# Find the link in the text file
link = None
for line in contents.splitlines():
    if 'http' in line:
        link = line
        break

# Open the link in the default web browser
if link:
    webbrowser.open(link)
else:
    print("No link found in the text file")
