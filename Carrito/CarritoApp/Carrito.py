class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            
            
    def agregar(self, producto) :
        id = str(producto.id)
        if id not in self.carrito.keys( ) :  # Si el producto no está en el carrito lo agrego con la cantidad solicitada (1)
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": float(producto.precio), 
                "acumulado": float(producto.precio),  # Convertir a flotante para operaciones matemáticas
                "cantidad":1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]['acumulado'] += float(producto.precio)
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
        
    def  eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
            
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]['acumulado'] -= float(producto.precio)
            if self.carrito[id]['cantidad'] <= 0: self.eliminar(producto)
            self.guardar_carrito()
        
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
        
    def obtener_total(self):
        total = 0
        for item_id, item_info in self.carrito.items():
            total += float(item_info['acumulado'])
        return total