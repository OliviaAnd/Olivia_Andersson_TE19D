import random as rnd

# behöver en lista för korten i ens hand 
def skapaKortlek():
    kortnummer = [i for i in range(2,11)] 
    klädkort = ["J", "Q", "K", "A"]
    kortnummer += klädkort
    lek = 4*kortnummer 
    blandaKort(lek)

    return lek
    
# blanda kort 

def blandaKort(lek):
    return rnd.shuffle(lek)
