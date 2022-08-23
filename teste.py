import pygetwindow
import pyautogui
import PySimpleGUIQt as sg

janelaSAP = 'SAP Business One 9.3 (g2srv11.G2TECNOLOGIA.COM.BR)'

SAP = pygetwindow.getWindowsWithTitle(janelaSAP)[0]


layout = [[sg.Input(key='seriais', size=(300,100))],
        [sg.Button('Executa', key='executar')]]

window = sg.Window('Transferencia', layout)

while True:
    event, values = window.read()
    seriais = values['seriais']
    listaSeriais = seriais.split()
    match(event):
        case 'executar':
            SAP.activate()
            SAP.maximize()
            for serial in listaSeriais:
                # print(seriais)
                print(serial)
                pyautogui.write(serial)
                pyautogui.press('tab')
        case sg.WIN_CLOSED:
            break
        case None:
            break