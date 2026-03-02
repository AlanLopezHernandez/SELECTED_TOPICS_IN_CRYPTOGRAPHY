def es_primo(p):
    # Verificar si p es primo
    if p <= 1:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True


def curva_verificacion(a, b, p):
    # Verificar que la curva elíptica y los parámetros son válidos
    pasos = []

    pasos.append(f"1) Verificar si p = {p} es primo.")

    if not es_primo(p):
        pasos.append(f"{p} no es primo.")
        return {
            "valida": False,
            "discriminante": None,
            "pasos": pasos
        }

    pasos.append(f"    {p} es primo.")

    pasos.append("2) Calcular el discriminante:")
    pasos.append("    Δ = 4a³ + 27b² (mod p)")

    a3 = a**3
    b2 = b**2
    parte1 = 4 * a3
    parte2 = 27 * b2
    parte3 = parte1 + parte2
    discriminante = parte3 % p

    pasos.append("    Sustituir valores:")
    pasos.append(f"    Δ = 4{a}³ + 27{b}² (mod {p})")
    pasos.append(f"    Δ = 4({a3}) + 27({b2}) (mod {p})")
    pasos.append(f"    Δ = {parte1} + {parte2} (mod {p})")
    pasos.append(f"    Δ = {parte3} (mod {p})")
    pasos.append(f"    Δ = {discriminante}")

    if (4 * a**3 + 27 * b**2) % p == 0:
        pasos.append(f"    Δ = {discriminante} = 0 ⇒ La curva es singular (NO válida).")
        return {
        "valida": False,
        "discriminante": discriminante,
        "pasos": pasos
    }
    else:
        pasos.append(f"    Δ = {discriminante} ≠ 0 ⇒ La curva es NO singular (válida).")
        return {
            "valida": True,
            "discriminante": discriminante,
            "pasos": pasos
        }

calcular_punto = lambda x, y, a, b, p: (y**2 % p) == ((x**3 + a * x + b) % p)

def puntos_en_curva(a, b, p):
    # Calcular todos los puntos (x, y) que satisfacen la ecuación de la curva elíptica
    puntos = []
    for x in range(p):
        for y in range(p):
            if calcular_punto(x, y, a, b, p):
                puntos.append((x, y))
    return puntos