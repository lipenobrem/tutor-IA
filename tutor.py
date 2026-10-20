import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def obter_resposta_tutor(historico, pergunta):
    """
    Realiza a chamada direta para a API do Gemini.
    """
    instrucao = (
        "Você é um tutor de Português e Matemática altamente didático. "
        "Não dê apenas a resposta final. Explique o conceito. "
        "Para Matemática: use passo a passo e LaTeX ($). "
        "Para Português: use exemplos e regras gramaticais claras."
    )
 
    model = genai.GenerativeModel(
        model_name="gemini-flash-latest",
        system_instruction=instrucao
    )

    chat = model.start_chat(history=historico)
 
    response = chat.send_message(pergunta)
    return response.text, chat.history