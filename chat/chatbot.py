from models import Vencimento
from ext import db
from datetime import datetime
import openai

# Configura sua chave da API OpenAI
openai.api_key = 'sua-chave-api-openai'  # Use uma variável de ambiente para essa chave

def tela_inicial():
    return (
        "Bem-vindo ao Bemobi! Por favor, escolha uma das opções:\n"
        "1 - Alterar Data de Vencimento\n"
        "2 - Renovação\n"
        "3 - Planos\n"
        "4 - Cancelamento\n"
        "5 - Ouvidoria\n"
        "6 - Conversa Inteligente"
    )

def handle_message(message, user_id):
    message = message.lower()

    # Alterar vencimento de assinatura (o cliente escolhe a data)
    if message in ["1", "vencimento"]:
        return (
            "Você escolheu alterar o vencimento. Escolha uma data para o novo vencimento:\n"
            "1 - Dia 05\n"
            "2 - Dia 15\n"
            "3 - Dia 25"
        )

    # Atualizar o vencimento com base na escolha do cliente
    elif message in ["1", "2", "3"]:
        data_map = {
            "1": "05",
            "2": "15",
            "3": "25"
        }
        dia_vencimento = data_map.get(message, None)
        
        if dia_vencimento:
            # Atualizar o vencimento no banco de dados
            nova_data_vencimento = atualizar_vencimento_no_banco(user_id, dia_vencimento)
            return f"A data de vencimento foi atualizada para o dia {nova_data_vencimento.strftime('%d/%m/%Y')}."
        else:
            return "Opção inválida. Por favor, escolha entre as opções 1, 2 ou 3 para a data de vencimento."

    # Renovação de assinatura
    elif message in ["2", "renovação", "renovar assinatura"]:
        return "Você gostaria de renovar sua assinatura. Confirmar renovação? (sim/voltar)"

    elif message == "sim" and "renovação" in message:
        return "Sua assinatura foi renovada com sucesso!"

    # Informações sobre planos disponíveis
    elif message in ["3", "planos", "planos disponíveis"]:
        return (
            "Oferecemos os seguintes planos:\n"
            "1 - Plano Básico\n"
            "2 - Plano Premium\n"
            "Deseja mais informações sobre um plano específico?"
        )

    # Cancelamento: confirmação
    elif message in ["4", "cancelamento", "cancelar assinatura"]:
        return "Você realmente deseja cancelar sua assinatura? (sim/voltar)"

    elif message == "sim" and "cancelamento" in message:
        return "Sua assinatura foi cancelada com sucesso."

    # Ouvidoria
    elif message in ["5", "ouvidoria"]:
        return "Por favor, entre em contato com nossa ouvidoria pelo telefone 0800-123-456 ou via e-mail: ouvidoria@empresa.com."

    # Integração GPT-3 para conversa inteligente
    elif message in ["6", "conversa inteligente"]:
        return "Digite sua pergunta ou mensagem para iniciar uma conversa inteligente com nossa IA."

    elif message.startswith("conversa"):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()

    elif message == "voltar":
        return tela_inicial()

    # Caso nenhuma opção válida seja inserida
    else:
        return "Opção inválida. Por favor, tente novamente ou digite 'voltar' para retornar à tela inicial."

# Função responsável por atualizar a data de vencimento no banco de dados
def atualizar_vencimento_no_banco(user_id, dia_vencimento):
    # Pegando o mês e o ano atuais
    hoje = datetime.now()
    mes_ano_atual = hoje.strftime('%m/%Y')

    # Criando a nova data de vencimento com base na escolha do cliente
    nova_data = f"{dia_vencimento}/{mes_ano_atual}"
    
    try:
        # Converte a string da nova data para o formato datetime
        data_vencimento = datetime.strptime(nova_data, '%d/%m/%Y')

        # Verifica se o usuário já tem uma data de vencimento no banco
        vencimento_atual = Vencimento.query.filter_by(user_id=user_id).first()

        if vencimento_atual:
            # Atualiza o vencimento existente
            vencimento_atual.data_vencimento = data_vencimento
            db.session.commit()
        else:
            # Cria um novo vencimento para o usuário
            novo_vencimento = Vencimento(user_id=user_id, data_vencimento=data_vencimento)
            db.session.add(novo_vencimento)
            db.session.commit()

        return data_vencimento
    except ValueError:
        return None
