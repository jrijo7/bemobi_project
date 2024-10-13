from flask import Blueprint, request, jsonify
from chat.chatbot import handle_message

api = Blueprint('api', __name__)

@api.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    user_id = data.get('user_id')  # Identificar usuário

    # Processar menssagem
    response = handle_message(user_message, user_id)

    # Resposta em formato JSON
    return jsonify({'response': response})

