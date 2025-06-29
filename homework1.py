import plotly.express as px 
from plotly.offline import plot 
import pandas as pd 

def spar_funktion(AK,SR,i,lz):
    
    kapital = AK #Anfangskapital 
    sparen = AK #Anfangskapital 
    zinsen = 0 #Zinsen am Anfang 
    
    gesamt_kapital = []
    gesamt_zinsen = []
    gesamt_einzahlung = []
    

    for k in range(1, lz, 1):
    #zinsberechnung 
        zinsen = zinsen + i* kapital
    # Einzahlungen 
        sparen = sparen + SR 
    #Gesamtkapital (Nur zum prüfen)
        kapital = kapital * (1+i) + SR
    #Werte in die leere Liste hinzufügen
        gesamt_kapital.append(round(kapital, 2))
        gesamt_zinsen.append(round(zinsen, 2))
        gesamt_einzahlung.append(round(sparen,2))
    
    return [gesamt_kapital, gesamt_einzahlung, gesamt_zinsen]

ergebnisse = spar_funktion(AK = 10000, 
              SR = 1000, 
              i = 0.01, 
              lz = 10)

# Dictionary erstellen 
d = {"Zeit": range (1, 11),
     "Zinsen": ergebnisse[2],
     "Einzahlungen": ergebnisse[1]
     
     }

#DataFrame mit Pandas erstellen
df = pd.DataFrame(data = d)

# Zum Schluss, Balkendiagramm mit Plotly
fig = px.bar(df, 
             x = "Zeit", 
             y = ["Einzahlungen", "Zinsen"],
             labels = {"value" : "Euro",
                       "Zeit": "Jahr",
                       "variable": "Kapital", 
                       
                 },
             title = "Sparplan")

plot(fig, filename = "homework1.html")