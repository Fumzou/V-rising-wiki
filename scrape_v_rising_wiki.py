import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://vrising.fandom.com/wiki/V_Rising_Wiki"
ALLOWED_PREFIX = "https://vrising.fandom.com/wiki/"
OUTPUT_DIR = "V_Rising_Wiki"

visited = set()


def sanitize_filename(name: str) -> str:
    invalid_chars = '\\/:*?"<>|'
    for ch in invalid_chars:
        name = name.replace(ch, '_')
    return name.replace(' ', '_')


def save_page(title: str, content: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = sanitize_filename(title) + '.txt'
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(title + '\n\n')
        f.write(content)


def clean_content(div) -> str:
    for tag in div(['script', 'style']):
        tag.decompose()
    return div.get_text('\n', strip=True)


def crawl(url: str):
    if url in visited or not url.startswith(ALLOWED_PREFIX):
        return
    print(f"Crawling: {url}")
    visited.add(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('h1', id='firstHeading')
    content_div = soup.find('div', id='mw-content-text')
    if not title_tag or not content_div:
        return
    title = title_tag.get_text(strip=True)
    text = clean_content(content_div)
    save_page(title, text)

    for link in content_div.find_all('a', href=True):
        href = link['href']
        full_url = urljoin(url, href)
        if full_url.startswith(ALLOWED_PREFIX) and full_url not in visited:
            time.sleep(1)
            crawl(full_url)


if __name__ == "__main__":
    crawl(BASE_URL)
    print(f"\nPages processed: {len(visited)}")
    print(f"Output directory: {os.path.abspath(OUTPUT_DIR)}")
