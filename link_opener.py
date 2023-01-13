import webbrowser

# Open the text file
with open(r'C:\Users\shacosta\Desktop\Motion Calcs/Convert kg-m^2 to lb-in^2.txt') as f:
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
