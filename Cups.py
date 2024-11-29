'''
Função para listar um país e seus respectivos anos de titulos de copas com base no input do usuário
'''
def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
         print('years: ', title)

world_cup_titles('Brazil', 1990, 2000)