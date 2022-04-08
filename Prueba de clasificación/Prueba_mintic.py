import csv
import math

def new_csv():
    indice=0
    with open('analisis_bitcoin.csv','w', newline='') as file:
                    headers = ['Indice', 'Fecha', 'Open','Close','Variacion_diaria','Descripcion']
                    writer = csv.DictWriter(file, delimiter=';', lineterminator='\n',fieldnames=headers)
                    writer.writeheader()

                    with open('BTC-USD.csv','r') as bitcoin_data:
                        lector=csv.reader(bitcoin_data, delimiter=",")
                        next(lector, None)
                        for fila in lector:
                            Fecha=fila[0]
                            Open= float(fila[1])
                            Close=float(fila[4])
                            Variacion_diaria=(Close-Open)

                            if Variacion_diaria > 0:
                                Descripcion="Sube"
                            elif Variacion_diaria==0:
                                Descripcion="Estable"
                            else:
                                Descripcion="Baja"

                            writer.writerow({'Indice': indice, 'Fecha': Fecha, 'Open': float(Open),'Close': Close,'Variacion_diaria': Variacion_diaria,'Descripcion': Descripcion})
                            indice+=1

new_csv()

with open('analisis_bitcoin.csv','r') as data:
    csv_reader=csv.reader(data, delimiter=";")
    line_count=0


    variacion_diaria=[]
    id_max=0


    for row in csv_reader:
        if line_count == 0:
            #print(f'Los nombres de las columnas son: {",".join(row)}')
            line_count += 1
        else:
            #print(f'Fecha {row[0]} Valor Open {row[2]}')
            line_count += 1
            variacion_diaria.append(float(row[4]))

    variacion_diaria_media=sum(variacion_diaria)/len(variacion_diaria)




with open('BTC-USD.csv','r') as data:
    reader_csv=csv.reader(data, delimiter=",")
    count_line=0
    fecha_mayor_precio=0
    mayor_precio= -math.inf
    fecha_menor_precio=0
    menor_precio=math.inf

    for Fila in reader_csv:
        if count_line==0:
            print(f'Los nombres de las columnas son: {",".join(Fila)}')
            count_line += 1
        else:
            count_line+=1
            if float(Fila[2]) > mayor_precio:
                fecha_mayor_precio, mayor_precio= Fila[0],float(Fila[2])

            elif float(Fila[3]) < menor_precio:
                fecha_menor_precio,menor_precio= Fila[0], float(Fila[3])

print(f'fecha_menor_precio {fecha_menor_precio}')
print(f'menor_precio {menor_precio}')
print(f'fecha_mayor_precio {fecha_mayor_precio}')
print(f'mayor_precio {mayor_precio}')
print(f'promedio {variacion_diaria_media}')
