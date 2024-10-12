from datetime import datetime, timedelta

# Função para calcular o próximo vencimento
def calcular_proximo_vencimento(data_inicial, intervalo_dias):
    """
    Calcula a próxima data de vencimento a partir de uma data inicial e um intervalo em dias.
    
    :param data_inicial: Data da última cobrança ou assinatura (datetime object)
    :param intervalo_dias: Intervalo de dias entre os pagamentos (exemplo: 30 dias para mensal)
    :return: Próxima data de vencimento (string no formato DD/MM/AAAA)
    """
    proximo_vencimento = data_inicial + timedelta(days=intervalo_dias)
    return proximo_vencimento.strftime('%d/%m/%Y')

def handle_message(message):
  message = message.lower()

  if "cancelar assinatura" in message:
    return "Entendi, você gostaria de cancelar sua assinatura. Por favor, confirme."
  elif "renovar assinatura" in message:
    return "Certo! Vamos começar o processo de renovação da sua assinatura. Deseja continuar o plano atual ou alterar ?"
  elif "alterar assinatura" in message:
    return "Entendi! Você gostaria de mudar seu plano. Posso te ajudar com isso."
  elif "vencimento de pagamento" in message:
        # Exemplo: última cobrança em 1º de outubro de 2024
    ultima_cobranca = datetime(2024, 10, 1)
    intervalo_mensal = 30  # Intervalo para assinaturas mensais
    proximo_vencimento = calcular_proximo_vencimento(ultima_cobranca, intervalo_mensal)
    return f"Seu próximo pagamento está agendado para {proximo_vencimento}."
  elif "planos disponíveis" in message:
    return "Oferecemos os seguintes planos: Básico, Premium e VIP. Gostaria de saber mais detalhes ?"
  else:
    return "Desculpe, não consegui entender sua solicitação"