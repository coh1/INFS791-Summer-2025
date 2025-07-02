from bs4 import BeautifulSoup
import urllib.request

from pathlib import Path

# Construct the Path object for the Audiobooks.html file in the Mac IOS Documents folder
# Path.home() gets the user's home directory (e.g., /Users/yourusername on Mac)
# The / operator is used for joining path components in pathlib
documents_folder_path = Path.home() / "Documents"
audiobooks_html_path = documents_folder_path / "Audiobooks.html"


# 2. Convert the Path object to a file:// URL string
# .as_uri() properly formats the path for urllib.request on all OS.
AudioBooksFile_url = audiobooks_html_path.as_uri() # Renamed to be explicit about it being a URL

# 3. Open the local HTML file using urllib.request.urlopen
try:
    Audio_Books_html = urllib.request.urlopen(AudioBooksFile_url)
    print("Successfully opened the HTML file using urllib.request.urlopen.")

    # 4. Parse the HTML content with BeautifulSoup
    html_to_parse = BeautifulSoup(Audio_Books_html, "html.parser")

    # 5. Create a list of audiobooks found in the webpage (assuming they are in <li> tags)
    List_of_Audiobooks_found = html_to_parse.find_all("li")

    Audiobookslist = []
    for element in List_of_Audiobooks_found:
        Audiobookslist.append(element.text.strip()) # Use .strip() for cleaner text

    print("\n--- Results ---")
    print("Number of Audiobooks found: " + str(len(Audiobookslist)))

    if Audiobookslist: # Check if the list is not empty before trying to access index 0
        print("The first book on the list is: ", Audiobookslist[0])
    else:
        print("No audiobooks found in the list.")

except urllib.error.URLError as e:
    print(f"URLError when trying to open file URL: {e}")
    print("This can happen if the URL is malformed, permissions are an issue, or the file path is incorrect.")
except Exception as e:
    print(f"An unexpected error occurred during HTML parsing: {e}")
