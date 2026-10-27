from bs4 import BeautifulSoup
def tytuly(html):
    soup = BeautifulSoup(html, "html.parser")
    return [x.text for x in soup.select(".album")]
