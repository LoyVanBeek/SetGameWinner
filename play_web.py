""""Plays the game of Set via the website http://thebreretons.com/setgame/
It uses GUI automation via autopy to play and recognize the cards.

This is the process:
 - take a screenshot
 - for each file:
     determine if its on the table and get its position
 -  from the filenames of the detected cards, construct Card-objects
 -  use find_sets(...)
 -  click each of the sets card by card
     
"""

import logic
import get_images as images
import autopy as au
import time

def card_from_filename(filename):
    #print filename
    shapes      = {'d':"diamond",   's':"squiggle", 'o':"oval"}
    fills       = {'f':"full",      's':"striped",  'e':"empty"}
    colors      = {'r':"red",       'g':"green",    'p':"purple"}

    num = filename[0]
    color = filename[1]
    fill = filename[2]
    shape = filename[3]

    #print num, colors[color], fills[fill], shapes[shape]

    return logic.Card(colors[color], shapes[shape], fills[fill], int(num))

short2card = {f:card_from_filename(f) for f in images.combis()}
card2short = {value:key for key, value in short2card.iteritems()}

def find_cards(bmp):
    for card, name in card2short.iteritems():
        img = au.bitmap.Bitmap.open("images/{0}.png".format(name))
        pos = bmp.find_bitmap(img)
        if pos:
            yield card, pos

def find_sets():
    time.sleep(2)
    screen = au.bitmap.capture_screen()
    table = {card:pos for card, pos in find_cards(screen)}
    sets = logic.findsets(table.keys())
    return table, sets

if __name__ == "__main__":
    table, sets = find_sets()

    for s in sets:
        print "-"*10
        for card in s:
            print card
            pos = table[card]
            au.mouse.smooth_move(pos[0], pos[1])
            print "Click:"
            au.mouse.click()
            time.sleep(0.5)
        
