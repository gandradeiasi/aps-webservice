from flask import Flask, request

app = Flask(__name__)

Eag = 0.0176
Een = 0.11
Eon = 1.28
Eme = 3.16
Eca = 0.19
Emo = 0.07

@app.route("/calcularPegada")
def calcularPegada():
    try:
        m3Mes = float(request.args.get("m3Mes"))
        pessoas = float(request.args.get("pessoas") if parametroValido(request.args.get("pessoas")) else 1)
        kwh = float(request.args.get("kwh"))
        horaDiaEnergia = float(request.args.get("horaDiaEnergia"))
        kmCarroDia = float(request.args.get("kmCarroDia") if parametroValido(request.args.get("kmCarroDia")) else 0)
        kmMotoDia = float(request.args.get("kmMotoDia") if parametroValido(request.args.get("kmMotoDia")) else 0)
        kmOnibusDia = float(request.args.get("kmOnibusDia") if parametroValido(request.args.get("kmOnibusDia")) else 0)
        kmMetroDia = float(request.args.get("kmMetroDia") if parametroValido(request.args.get("kmMetroDia")) else 0)

        print("Metro Cubico por Mes: " + str(m3Mes))
        print("Pessoas: " + str(pessoas))
        print("kWh: " + str(kwh))
        print("Hora de Energia Por dia: " + str(horaDiaEnergia))
        print("Kilometro Carro Dia: " + str(kmCarroDia))
        print("Kilometro Moto Dia: " + str(kmMotoDia))
        print("Kilometro Onibus Dia: " + str(kmOnibusDia))
        print("Kilometro Metro Dia: " + str(kmMetroDia))
    
        return str((m3Mes * Eag) / pessoas + (kwh * horaDiaEnergia * 30 * Een) / pessoas + (30 * (kmCarroDia * Eca + kmMotoDia * Emo + kmMetroDia * Eme + kmOnibusDia + Eon)))
    except:
        return "Certifique-se de que todos os parâmetros foram preenchidos corretamente"

def parametroValido(string):
    if (string == None):
         return False
    if (string == ''):
         return False
    if (string == ""):
         return False
    return True