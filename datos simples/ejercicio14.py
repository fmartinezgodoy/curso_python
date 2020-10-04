


precio_pan = 3.49

descuento = 0.6

ventas_barras_viejas = float(input("Ingrese la cantidad de barras vendidas de ayer: "))

costo_neto = precio_pan * ventas_barras_viejas

total_descuento = costo_neto * (1 - descuento)

costo_final = costo_neto - total_descuento

print("Precio sin descuento: " + str(round(costo_neto,1)))
print("Descuento por no ser pan fresco: " + str(round(total_descuento,1)))
print("--------------------------------------")
print("Costo final: " + str(round(costo_final,1)))












