import kortlek 

print(lek)

# behöver räkna ut värdet på korten  
def räknaPoäng(hand):
    poäng = 0 
    for kort in hand:
        if kort == "j" or kort == "Q" or kort == "K":
            poäng += 10
        elif kort == "A" and poäng < 11:
            poäng += 11
        elif kort == "A" and poäng >= 11:
            poäng += 1
        else:
            poäng += kort
    return poäng 

# handen 
def skrivUtHanden(hand):
    print("Dina kort är: ", end= "")
    for kort in hand:
        print(str(kort) + ", ", end="") 

# vinnaren 
def checkaVinnare(hand, dealer):
    dealerPoäng = räknaPoäng(dealer)
    spelarePoäng = ränkaPoäng(hand)

    if spelarePoäng == 21:
        print("Blackjack")
    elif spelarePoäng <= dealerPoäng or spelarePoäng > 21:
        print("Huset vinner")
    else:
        print("Du vinner")


# spel-loop 
    while True:
        spela = input("Vill du spela Black Jack? (j för ja, annan tangent för nej)")

        if spela != "j":
            break
        
        lek = kortlek.skapaKortlek()

        print(lek)
        # dealer ger två kort 
        dealer = [lek.pop(0),lek.pop(0)]
        print(f"Dealerns första kort är {dealer[0]}")
        
        hand = {lek.pop(0), lek.pop(0)}
        print(f"Dina första två kort är: {hand[0] och hand[1]}")

        fortsätt = True

    # göra val (få fler kort, stanna)
    while fortsätt:
        takort = input("Ta nytt kort? (j för ja, annan tangent för att stanna)")

        if takort == "j":
            hand.append(lek.pop(0))
            skrivUtHanden(hand)
        else:
            fortsätt = False
    print(f"dina poäng är {räknaPoäng(hand)}")

print("Spelet slutar, ha de gött haj")