staedte = ["Rome", "Paris", "London", "Berlin"]

# Berlin aus der Liste entfernen
staedte.remove("Berlin")

# Madrid hinzufügen (Am ende)
staedte.append("Madrid")

# Amsterdam hinter Rom einfügen
staedte.insert(staedte.index("Rome") + 1, "Amsterdam")

# Sortieren alphabetisch
staedte.sort()

# Ausgabe iste
print(staedte)
