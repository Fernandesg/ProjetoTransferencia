import pygetwindow
import pyautogui
import PySimpleGUIQt as sg
import smtplib
from time import sleep

credencialEmail = open('credencialEmail.txt', 'r')
loginEmail = []

for linhas in credencialEmail:
    linhas = linhas.strip()
    loginEmail.append(linhas)
usuario_email = loginEmail[0][17:-1]
senha_email = loginEmail[1][15:-1]
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
s.login(usuario_email, senha_email)

with open('titlosap.txt') as titulosap:
    janelaSAP = titulosap.read()

SAP = pygetwindow.getWindowsWithTitle(janelaSAP)


layout = [
        [sg.Multiline(key='seriais', size=(250,300), enable_events=True)],
        [sg.Text('Total de itens: '), sg.Text('', key='-NUMITEM-',enable_events=True),sg.Stretch()],
        [sg.Button('Executa', key='executar')]
        ]

window = sg.Window('Transferências', layout = layout)

while True:
    event, values = window.read()
    if event == None:
        break
    seriais = values['seriais']
    listaSeriais = seriais.split()
    window['-NUMITEM-'].update(len(listaSeriais))
    match(event):
        case 'executar':
            SAP.activate()
            SAP.maximize()
            for serial in listaSeriais:
                pyautogui.write(serial)
                pyautogui.press('tab')
                sleep(0.1)
                if pyautogui.locateOnScreen('impossivelLocalizar.png',confidence=0.9) != None:
                    sg.popup(f'Erro! {serial} não encontrado!\nLinha: {listaSeriais.index(serial)}')
                    break
                    
            sg.popup('Transferencia finalizada')
        case sg.WIN_CLOSED:
            exit()