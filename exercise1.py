def cagr_berechnung(ak, ek, t):
    if ak <= 0 or t <= 0:
        return "Anfangskapital und Jahre müssen größer als 0 sein."
    
    cagr = (ek / ak) ** (1 / t) - 1
    return cagr

cagr = cagr_berechnung(120, 700, 30)

print(120 * (1 * cagr)**30)

