cor1 = '\033[32m'
reset = '\033[0m'

while True:
    resposta = input(f'{cor1}Tinha o pete e o repete, o pete morreu. Quem ficou vivo?{reset}\n')
    if resposta.lower() != 'repete':
        print("Tu é burro ou só se faz mesmo?")
        break