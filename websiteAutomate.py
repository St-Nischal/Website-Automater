import re
import sys
import webbrowser


urls={
    "work" : ["www.stackoverflow.com", "www.google.com"],
    "personal" : ["www.youtube.com", "www.netflix.com"]
}

def is_valid_url(url):
    regex = re.compile(
        r'^(https?:\/\/)?'
        r'([a-zA-Z0-9.-]+)'
        r'(\.[a-zA-Z]{2,6})'
        r'(\/[a-zA-Z0-9@:%_+.~#?&//=]*)?$'
    )
    return re.match(regex, url) is not None




def openWebPages(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Error: Please a catagory")
        sys.exit(1)

    set_name = sys.argv[1]

    if set_name not in urls:
        print(f"Error: '{set_name} is not a valid category'")
        sys.exit(1)

    valid_urls = [url if url.startswith("http") else f"https://{url}" for url in urls[set_name] if is_valid_url(url)]
    if not valid_urls:
        print("Error: No valid URLs found in this category.")
        sys.exit(1)

    


    urls = urls[set_name]
    openWebPages(urls)