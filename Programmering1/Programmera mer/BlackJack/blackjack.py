import kortlek 

lek = kortlek.skapaKortlek()

print(lek)

# behöver räkna ut värdet på korten  

# handen 
def skrivUtHanden(hand):
    print("Dina kort är: ", end= "")
    for kort in hand:
        print(str(kort)) #fortsätt här

# vinnaren 

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
    else:
        fortsätt = False
