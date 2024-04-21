#carregando os módulos para a execução do chat
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# isso aqui só precisa para corrigir o bug
from spacy.cli import download

#biblioteca da voz
import pyttsx3
#carrega a lcasse e inicia
speak =  pyttsx3.init('sapi5')

download("en_core_web_sm")


#classe obrigatória
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
# Create a new chat bot named Charlie
chatbot = ChatBot('Jarvis',tagger_language=ENGSM)

trainer = ListTrainer(chatbot)

conversa = trainer.train([
    "Oi, tudo bem com você?",
    "Em que posso ajuda -lo?.",
    "Desculpa, pode repetir por favor!."
])


while True:
    msg = input('Pergunte ao Jarvis')
    if msg =="parar":
        break

    response = chatbot.get_response(msg)

    #seta a string para ser falada
    speak.say(response)

    #espera para executar
    speak.runAndWait()
    print(response)