from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

def randomSuperpower():
    urls = ["https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Almighty_Powers",
    "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Constructs",
    "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Enhancements",
    "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Magical_Powers",
    "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Manipulations",
    "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Meta_Powers",
    "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Physiology",
    "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Psychic_Powers",
    "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Science_Powers"]

    rand_url = random.choice(urls)

    page = urlopen(rand_url)

    html = page.read().decode("utf-8")

    soup = BeautifulSoup(html, "lxml")

    title = soup.find('h1').text.strip()

    desc = soup.find_all('p')

    for d in desc[1:]:
        cap_string = d.text + "\n"

    response = title + "\n" + "Description: " + desc[0].text + "\n" + "Capabilties: " + cap_string + "Read more about your random power at: https://powerlisting.fandom.com/wiki/%s" % title.replace(" ", "_")

    return response