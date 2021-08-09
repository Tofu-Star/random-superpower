from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

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
    url = "https://powerlisting.fandom.com/wiki/Special:Random"

    response = formulateMessage(url)

    return response

def randByCategory(category):
    url = "https://powerlisting.fandom.com/wiki/Special:RandomInCategory/"
    response = "Sorry, I didn't understand that command! \nPlease choose one of the nine categories\n(Almighty, Enhancements, Magical Powers, Manipulations, Meta Powers, Physiology, Psychic Powers or Science Powers)\n or type !-superpower, without the -, to roll a truly random power!\nType !-help, without the -, for more info!"

    #Python doesn't have a switch case statement
    #So this will have to do
    #But it doesn't look great
    if(category == "almighty"):
        url += "Almighty_Powers"
    elif(category == "construct"):
        url += "Constructs"
    elif(category == "enhancement"):
        url += "Enhancements"
    elif(category == "magical"):
        url += "Magical_Powers"
    elif(category == "manipulation"):
        url += "Manipulations"
    elif(category == "meta"):
        url += "Meta_Powers"
    elif(category == "physiology"):
        url += "Physiology"
    elif(category == "psychic"):
        url += "Psychic_Powers"
    elif(category == "science"):
        url += "Science_Powers"
    else:
        return response

    response = formulateMessage(url)

    return response
