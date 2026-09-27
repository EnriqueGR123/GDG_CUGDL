'''
Simulador de procesamiento de sensores por lotes

Tienes una lista de lecturas de un sensor (por ejemplo, temperatura de un dispositivo
biomédico o valores de un pipeline de datos). Vas a procesarlas en lotes , 
clasificarlas, saltarte las inválidas, y detener todo si aparece una lectura crítica.

Valor negativo: inválido
Valor entre 0 y 50 : normal
Valor entre 51 y 90: alerta
Valor mayor a 90:  crítico
'''

values = [-1,-3,5,10,51,91,-2,10,20,33,-33,1]

normal = []
alerta = []
for value in values:
        if value < 0:
            continue
        elif value >= 0 and value <=50:
            #print(f'Valor {value} normal')
            normal.append(value)
        elif value >= 51 and value <90:
            #print(f'Valor {value} alerta')
            alerta.append(value)
        elif value >= 91:
            print(f'Valor critico encnontrado: {value}')
            break
print(f'Valores normales {normal}')
print(f'Valores alerta {alerta}')





'''
id_producto: Tipo entero (int), Llave Primaria (PK).
nombre: Tipo texto (varchar de 100 caracteres).
precio: Tipo decimal (decimal(10,2)).
stock: Tipo entero (int).
categoria_id: Tipo entero (int), Llave Foránea (FK) que apunta a la columna categoria_id de la tabla categorias.

'''