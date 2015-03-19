import random
a=print("bem vindo ao pedra papel tesoura spock e lagarto")
b=input("voce gostaria de jogar? ")
if b==("nao"):
    print("tranquilo, tenha uma boa semana")
n1=0
n2=0

if b==("sim"):
    while (n1<3) and (n2<3):
        c=input("o que voce escolhe? ")
        d=random.choice(["pedra", "papel", "tesoura", "spock", "lagarto"])
        if c==("pedra"):
            if d==("pedra"):
                print("ocorreu um empate")
                n1=0
                n2=0
            elif d==("papel"):
                print("voce perdeu")
                n1=0
                n2=n2+1
            elif d==("spock"):
                print("voce perdeu")
                n1=0
                n2=n2+1
            elif d==("tesoura"):
                print("voce ganhou")
                n1=n1+1
                n2=0
            elif d==("lagarto"):
                print("voce ganhou")
                n1=n1+1
                n2=0
                
        if c==("papel"):
           if d==("papel"):
               print("ocorreu um empate")
               n1=0
               n2=0
           elif d==("tesoura"):
                print("voce perdeu")
                n1=0
                n2=n2+1
           elif d==("lagarto"):
                print("voce perdeu")
                n1=0
                n2=n2+1
           elif d==("pedra"):
                print("voce ganhou")
                n1=n1+1
                n2=0
           elif d==("spock"):
                print("voce ganhou")
                n1=n1+1
                n2=0
                
        if c==("tesoura"):
            if d==("tesoura"):
                print("ocorreu um empate")
                n1=0
                n2=0
            elif d==("pedra"):
                print("voce perdeu")
                n1=0
                n2=n2+1
            elif d==("spock"):
                print("voce perdeu")
                n1=0
                n2=n2+1
            elif d==("papel"):
                print("voce ganhou")
                n1=n1+1
                n2=0
            elif d==("lagarto"):
                print("voce ganhou")
                n1=n1+1
                n2=0
            
        if c==("lagarto"):
            if d==("lagarto"):
                print("ocorreu um empate")
                n1=0
                n2=0
            elif d==("pedra"):
                print("voce perdeu")
                n1=0
                n2=n2+1
            elif d==("tesoura"):
                print("voce perdeu")
                n1=0
                n2=n2+1
            elif d==("papel"):
                print("voce ganhou")
                n1=n1+1
                n2=0
            elif d==("spock"):
                print("voce ganhou")
                n1=n1+1
                n2=0
            
        if c==("spock"):
            if d==("spock"):
                print("ocorreu um empate")
                n1=0
                n2=0
            elif d==("papel"):
                print("voce perdeu")
                n1=0
                n2=n2+1
            elif d==("lagarto"):
                print("voce perdeu")
                n1=0
                n2=n2+1
            elif d==("pedra"):
                print("voce ganhou")
                n1=n1+1
                n2=0
            elif d==("tesoura"):
                print("voce ganhou")
                n1=n1+1
                n2=0
    if n1==3:
        print("voce ganhou o jogo, parabens pela conquista")
    elif n2==3:
        print("voce perdeu o jogo, talvez voce ganhe na proxima")
