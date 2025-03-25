# for all tools in the csv file, download the icon from the url and save it to the icons folder

import requests
import os
import csv
from utils.string_helpers import clean_name


TOOL_ICON_URL_FIELD = "Tool Icon URL"
TOOL_NAME_FIELD = "Tool Name"

def suffix(url):
    # get suffix from url
    # also strip query params
    # return as string
    return str(os.path.splitext(url.split('?')[0])[1])

def download_icon(name,url, filename):

    # timeout after 5 seconds
    try:
        response = requests.get(url, timeout=5)

        # get redirected url
        if (url != response.url):
            print(f"Redirected to {response.url}")
            url = response.url
        
        if response.status_code == 200:

            # check if the file already exists
            if os.path.exists(filename):
                print(f"Skipping {filename} because it already exists")
                return

            print(f"Saving icon to {filename}")

            with open(filename, 'wb') as file:
                file.write(response.content)
            
            # check if the file is an image
        else:
            print(f"Failed to download icon from {url}")
    except Exception as e:
        print(f"Error downloading icon from {url}: {e}")

def main():
    # read the csv file
    with open('data/csv/AI Native Dev Tool Catalog - Internal - Tools.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        tools = list(csv_reader)  

    for tool in tools:
            icon_url = tool[TOOL_ICON_URL_FIELD]
            name = tool[TOOL_NAME_FIELD] 

            # create the icons folder
            os.makedirs(f"data/repo/data/icons", exist_ok=True)

            if icon_url:
                    download_icon(name, icon_url, f"data/repo/data/icons/{clean_name(name)}{suffix(icon_url)}")
            else:
                #print(f"Skipping {name} because it contains Rover")
                continue


if __name__ == "__main__":
    main()
