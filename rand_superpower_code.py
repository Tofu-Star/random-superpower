from bs4 import BeautifulSoup
from urllib.request import urlopen

def formulateMessage(url):
    page = urlopen(url)

    html = page.read().decode("utf-8")

    soup = BeautifulSoup(html, "lxml")

    title = soup.find('h1').text.strip()

    desc = soup.find_all('p')

    for d in desc[1:]:
        cap_string = d.text + "\n"

    response = title + "\n" + "Description: " + desc[0].text + "\n" + "Capabilties: " + cap_string + "Read more about your random power at: https://powerlisting.fandom.com/wiki/%s" % title.replace(" ", "_")
    
    return response

def randomSuperpower(category = None):
    url = "https://powerlisting.fandom.com/wiki/"

    #Python doesn't have a switch case statement
    #So this will have to do
    #But it doesn't look great
    if(category == "almighty"):
        url += "Special:RandomInCategory/Almighty_Powers"
    elif(category == "construct"):
        url += "Special:RandomInCategory/Constructs"
    elif(category == "enhancement"):
        url += "Special:RandomInCategory/Enhancements"
    elif(category == "magical"):
        url += "Special:RandomInCategory/Magical_Powers"
    elif(category == "manipulation"):
        url += "Special:RandomInCategory/Manipulations"
    elif(category == "meta"):
        url += "Special:RandomInCategory/Meta_Powers"
    elif(category == "physiology"):
        url += "Special:RandomInCategory/Physiology"
    elif(category == "psychic"):
        url += "Special:RandomInCategory/Psychic_Powers"
    elif(category == "science"):
        url += "Special:RandomInCategory/Science_Powers"
    else:
        url += "Special:Random"

    response = formulateMessage(url)

    return response