from django.shortcuts import render
from .elliptic_curve import curva_verificacion, puntos_en_curva

def index(request):
    resultado = None

    if request.method == "POST":
        try:
            a = int(request.POST.get("a"))
            b = int(request.POST.get("b"))
            p = int(request.POST.get("p"))

            resultado = curva_verificacion(a, b, p)

            # Si es válida, agregar puntos al mismo diccionario
            if resultado["valida"]:
                resultado["puntos"] = puntos_en_curva(a, b, p)
            else:
                resultado["puntos"] = []

        except (TypeError, ValueError):
            resultado = {
                "valida": False,
                "pasos": ["Error: los valores ingresados no son válidos."],
                "puntos": []
            }

    return render(request, "curvas/index.html", {
        "resultado": resultado
    })