Webpage Automation Script

  This Python script allows users to quickly open a predefined set of webpages in their default web browser. 
  It is useful for automating daily tasks by opening frequently used work or personal websites with a single command.

Features:

  * Opens multiple webpages at once.

  * Supports different sets of URLs (e.g., work-related or personal browsing).

  * Simple command-line interface.

Prerequisites: 
    Ensure you have Python installed on your system. 
    The script uses the built-in webbrowser module, so no additional dependencies are required.

Installation:

    Clone this repository or download the script.

    Ensure Python is installed (Python 3 recommended).

Usage: Run the script from the command line with one of the predefined categories.

    python script.py work

or

    python script.py personal

Available Categories:

    work: Opens Stack Overflow and Google.

    personal: Opens YouTube and Netflix.

How It Works

    1.The script takes a command-line argument specifying the category (work or personal).

    2.It retrieves the corresponding list of URLs.

    3.It opens each URL in a new browser tab.

Customization

    To add more website categories, modify the urls dictionary in the script:

urls = {
    "work": ["www.stackoverflow.com", "www.google.com"],
    "personal": ["www.youtube.com", "www.netflix.com"],
    "study": ["www.khanacademy.org", "www.coursera.org"]
}

Author: Nischal Poudel
