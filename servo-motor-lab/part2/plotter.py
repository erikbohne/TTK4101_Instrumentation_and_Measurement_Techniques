import pandas as pd
import matplotlib.pyplot as plt
import os

path = "data"

# finner alle filer i mappen
files = os.listdir(path)

# Fjerner filer som ikke er csv
files = [file for file in files if file.endswith('.csv')]

# Itererer over alle filene
for file in files:
    # Henter ut filnavn
    fileName = file.split('.')[0]
    # Leser csv-fila
    data1 = pd.read_csv(f"{path}/{file}")

    # Hent ut måleserie og tid, konverter til numpy
    time = data1.iloc[:,0].to_numpy()
    signal = data1.iloc[:,1].to_numpy()

    # 1) Sett tidsaksen til å starte på 0
    # 2) Pass på at tidsaksen er i millisekunder (datapunktene vi henter ut fra filene er i sekunder)
    time = (time - time[0]) * 1000

    # Plot og lagre data
    fig,a = plt.subplots(1,1)
    time_subsampled = time[::10]
    signal_subsampled = signal[::10]
    a.plot(time_subsampled, signal_subsampled)
    a.set_xlabel('t [ms]')
    a.set_ylabel('V [V]')
    plt.savefig(f"figures/{fileName}.png")
    plt.close()