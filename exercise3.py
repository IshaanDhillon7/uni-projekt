def steigung_funktion(meine_liste):
    x1 = meine_liste[0] # 0 ist ein Index 
    y1 = meine_liste[1]
    x2 = meine_liste[2]
    y2 = meine_liste[3]
    delta_x = x2 - x1 
    delta_y = y2 - y1 
    
    if delta_x == 0:
        print("Die Steigung ist nicht definiert")
    else: 
        steigung = delta_y / delta_x #Zwischen speichern durch steigung 
        return steigung
    
test_liste = [4,3,4,7]

print(steigung_funktion(meine_liste = test_liste)) # Oder in die Konsole schreiben


#Übung Listen
staedte = ["Rome", "Paris", "London", "Berlin"]

# Berlin aus der Liste entfernen
staedte.remove("Berlin")

# Madrid hinzufügen (Am ende)
staedte.append("Madrid")

# Amsterdam hinter Rom einfügen
staedte.insert(1, "Amsterdam")

# Sortieren alphabetisch
staedte.sort()

# Ausgabe iste
print(staedte)