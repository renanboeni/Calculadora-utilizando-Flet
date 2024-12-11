import flet as ft
from flet import colors
from decimal import Decimal

botoes = [
    {"operador": "AC", "font": colors.BLACK, "fundo": "#DCDCDC"},
    {"operador": "±", "font": colors.BLACK, "fundo": "#DCDCDC"},
    {"operador": "%", "font": colors.BLACK, "fundo": "#DCDCDC"},
    {"operador": "/", "font": colors.WHITE, "fundo": colors.ORANGE},
    {"operador": "7", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "8", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "9", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "*", "font": colors.WHITE, "fundo": colors.ORANGE},
    {"operador": "4", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "5", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "6", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "-", "font": colors.WHITE, "fundo": colors.ORANGE},
    {"operador": "1", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "2", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "3", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "+", "font": colors.WHITE, "fundo": colors.ORANGE},
    {"operador": "0", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": ",", "font": colors.WHITE, "fundo": colors.WHITE24},
    {"operador": "=", "font": colors.WHITE, "fundo": colors.ORANGE},
] # Lista de botões da calculadora

def main(page: ft.Page):
    # Configs gerais
    page.title = "Calculadora" #Nome da janela
    page.bgcolor = "#000" #Cor do background
    page.window.width = 250 #Tamanho da largura
    page.window.height = 380 #Tamanho da altura
    
    page.window.always_on_top = True #Sempre deixa a calculadora acima de tudo
    page.window.resizable = False #Não deixar mudar o tamanho da calculadora

    result = ft.Text( value = "0", color = colors.WHITE, size = 25 )

    def calculate(operador, value_at):
        try:
            value_at = value_at.replace(",", ".")
            value = eval(value_at) #faz o calculo de qualquer valor que passar para dentro desta string
            if operador == "%": #definindo que a função porcentagem ira dividir o numero por 100
                value = value / 100
            elif operador == "±": #definindo que a função ira retornar o valor com operador contrario
                value = -value
        except:
            return "Error"
        
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f".{digits}f")


    def select(e):
        value_at = result.value if result.value not in ("0","Error") else "" #verifica se o número digitado é diferente de zero.
        value = e.control.content.value #captura o valor da função btn.

        if value.isdigit(): #verifica se é um digito.
            value = value_at + value #se for um número, ele vai ser concatenado com o valor anterior.
        elif value == "AC": #Se clicar AC, o valor ira ser zerado.
            value = "0"
        else:
            if value_at and value_at[-1] in ("/","*","-","+",","): # verifica se é um operador matematico
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ("=","%","±"): #verificando se o último valor é um operador
                value = calculate(operador = value[-1], value_at = value_at)

        result.value = value #atualizando o valor do display
        result.update() #atualizando o display


    display = ft.Row(
        width = 250,
        controls = [result],
        alignment = "end"
    )#display da calculadora

    btn = [ft.Container(
            content = ft.Text( value = btn["operador"],color = btn["font"] ), #Texto do botão
            width = 50,
            height = 50,
            bgcolor = btn["fundo"],
            border_radius = 100,
            alignment= ft.alignment.center,
            on_click = select,
        ) 
        for btn in botoes
    ] #replicando os Botões da calculadora

    keyboard = ft.GridView(
        expand = True,
        max_extent = 60,
        spacing = 5,
        run_spacing = 5,
        controls = btn,
    ) #teclado da calculadora

    #adicionando o display e o teclado na página
    page.add(display)
    page.add(keyboard)

ft.app(target = main)