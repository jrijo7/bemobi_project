from models import Vencimento
from ext import db
from datetime import datetime
import openai

# Essa parte eu peguei no gpt, tô tentando entender ela
# Configura sua chave da API OpenAI
openai.api_key = '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'

def handle_message(message, user_id):
    message = message.lower()

    # Cancelamento de assinatura
    if "cancelar assinatura" in message:
        return "Entendido. Você gostaria de cancelar sua assinatura. Por favor, confirme."

    # Alterar vencimento de assinatura
    elif "alterar vencimento" in message:
        try:
            nova_data = message.split("para ")[-1]
            data_vencimento = datetime.strptime(nova_data, '%d/%m/%Y')

            vencimento = Vencimento.query.filter_by(user_id=user_id).first()

            if vencimento:
                vencimento.data_vencimento = data_vencimento
                db.session.commit()
                return f"A data de vencimento foi alterada para {data_vencimento.strftime('%d/%m/%Y')}."
            else:
                novo_vencimento = Vencimento(user_id=user_id, data_vencimento=data_vencimento)
                db.session.add(novo_vencimento)
                db.session.commit()
                return f"A data de vencimento foi definida para {data_vencimento.strftime('%d/%m/%Y')}."
        except ValueError:
            return "Por favor, forneça a data no formato DD/MM/AAAA, por exemplo, 'alterar vencimento para 15/12/2024'."

    # Renovação de assinatura
    elif "renovar assinatura" in message:
        return "Certo! Vamos renovar sua assinatura. Deseja continuar com o mesmo plano ou alterar?"

    # Informações sobre planos disponíveis
    elif "planos disponíveis" in message or "detalhes do plano" in message:
        return "Oferecemos os seguintes planos: Básico e Premium. Cada plano oferece benefícios diferentes. Gostaria de saber mais detalhes sobre um dos planos?"

    # Integração GPT-3
    else:
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=150
        )
        return response.choices[0].text.strip()
