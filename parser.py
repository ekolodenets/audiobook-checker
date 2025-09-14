import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import quote

def get_last_book_from_site(url):
    """Gets the latest book title from the site."""
    try:
        # Encode URL for proper requests handling
        encoded_url = quote(url, safe=':/?&=')

        # Comprehensive headers to mimic browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://audioboo.org/',
            'DNT': '1',
            'Sec-GPC': '1',
        }

        session = requests.Session()
        response = session.get(encoded_url, headers=headers, timeout=15)

        if response.status_code != 200:
            return None

        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        return parse_book_title(soup)

    except Exception:
        return None

def parse_book_title(soup):
    """Parses book title from HTML."""
    try:
        # Try different selectors
        selectors = [
            'h2',
            '.title a',
            'a[href*="/book/"]',
            '.product-title',
            '.item-title',
            'h2 a',
            '.book-title',
            '.name'
        ]

        for selector in selectors:
            elements = soup.select(selector)
            if elements:
                for element in elements[:3]:
                    text = element.get_text(strip=True)
                    if text and len(text) > 10:
                        return text

        # Additional fallback
        for tag in soup.find_all(['h2', 'a']):
            text = tag.get_text(strip=True)
            if text and len(text) > 20 and len(text) < 200:
                return text

        return None

    except Exception:
        return None