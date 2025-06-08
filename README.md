# V Rising Wiki Scraper

This repository contains scripts to download and consolidate content from the V Rising Wiki.

- `scrape_v_rising_wiki.py` recursively crawls the wiki starting from the home page and saves each page into the `V_Rising_Wiki` directory.
- `compile_wiki.py` downloads a predefined list of wiki pages and appends their cleaned contents into a single text file `V_Rising_Wiki.txt`.

Both scripts throttle requests to avoid overwhelming the server.
