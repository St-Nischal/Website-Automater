import sys
import webbrowser


urls={
    "work" : ["www.stackoverflow.com", "www.google.com"],
    "personal" : ["www.youtube.com", "www.netflix.com"]
}

def openWebPages(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

if __name__ == "__main__":
    set_name = sys.argv[1]
    urls = urls[set_name]
    openWebPages(urls)