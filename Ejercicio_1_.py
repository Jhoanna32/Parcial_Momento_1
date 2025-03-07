Compra= int(input("Ingrese el monto de la compra: "))
if Compra<50:
    print("No hay descuento")
elif 50 >= Compra <= 100:
    descuento= Compra*0.05
    print("El descuento es del 5%")
elif Compra > 100:
    descuento=  Compra*0.10
    #("El descuento es del 10%")
    
Total= Compra-descuento

print(f"Descuento aplicado: ${descuento}")
print(f"Total a pagar: ${Total}")