#Redigeringslogg:
#2023 - Emil Johnsen
import matplotlib.pyplot as plt
import numpy as np

filename = 'data/4a' #Skriv deres filnavn inn her!

# !! - HERFRA TRENGER DERE IKKE Å GJØRE NOEN ENDRINGER - !!

ventilAapning = []
likePros = []
lineaer = []
hurtigAapnende = []
#åpner fila
file = open(filename, "r")
for data in file:
    data = data.replace(",",".")
    data = data.split()

    # print(data[1])
    # ventilAapning.append(float(data[0]))
    # likePros.append(float(data[1]))
    # lineaer.append(float(data[4]))
    # hurtigAapnende.append(float(data[7]))
    
    ventilAapning.append(float(data[0]))
    likePros.append(float(data[1]) / np.sqrt(float(data[2])))
    lineaer.append(float(data[4]) / np.sqrt(float(data[5])))
    hurtigAapnende.append(float(data[7]) / np.sqrt(float(data[8])))


file.close()
plt.plot(ventilAapning,likePros,label="Likeprosentlig")
plt.plot(ventilAapning,lineaer,label="Lineær")
plt.plot(ventilAapning,hurtigAapnende,label="Hurtigåpnede")
plt.xlabel("Ventilåpning[%]")
plt.ylabel("Flow [l/h]")
plt.legend()
plt.show()
