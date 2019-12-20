import sys
import traceback
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup


def valid_url(url):
    if not url:
        return False
    return url.startswith("http://") or url.startswith("https://")


def get_links_from_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if valid_url(url):
            urls.append(url)
    return urls


def get_links_from_url(url):
    response = requests.get(url)
    return get_links_from_text(response.text)


def print_result(url, links):
    print(url)
    for link in links:
        print(f"    {link}")


def parallel_crawl(url, max_workers=None):
    links = get_links_from_url(url)
    print_result(url, links)
    futures = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for link in links:
            futures.append((link, executor.submit(get_links_from_url, link)))
        for link, future in futures:
            try:
                print_result(link, future.result())
            except Exception as e:
                traceback.print_exc()


if __name__ == '__main__':
    parallel_crawl(sys.argv[1])

