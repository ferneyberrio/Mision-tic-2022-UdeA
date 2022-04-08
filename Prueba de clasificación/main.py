from ast import With
import csv
import json
def descripcion(parametro):
    if parametro > 0:
        return "Sube"
    elif parametro < 0:
        return "Baja"
    else:
        return "Estable"

def escribir_csv(parametro):  
    archivo = 'analisis_bitcoin.csv'
    csv=open(archivo,'w')
    tituloR = "Indice;Fecha;Open;Close;Variacion_diaria;Descripcion"
    csv.write(tituloR)
    csv.write('\n')
    for elmento in parametro:
          elmento = elmento.rstrip()
          separador ="-"
          lista = elmento.split(separador)
          #Indice = parametro["Indice"]  
          #Fecha = parametro["Fecha"]   
          #Open = parametro["Open"]
          #Close = parametro["Close"]
          #Varuiacion_diaria = parametro["Variacion_diaria"]
          #Descripcion = parametro["Descripcion"]
          #filas = Indice+';'+Fecha+';'+Open+';'+Close+';'+Varuiacion_diaria+';'+Descripcion+"\n"
          print(lista)
          #csv.write(filas)
        


    """
     with open('analisis_bitcoin.csv', 'w',newline='' ) as csvfile:
        fieldnames = ['Indice', 'Fecha', 'Open', 'Close', 'Variacion_diaria', 'Descripcion']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for key in parametro:          
         Indice = parametro['Indice']         
         fecha = parametro['Fecha']
         Open = parametro['Open']
         Close = parametro['Close']
         Variacion_diaria = parametro['Variacion_diaria']
         Descripcion = parametro['Descripcion']
         writer.writerows({'Indice': Indice, 'Fecha': fecha, 'Open': Open, 'Close': Close, 'Variacion_diaria': Variacion_diaria, 'Descripcion': Descripcion})
    """     
 

def leer_csv():
    nombre_archivo="BTC-USD.csv"
    with open(nombre_archivo, 'r') as archivo:
         next(archivo,None)
         for index,linea in enumerate(archivo):
             linea = linea.rstrip()
             separador =","
             lista = linea.split(separador)
             Indice = str(index)
             Fecha = lista[0]
             Open= lista[1]
             Close= lista[4]
             Variacion_diaria=float(Close)-float(Open)
             Variacion_diaria_str=str(Variacion_diaria)
             descrip = descripcion(Variacion_diaria)
          

             result = (Indice+','+Fecha+','+Open+','+Close+','+Variacion_diaria_str+','+descrip+'-')
            
             #result = {"Indice":Indice,"Fecha":Fecha,"Open":Open,"Close":Close,"Variacion_diaria":Variacion_diaria_str,"Descripcion":descrip}
             escribir_csv(result)

             
   


def solucion():
    leer_csv()
     

solucion()