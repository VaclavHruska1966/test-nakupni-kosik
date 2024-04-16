zbozi = ["jablko", "hruška", "banán", "pomeranč", "mrkev"]
kosik = []

def kupovani(koupe):
    for x in range(len(koupe)): 
        print(f"{x+1}: {koupe[x]}")
        
kupovani(zbozi)
while(True):
    kosik_plus = input("Zadejte potravinu, kterou chcete přidat:     ")


    if kosik_plus:= "jablko": 
        kosik.append(kosik_plus)
        zbozi.remove("jablko")
        
    
    
    elif kosik_plus:= "hruška": 
        zbozi.append(kosik_plus)
        zbozi.remove("hruška")

    elif kosik_plus:= "banán": 
        zbozi.append(kosik_plus)
        zbozi.remove("banán")
    
    elif kosik_plus:= "pomeranč": 
        zbozi.append(kosik_plus)
        zbozi.remove("pomeranč")
    
    elif kosik_plus:= "mrkev": 
        zbozi.append(kosik_plus)
        zbozi.remove("mrkev")
    
    elif kosik_plus:= "1": 
        zbozi.append(kosik_plus)
        zbozi.remove("1")
    
    elif kosik_plus:= "2": 
        zbozi.append(kosik_plus)
        zbozi.remove("2")
    
    elif kosik_plus:= "3": 
        zbozi.append(kosik_plus)
        zbozi.remove("3")
    
    elif kosik_plus:= "4": 
        zbozi.append(kosik_plus)
        zbozi.remove("4")
    
    elif kosik_plus:= "5": 
        zbozi.append(kosik_plus)
        zbozi.remove("5")
    
    elif kosik_plus:= "dost": 
        zbozi.append(kosik_plus)
        zbozi.remove("5")
    
    
    
    
    else:
        print("co děláš")

    kupovani(zbozi)
    print(kosik)

    