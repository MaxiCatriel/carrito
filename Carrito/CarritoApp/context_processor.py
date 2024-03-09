def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if request.session.get("carrito", {}):  # Cambiar corchetes por paréntesis
            for key, value in request.session["carrito"].items():  # Cambiar sesion por session y agregar paréntesis a items
                total += float(value["acumulado"])
    return {"total_carrito": total}
