from re import S
import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('Dark')
        # Layout
        layout = [
            [sg.Text('nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('quais provedores de email são aceitos?')],
            [sg.Checkbox('gmail', key='gmail'), sg.Checkbox('Outkook', key='outlook'),
             sg.Checkbox('Terra', key='terra')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('sim', 'cartoes', key='aceitaCartao'),sg.Radio('não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0,255),default_value=0, orientation='h',size=(15,20), key='sliderVelocidade' )],
            [sg.Button('enviar dados')],
            [sg.Output(size=(30,20))],
        ]
        # janela
        self.janela = sg.Window("Dados de usuario").layout(layout)



    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['terra']
            aceita_Cartao = self.values['aceitaCartao']
            nao_aceitacartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']

            print(f'nome:{nome}')
            print(f'idade :{idade}')
            print(f'gmail: {aceita_gmail}')
            print(f'outlook: {aceita_outlook}')
            print(f'yahoo : {aceita_yahoo}')
            print(f'aceita cartao: `{aceita_Cartao}')
            print(f'não aceita catão: {nao_aceitacartao}')
            print(f'Velocidade Script: {velocidade_script}')


tela = TelaPython()
tela.Iniciar()
