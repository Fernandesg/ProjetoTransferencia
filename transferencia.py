import pygetwindow
import pyautogui
import PySimpleGUIQt as sg
import smtplib

usuario = 'pythonautoriza@gmail.com'
senha = 'zupobloxnswadzio'
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
s.login(usuario, senha)

janelaSAP = 'SAP Business One 9.3 (g2srv11.G2TECNOLOGIA.COM.BR)'

SAP = pygetwindow.getWindowsWithTitle(janelaSAP)[0]


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
            sg.popup('Transferencia finalizada')
        case sg.WIN_CLOSED:
            exit()