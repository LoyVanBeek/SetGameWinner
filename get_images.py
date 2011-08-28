""""Downloads the images of cards shamefully from thebreretons.com/setgame"""

import urllib2

def combis():
    for num in ['1','2','3']:
        for color in ['r','p','g']: #red, purple, green
            for shape in ['s','d','o']: #squiggle, diamond, oval
                for fill in ['f','s','e']: #full, striped, empty
                    yield num+color+fill+shape

def download_card(filename, folder="http://thebreretons.com/setgame/images/"):
    full_url = folder+filename+".png"

    opener = urllib2.build_opener()
    page = opener.open(full_url)
    pic = page.read()

    return pic

if __name__ == "__main__":
##    pass
    c = combis()
    url1 = c.next()
    card1 = download_card(url1)
    #cards = {card:download_card(card) for car in combis()}
    for card in combis():
        cardimg = download_card(card)
        f = open(card+".png",  "wb")
        f.write(cardimg)
        f.close()
        
