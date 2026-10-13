from bs4 import BeautifulSoup
import requests

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given URL,
    truncated to 2,000 characters.
    """

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"

    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()

        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    return (title + "\n\n" + text)[:2_000]


def fetch_website_links(url):
    """
    Return the links on the website at the given url
    I realize this is inefficient as we are parsing twice! This  is to kep the code in the lab sample.
    Feel fre to use a class and optimize
    """

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]
