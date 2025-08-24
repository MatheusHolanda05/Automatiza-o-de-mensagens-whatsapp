# Automação de Envio de Mensagens para o WhatsApp

Este projeto permite o envio automatizado de mensagens para múltiplos contatos no WhatsApp através de uma planilha Excel.

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Google Chrome instalado
- Conta no WhatsApp Web

## 🛠️ Instalação

1. Clone este repositório:
```bash
git clone https://github.com/MatheusHolanda05/Automatizacao-de-envio-de-mensagens-para-o-whatsapp.git
cd Automatizacao-de-envio-de-mensagens-para-o-whatsapp

2. Instale as dependências:
pip install -r requirements.txt

📦 Dependências
As principais bibliotecas utilizadas são:

pandas

selenium

urllib3

📊 Estrutura do Arquivo Excel
Crie um arquivo Enviar.xlsx com a seguinte estrutura:

Pessoa	Número	Mensagem
Nome1	5511999999999	Mensagem 1
Nome2	5511888888888	Mensagem 2
Importante: O número deve estar no formato internacional (código do país + DDD + número), sem espaços ou caracteres especiais.

🚀 Como Usar
Prepare sua planilha Enviar.xlsx com os contatos e mensagens

Execute o script:

bash
python Enviar_mensagens_WhatsApp.py
Escaneie o código QR do WhatsApp Web quando solicitado

O script enviará as mensagens automaticamente para todos os contatos da lista

⚠️ Observações
Mantenha o navegador aberto durante a execução do script

O WhatsApp pode limitar o número de mensagens enviadas em um curto período

Use esta ferramenta com responsabilidade e respeite as políticas do WhatsApp

📝 Licença
Este projeto é para fins educacionais. Use por sua própria conta e risco.