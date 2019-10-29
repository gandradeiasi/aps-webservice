from flask import Flask, request

Eag = 0.0176
Een = 0.11
Eon = 1.28
Eme = 3.16
Eca = 0.19
Emo = 0.07

@app.route("/calcularPegada")
def calcularPegada():
    m3Mes = request.args.get("m3Mes")
    pessoas = request.args.get("pessoas")
    kwh = request.args.get("kwh")
    horaDiaEnergia = request.args.get("horaDiaEnergia")
    kmCarroDia = request.args.get("kmCarroDia")
    kmMotoDia = request.args.get("kmMotoDia")
    kmOnibusDia = request.args.get("kmOnibusDia")
    kmMetroDia = request.args.get("kmOnibusDia")
    
    return (m3Mes * Eag) / pessoas + (kwh * horaDiaEnergia * 30 * Een) / pessoas + (30 * (kmCarroDia * Eca + kmMotoDia * Emo + kmMetroDia * Eme + kmOnibusDia + Eon))
