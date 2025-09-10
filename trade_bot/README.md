# 🐍 AI Trading Bot

Um **Trading Bot com interface gráfica em Tkinter** que utiliza a API da **Alpaca** para negociação automatizada e integração com o **OpenAI GPT** para análise do portfólio.

---

## 🚀 Funcionalidades

- 📈 **Gerenciamento de Carteira**  
  - Consulta posições abertas na corretora (Alpaca).  
  - Exibe preço de entrada, preço atual, stop loss e take profit.  

- 🤖 **Execução Automática de Ordens**  
  - Compra inicial caso não haja posição aberta.  
  - Stop Loss automático (-5%).  
  - Take Profit automático (+10%).  

- 💬 **Integração com IA (ChatGPT)**  
  - Permite enviar mensagens ao ChatGPT para análise do portfólio e ordens abertas.  

- 🖥️ **Interface Gráfica (Tkinter)**  
  - Adicionar e remover ativos.  
  - Ligar/Desligar sistemas individuais por ativo.  
  - Visualizar tabela de ativos monitorados em tempo real.  

- 🔄 **Atualização Automática**  
  - O bot atualiza os preços e executa as regras a cada 5 segundos.  

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (interface gráfica)
- **Alpaca Trade API** (ordens e dados de mercado)
- **OpenAI GPT API** (análise de portfólio com IA)
- **JSON** (armazenamento dos ativos)


<img width="510" height="405" alt="Captura de tela 2025-09-10 151955" src="https://github.com/user-attachments/assets/0d4f18ae-62c8-43ca-94cf-214bd4f0e09c" />

## 📊 Funcionalidades da Interface

- Adicionar Equity → Insere um ativo para monitoramento.
- Tabela de Ativos → Exibe os detalhes do portfólio em tempo real.
- Toggle System → Liga/desliga o sistema de negociação para o ativo selecionado.
- Remove Equity → Remove um ativo do monitoramento.
- Chat com IA → Permite enviar perguntas para análise de portfólio.

## ⚠️ Aviso

Este projeto é educacional e utiliza a API paper trading da Alpaca.
Não utilize com contas reais sem compreender os riscos do mercado financeiro.

## 📜 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e compartilhar.
