def vokon_zählen(x):
    x_lower = x.lower()
    x_lower_list = list(x_lower)
    vokalen = "aeiou" 
    
    v = [] # Hier speichern wir die Vokale 
    k = [] # Hier speichern wir alle Buchstaben 
    
    for b in x_lower_list:
        #Hier pr+fen wir ob b ein Buchstabe ist 
        if b.isalpha():  
            k.append(b)
        #Hier prüfen wir ob b ein Vokal ist
        if b in vokalen: 
            v.append(b)
            
    return f"Im String {x} gibt es {len(v)} Vokale und {len(k)-len(v)} Konsonanten"
            
    #return [len(v), len(k)-len(v)]

print(vokon_zählen("Berlin I love you!"))
