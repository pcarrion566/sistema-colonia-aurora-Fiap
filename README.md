# Sistema Inteligente da Colônia Aurora

Este projeto é um sistema integrado em Python desenvolvido para gerenciar e prever o uso de energia em uma colônia autossuficiente, utilizando conceitos de Estruturas de Dados, Lógica de Programação e Modelagem Matemática (Regressão Linear).

## Funcionalidades
1. **Organização de Dados:** Armazena informações climáticas, consumo e capacidade dos sistemas solares e eólicos usando estruturas hierárquicas (dicionários e listas).
2. **Previsão (Regressão Linear):** Utiliza dados históricos de vento e energia (`vento = [8, 10, 12]`, `energia = [20, 25, 30]`) para calcular a inclinação e o intercepto e prever a geração futura baseada no vento atual.
3. **Decisão Lógica:** Aplica regras booleanas para avaliar o contexto da colônia e emitir alertas claros.

## Exemplo de Entrada e Saída

**Entrada do Sistema:**
- Leitura atual do vento: 11
- Geração Solar: 40
- Consumo Atual: 70
- Reserva de Bateria: 45

**Saída Esperada no Terminal:**
```text
Iniciando Sistema da Colônia Aurora...

-> Leitura de vento: 11 | Previsão de geração eólica: 27.5
--- ANÁLISE DE SISTEMA ---
Geração Total: 67.5 | Consumo: 70 | Reserva: 45
-> DECISÃO DO SISTEMA: ALERTA CRÍTICO: consumo maior que geração e bateria baixa. Reduzir sistemas não essenciais!
