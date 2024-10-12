from flask import Blueprint, request, jsonify
from chat.chatbot import handle_message

# inicializa o blueprint da API
api = Blueprint('api', __name__)

@api.route('/chat', methods=['POST'])

def chat():
  data = request.json
  user_message = data.get('message')

  response = handle_message(user_message)

  return jsonify({'response': response})