# encoding: utf-8
"""
Codigo simples que mostra alguns eventos da sua agenda do google,
Criado para entender melhor o codigo e então inclementar em outro projeto
Adaptado por Maurício Mazur do https://developers.google.com/calendar/quickstart/python
O arquivo credentials,json deve ser criado no google, neste link acima


"""
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#funcao que retorna 3 eventos
def Eventos_calendario():
    # Configurando a API do google Calendario
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None

    # o arquivo Token.pickle é as credencias do usuario,
    # Criado depois do usuario autorizar a API
    

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # SE não tiver credenciais validas, logar
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
        print(lista)
        return lista
    '''
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    '''
    #criando uma lista de eventos
    for event in events:
        nome_evento = (event['summary']) #,(events['dateTime']) # pega o nome do evento
        dia_evento = str(event['end'].get('dateTime', event['end'].get('date'))) # pega as datas do evento
        #separa dia, ano e mes para formatação
        data = dia_evento
        dia = (data[8:10])
        mes = (data[5:7])
        ano = int(data[0:4])
        data_do_evento = ("%s-%s-%s" %(dia, mes, ano))
        #organiza o evento
        eventos = ("%s dia %s" %(nome_evento, data_do_evento))
        #adiciona o eventos em uma lista
        lista.append(eventos)
        #da pra imprimir a lista, ou retornar ela da função
        print(eventos)
    return lista

evento = (Eventos_calendario())
print(evento)
