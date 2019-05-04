# encoding: utf-8
"""
Codigo simples que mostra alguns eventos da sua agenda do google,
Criado para entender melhor o codigo e então inclementar em outro projeto
Adaptado por Maurício Mazur do https://developers.google.com/calendar/quickstart/python
O arquivo credentials,json deve ser criado no google, neste link acima
-obs: 2 funções para que se precisar da lista de eventos somente, usa a primeira função, 
a segunda ja retorna um texto organizado com os eventos
-bibliotecas > google-api-python-client, google-auth-httplib2, google-auth-oauthlib
"""

from __future__ import print_function
import sys
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
reload(sys)
sys.setdefaultencoding('utf-8')
#funcao que retorna os eventos
def Eventos_calendario():
    # Configurando a API do google Calendario
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None

    # o arquivo Token.pickle é as credencias do usuario,
    # Criado depois do usuario autorizar a API

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # SE não tiver credenciais validas, vai pedir para se autenticar pelo navegador
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        #salvando as credenciais
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


    # Chamando a API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indica a hora UTC

    #lendo os proximos eventos do calendario
    max_eventos = 3  # <---- Numero de proximos eventos que vai ler
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=max_eventos, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    lista = []
    #se não tiver eventos
    if not events:
        eventos = ('Sua agenda está vazia.../') # mensagem avisando que está vazia
        lista = eventos
        #print(lista)
        return lista
    #criando uma lista de eventos
    for event in events:
        nome_evento = (event['summary']) #,(events['dateTime']) # pega o nome do evento
        dia_evento = str(event['end'].get('dateTime', event['end'].get('date'))) # pega as datas do evento
        #separa dia, ano e mes para formatação
        data = dia_evento
        dia = (data[8:10])
        mes = (data[5:7])
        ano = int(data[0:4])
        data_do_evento = ("%s/%s/%s" %(dia, mes, ano))
        #organiza o evento
        eventos = ("%s em %s" %(nome_evento, data_do_evento))
        #adiciona o eventos em uma lista
        lista.append(eventos)
        #da pra imprimir a lista, ou retornar ela da função
        #print(eventos)
    return lista

def mostrar_eventos():
    # função que retorna um texto com os eventos
    lista_eventos = Eventos_calendario() # <- pega a lista de eventos
    msg_eventos = ("") # <- cria uma varialvel
    virgula = 0 # <- so pra controlar a virgula apos cada evento
    for lista_eventos in lista_eventos:
        if virgula == 0:
            virgula += 1
            msg_eventos += lista_eventos
        else:
            msg_eventos += ", "
            msg_eventos += lista_eventos
    final = "Seus proximos eventos são: %s" % msg_eventos
    return final

eventos = mostrar_eventos()
print(eventos)
