#Redigeringslogg:
#2023 - Emil Johnsen
import matplotlib.pyplot as plt


filename = 'data/3a' #Skriv deres filnavn inn her!

# !! - HERFRA TRENGER DERE IKKE Å GJØRE NOEN ENDRINGER - !!

#def variabler
timeStep = []
turbinRef = []
turbinFIT104A = []
VA_FIT104B = []
elmag_FIT104C = []
vortex_FIT104D = []
coriolis_FIT104E = []
orfice_FIT104F = []
t = 0

#åpner fila og leser fila
file = open(filename, "r")
for data in file:
    data = data.replace(",",".")
    data = data.split()

    timeStep.append(t)
    turbinRef.append(float(data[2]))
    turbinFIT104A.append(float(data[6]))
    VA_FIT104B.append(float(data[7]))
    elmag_FIT104C.append(float(data[8]))
    vortex_FIT104D.append(float(data[9]))
    coriolis_FIT104E.append(float(data[10]))
    orfice_FIT104F.append(float(data[11]))
    t = t+1
file.close()

plt.plot(timeStep,turbinRef, label="Turbin Ref")
plt.plot(timeStep,turbinFIT104A, label="Turbin FIT-104A")
plt.plot(timeStep,VA_FIT104B,label="VA FIT-104B")
plt.plot(timeStep,elmag_FIT104C,label="Elmag FIT-104C")
plt.plot(timeStep,vortex_FIT104D,label="Vortex FIT-104D",linestyle="dashed")
plt.plot(timeStep,coriolis_FIT104E,label="Coriolis FIT-104E",linestyle="dashed")
plt.plot(timeStep,orfice_FIT104F,label="Orfice FIT-104F",linestyle="dashed")
plt.xlabel("Timestep")
plt.ylabel("Flow [l/h]")
plt.legend()
plt.show()