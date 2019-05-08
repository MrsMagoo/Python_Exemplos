# encoding: utf-8
'''
Criado para entender o uso da Biblioteca Telepot, a qual pode-se programar um bot para telegram
Feito como base para poder inclementar em outro projeto, 
Criado Por Maurício Mazur
''''
import telepot, time
#---------telegram------------#
id_bot = ("id") #Mudar para id do bot, entre aspas!!! 
telegram = telepot.Bot(id_bot) #< Id do bot do Telegram


def recebendo_msg(msg):  # recebe e manda a msg
    tipomsg, tipoChat, chatID = telepot.glance(msg)
    print(chatID) # mostra o id de quem mandou msg
    resposta = ("teste") # mensagem a ser enviada
    print(">", resposta)
    telegram.sendMessage(chatID, resposta) # envia a resposta para o id que mandou a mensgem
    return resposta

def enviar_mensagem(id, mensagem): #função que simples para enviar uma msg pra expecificamente alguém
    telegram.sendMessage(id, mensagem)
    print(id, ' > %s' %mensagem)

telegram.message_loop(recebendo_msg) #loop para receber mensagens
while True:#loop para ficar rodando
    time.sleep(1)
