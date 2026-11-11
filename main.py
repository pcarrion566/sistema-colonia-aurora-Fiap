# ==========================================
# Sistema Inteligente da Colônia Aurora
# ==========================================

# 1. Estruturação dos Dados da Colônia
dados_colonia = {
    "sistema_energetico": {
        "solar": {"geracao_atual": 40},
        "eolico": {"geracao_atual": 0, "historico_vento": [8, 10, 12], "historico_energia": [20, 25, 30]},
        "reserva_bateria": 45 
    },
    "consumo_atual": 70
}

# 2. Modelagem e Previsão (Regressão Linear Simples)
def prever_geracao_eolica(vento_atual, historico_vento, historico_energia):
    """
    Usa regressão linear simples para prever a geração de energia baseada no vento.
    """
    # Cálculo das médias
    media_vento = sum(historico_vento) / len(historico_vento)
    media_energia = sum(historico_energia) / len(historico_energia)
    
    # Cálculo da inclinação (beta_1) e intercepto (beta_0)
    numerador = sum((v - media_vento) * (e - media_energia) for v, e in zip(historico_vento, historico_energia))
    denominador = sum((v - media_vento) ** 2 for v in historico_vento)
    
    inclinacao = numerador / denominador
    intercepto = media_energia - (inclinacao * media_vento)
    
    # Previsão
    previsao = (inclinacao * vento_atual) + intercepto
    return round(previsao, 1)

# 3. Lógica de Decisão Automática
def analisar_energia(geracao_total, consumo, reserva):
    """
    Aplica regras lógicas booleanas para tomar decisões sobre a energia.
    """
    print(f"--- ANÁLISE DE SISTEMA ---")
    print(f"Geração Total: {geracao_total} | Consumo: {consumo} | Reserva: {reserva}")
    
    if geracao_total > consumo:
        return "SUGESTÃO: armazenar energia excedente nas baterias."
    
    elif consumo > geracao_total and reserva < 50:
        return "ALERTA CRÍTICO: consumo maior que geração e bateria baixa. Reduzir sistemas não essenciais!"
        
    elif consumo > geracao_total:
        return "ALERTA: consumo maior que geração. Utilizando reserva de energia."
        
    else:
        return "STATUS: Sistema equilibrado."

# ==========================================
# Execução do Sistema (Simulação)
# ==========================================
def executar_sistema():
    print("Iniciando Sistema da Colônia Aurora...\n")
    
    # Prever energia eólica com base em uma nova leitura de vento (ex: 11)
    vento_leitura_atual = 11
    hist_vento = dados_colonia["sistema_energetico"]["eolico"]["historico_vento"]
    hist_energia = dados_colonia["sistema_energetico"]["eolico"]["historico_energia"]
    
    previsao_eolica = prever_geracao_eolica(vento_leitura_atual, hist_vento, hist_energia)
    dados_colonia["sistema_energetico"]["eolico"]["geracao_atual"] = previsao_eolica
    print(f"-> Leitura de vento: {vento_leitura_atual} | Previsão de geração eólica: {previsao_eolica}")
    
    # Calcular geração total (Solar + Eólica prevista)
    geracao_solar = dados_colonia["sistema_energetico"]["solar"]["geracao_atual"]
    geracao_total = geracao_solar + previsao_eolica
    
    # Tomar decisão com base nos dados
    consumo = dados_colonia["consumo_atual"]
    reserva = dados_colonia["sistema_energetico"]["reserva_bateria"]
    
    decisao = analisar_energia(geracao_total, consumo, reserva)
    print(f"-> DECISÃO DO SISTEMA: {decisao}\n")

# Rodar o programa
if __name__ == "__main__":
    executar_sistema()
