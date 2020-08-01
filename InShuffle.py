def inShuffle(deck, newdeck):
    # Shuffle the deck by interlacing top half with bottom
    for i in range(len(deck) // 2):
        newdeck.append(deck[i + (len(deck) // 2)])
        newdeck.append(deck[i])

    return newdeck


def requirement1(deck):
    # Shuffle 7 times
    for i in range(7):
        newdeck = []
        inShuffle(deck, newdeck)
        deck = newdeck

    # since python follows 0 based index, to get 1 based index, add 1
    return newdeck.index(1) + 1


def requirement2(deck, count):
    deckCopy = deck
    while True:
        count += 1
        newdeck = []
        inShuffle(deck, newdeck)
        deck = newdeck

        # If card 1 is at last position, break
        if newdeck[-1] == deckCopy[0]:
            break
    return count


def requirement3(deck, count):
    while True:
        count += 1
        newdeck = []
        inShuffle(deck, newdeck)
        deck = newdeck

        # Check if 1 occurs after 52 or 52 occurs after 1
        if ((newdeck.index(1) + 1) == newdeck.index(52)) or \
                ((newdeck.index(52) + 1) == newdeck.index(1)):
            break

    return count

def main():

    DeckSize = 52
    deck = [(i + 1) for i in range(DeckSize)]
    count = 0

    print("\n After 7 shuffles, the 1st card is at {} position"
          .format(requirement1(deck)))
    print("\n For the top card to becom the bottom card, one must shuffle {} times"
          .format(requirement2(deck, count)))
    print("\n The first and last cards touch after {} shuffles"
          .format(requirement3(deck, count)))


if __name__ == '__main__':
    main()
