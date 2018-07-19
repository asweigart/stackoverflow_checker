# stackoverflow_checker
A simple script I use to check for StackOverflow questions on a given topic (PyAutoGUI, in my case).

# Installation

Just download the zip file and extract `stackoverflow_checker.py`. You'll also need the Requests and BeautifulSoup modules, which you can install with `pip3` (on Linux/Mac) or `pip` (on Windows):

    pip3 install requests
    pip3 install beautifulsoup4

# Usage

Edit the `queries` variable in `stackoverflow_checker.py` and set it to the search terms you want to use, then run `python3 stackoverflow_checker.py` (on Linux/Mac) or `python stackoverflow_checker.py` (on Windows).

Note that each string in `queries` is what you would type into the search bar. If you want to search for "python concatenation operator", you would set it to `['python concatenation operator']`, not `['python', 'concatenation', 'operator']`. The separate strings in this list are as if you wanted to run the script multiple times with different search queries.