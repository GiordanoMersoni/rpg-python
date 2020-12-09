import random, os, equip_item, emojis
from armor import *
from weapon import *
from char import *
from copy import deepcopy, copy
from terminedia import getch

#cmd = 'mode 160,30'
#os.system(cmd)

inimigo = emojis.encode(':japanese_ogre:')
player_character = emojis.encode(':running:')
chest = emojis.encode(':package:')
wall = emojis.encode(':heavy_plus_sign:')
life_heart = emojis.encode(':green_heart:')
cracked_heart = emojis.encode(':broken_heart:')
empty_heart = emojis.encode(':yellow_heart:')
blacksmith = emojis.encode(':nut_and_bolt:')
moneybag = emojis.encode(':moneybag:')
potion = emojis.encode(':wine_glass:')


wall_list = [[0,7], [0,10], [0,17],
            [1,2], [1,3], [1,4], [1,5], [1,7], [1,9], [1,10], [1,11], [1,12], [1,14], [1,18], [1,20],
            [2,1], [2,7], [2,10], [2,15], [2,16], [2,19], [2,23],
            [3,8], [3,12], [3,13], [3,17], [3,19], [3,22],
            [4,3], [4,4], [4,5], [4,6], [4,9], [4,10], [4,11], [4,14], [4,15], [4,21],
            [5,2], [5,7], [5,18], [5,19], [5,21], [5,23],
            [6,1], [6,4], [6,7], [6,8], [6,9], [6,10], [6,11], [6,12], [6,13], [6,14], [6,15], [6,21], [6,24],
            [7,1], [7,3], [7,5], [7,12], [7,20], [7,22],
            [8,1], [8,5], [8,8], [8,11], [8,12], [8,16], [8,18], [8,19], [8,20], [8, 23],
            [9,1], [9,3], [9,5], [9,8], [9,15], [9,20]]

chest_list = [[0,11], [1,19], [2,2], [7,4], [7,11], [7,21], [9,4], [9,16], [9,19]]

enemy_list = [[0,2], [0,12], [1,21], [1,22], [3,0], [3,24], [7,24], [8,3], [8,4], [8,21], [9,10], [9,17], [9,18]]

foe_list = [npc1, npc2, npc3]

armor_list = []
weapon_list = []
life_potion = [0, 20]
cash = [0]

linhas = 10
colunas = 25

# ------------------------------------------------------------- #
def cab():
    os.system('cls')
    print((' ' * 21), 'jogando')
    print((' ' * 13), '<<>>~~~~~~<<>>^~~~~~~<<>>')
    print((' ' * 18), 'WORK IN PROGRESS')
    print((' ' * 13), '<<>>~~~~~~<<>>^~~~~~~<<>>')
    print('')
# ------------------------------------------------------------- #
def bs(char1, char2):
    print('')
    print('o-----o o       o      o----o     ^  o--o--o  ^    o       o     o    ^   ')
    print('|       |\     /|      |     \   / \    |    / \   |       |     |   / \  ')
    print('|       | \   / |      |     /  /   \   |   /   \  |       |     |  /   \ ')
    print('o---o   |  \ /  |      o----<  o-----o  |  o-----o |       o-----o o-----o')
    print('|       |   o   |      |     \ |     |  |  |     | |       |     | |     |')
    print('|       |       |      |     / |     |  |  |     | |       |     | |     |')
    print('o-----o o       o      o----O  o     o  o  o     o o-----o o     o o     o')
    print('')
    print('        ', player_character, '                     ', inimigo)

    qtd_life_heart_player = char1.getLife() // 10
    if char1.getLife() % 10 == 0:
        qtd_cracked_heart_player = 0
    elif char1.getLife() % 10 > 0:
        qtd_cracked_heart_player = 1
    qtd_empty_heart_player = 10 - qtd_life_heart_player - qtd_cracked_heart_player
    
    qtd_life_heart_npc = char2.getLife() // 10
    if char2.getLife() % 10 == 0:
        qtd_cracked_heart_npc = 0
    elif char2.getLife() % 10 > 0:
        qtd_cracked_heart_npc = 1
    qtd_empty_heart_npc = 10 - qtd_life_heart_npc - qtd_cracked_heart_npc

    print(f'{life_heart * qtd_life_heart_player}{cracked_heart * qtd_cracked_heart_player}{empty_heart * qtd_empty_heart_player}     {life_heart * qtd_life_heart_npc}{cracked_heart * qtd_cracked_heart_npc}{empty_heart * qtd_empty_heart_npc}')


# ------------------------------------------------------------- #
def cabbs(char1, char2):
    cab()
    bs(char1, char2)
# ------------------------------------------------------------- #
def print_board(some_board): # imprimir matriz item por item      
    print(' ', end='')
    print('_' * 50)
    lin = 0
    while lin < linhas:
        col = 0
        print('|', end='')
        while col < colunas:
            print(some_board[lin][col], end='')
            col += 1
        print('|')
        lin += 1
    print(' ', end='')
    print('T' * 50)
# ------------------------------------------------------------- #
def get_random_spot(lin, col):
    r1 = lin - 1
    r2 = col - 1
    c1 = random.randint(0, r1)
    c2 = random.randint(0, r2)
    c = [c1, c2]
    return c
# ------------------------------------------------------------- #
def drop(char):
    reward = random.randint(25, 150)
    cash[0] += reward
    print('')
    print(f'{char.getName()} largou {reward} moedas')
    print('')
    drop_list = [char.weapon, char.armor]
    for item in drop_list:
        rate = random.randint(0, 2)
        if rate == 0:
            if item.type == 'armor':
                armor_list.append(deepcopy(item))
            else:
                weapon_list.append(deepcopy(item))
            print(f'{char.getName()} largou 1 {item.getName()}')
            print('')
    qtd = random.randint(0, 4)
    if qtd == 0:
        pass
    else:
        life_potion[0] += qtd
        print(f'{char.getName()} largou {qtd} poção(ões) de vida')
        print('')
# ------------------------------------------------------------- #
def use_potion(char):
    life_potion[0] -= 1
    char.recover(life_potion[1])
    print('')
    print(f'{char.getName()} usou uma poção e recuperou {life_potion[1]} de vida')
    print('')
    os.system('pause')
# ------------------------------------------------------------- #
def open_chest(char):
    cash_found = random.randint(200, 550)
    cash[0] += cash_found
    print('')
    print(f'{char.getName()} recolheu {cash_found} moedas')
    potion_found = random.randint(5, 9)
    life_potion[0] += potion_found
    print('')
    print(f'{char.getName()} recolheu {potion_found} poções de vida')
    print('')
    if char.weapon_type == 'axe':
        weapon_list.append(deepcopy(starterAxe))
        print(f'{char.getName()} recolheu 1 Starter Axe')
    elif char.weapon_type == 'bow':
        weapon_list.append(deepcopy(starterBow))
        print(f'{char.getName()} recolheu 1 Starter Bow')
    elif char.weapon_type == 'spear':
        weapon_list.append(deepcopy(starterSpear))
        print(f'{char.getName()} recolheu 1 Starter Spear')
    armor_list.append(deepcopy(starterArmor))
    print('')
    print(f'{char.getName()} recolheu 1 Starter Armor')
    print('')
    os.system('pause')
# ------------------------------------------------------------- #
def talk_to_blacksmith(char):
    while True:
        os.system('cls')
        cab()
        print('')
        print('       FERREIRO')
        print('')
        print('1 - Forjar Equipamento')
        print('2 - Vender Equipamento')
        print('3 - Comprar Equipamento')
        print('4 - Sair')
        print('')
        choice = int(input('Escolha sua opção: '))
        if choice == 1:
            pass
        elif choice == 2:
            while True:
                os.system('cls')
                cab()
                print('')
                print('    VENDER EQUIPAMENTO')
                print('')
                print('1 - Vender arma')
                print('2 - Vender armadura')
                print('3 - Sair')
                print('')
                opc = int(input('Escolha sua opção: '))
                if opc == 1:
                    print('')
                    cont = 0
                    while cont < len(weapon_list):
                        print(cont, '-', weapon_list[cont].getName(), '/', weapon_list[cont].getPrice())
                        cont += 1
                    print(cont, '- SAIR')
                    print('')
                    while True: 
                        sell = int(input('Digite o item a ser vendido: '))
                        if sell >= 0 and sell < len(weapon_list):
                            cash[0] += weapon_list[sell].getPrice()
                            del weapon_list[sell]
                            print('Item vendido')
                            os.system('pause')
                            break
                        elif sell == len(weapon_list):
                            break
                        else:
                            print('Inválido')
                            os.system('pause')    
                elif opc == 2:
                    print('')
                    cont = 0
                    while cont < len(armor_list):
                        print(cont, '-', armor_list[cont].getName(), '/', armor_list[cont].getPrice())
                        cont += 1
                    print(cont, '- SAIR')
                    print('')
                    while True: 
                        sell = int(input('Digite o item a ser vendido: '))
                        if sell >= 0 and sell < len(armor_list):
                            cash[0] += armor_list[sell].getPrice()
                            del armor_list[sell]
                            print('Item vendido')
                            os.system('pause')
                            break
                        elif sell == len(armor_list):
                            break
                        else:
                            print('Inválido')
                            os.system('pause')    
                elif opc == 3:
                    break
                else:
                    print('Oção inválida')
                    os.system('pause')
        elif choice == 3:


            while True:
                os.system('cls')
                cab()
                print('')
                print('    COMPRAR EQUIPAMENTO')
                print('')
                print('1 - Comprar arma')
                print('2 - Comprar armadura')
                print('3 - Comprar poção')
                print('4 - Sair')
                print('')
                opc = int(input('Escolha sua opção: '))
                if opc == 1:
                    while True:
                        os.system('cls')
                        cab()
                        print('')
                        print('     COMPRAR ARMA')
                        print('')
                        print(f'1 - {starterAxe.getName()} ({starterAxe.ATK}) - $500')
                        print(f'2 - {starterBow.getName()} ({starterBow.ATK}) - $500')
                        print(f'3 - {starterSpear.getName()} ({starterSpear.ATK}) - $500')
                        print(f'4 - {decentAxe.getName()} ({decentAxe.ATK}) - $850')
                        print(f'5 - {decentBow.getName()} ({decentBow.ATK}) - $850')
                        print(f'6 - {decentSpear.getName()} ({decentSpear.ATK}) - $850')
                        print('7 - SAIR')
                        print('')
                        compra = int(input('Escolha sua arma: '))
                        if compra == 1:
                            if cash[0] >= 500:
                                cash[0] -= 500
                                weapon_list.append(deepcopy(starterAxe))
                                print('')
                                print('Arma adquirida')
                                os.system('pause')
                                break
                            else:
                                print('')
                                print('Moedas insuficientes')
                                os.system('pause')
                        elif compra == 2:
                            if cash[0] >= 500:
                                cash[0] -= 500
                                weapon_list.append(deepcopy(starterBow))
                                print('')
                                print('Arma adquirida')
                                os.system('pause')
                                break
                            else:
                                print('')
                                print('Moedas insuficientes')
                                os.system('pause')
                        elif compra == 3:
                            if cash[0] >= 500:
                                cash[0] -= 500
                                weapon_list.append(deepcopy(starterSpear))
                                print('')
                                print('Arma adquirida')
                                os.system('pause')
                                break
                            else:
                                print('')
                                print('Moedas insuficientes')
                                os.system('pause')
                        elif compra == 4:
                            if cash[0] >= 850:
                                cash[0] -= 850
                                weapon_list.append(deepcopy(decentAxe))
                                print('')
                                print('Arma adquirida')
                                os.system('pause')
                                break
                            else:
                                print('')
                                print('Moedas insuficientes')
                                os.system('pause')
                        elif compra == 5:
                            if cash[0] >= 850:
                                cash[0] -= 850
                                weapon_list.append(deepcopy(decentBow))
                                print('')
                                print('Arma adquirida')
                                os.system('pause')
                                break
                            else:
                                print('')
                                print('Moedas insuficientes')
                                os.system('pause')
                        elif compra == 6:
                            if cash[0] >= 850:
                                cash[0] -= 850
                                weapon_list.append(deepcopy(decentSpear))
                                print('')
                                print('Arma adquirida')
                                os.system('pause')
                                break
                            else:
                                print('')
                                print('Moedas insuficientes')
                                os.system('pause')
                        elif compra == 7:
                            break
                        else:
                            print('Opção inválida')
                            os.system('pause')
                elif opc == 2:
                    while True:
                        os.system('cls')
                        cab()
                        print('')
                        print('     COMPRAR ARMADURA')
                        print('')
                        print(f'1 - {starterArmor.getName()} ({starterArmor.DEF}) - $500')
                        print(f'2 - {decentArmor.getName()} ({decentArmor.DEF}) - $850')
                        print('3 - SAIR')
                        print('')
                        compra = int(input('Escolha sua arma: '))
                        if compra == 1:
                            if cash[0] >= 500:
                                cash[0] -= 500
                                armor_list.append(deepcopy(starterArmor))
                                print('')
                                print('Arma adquirida')
                                os.system('pause')
                                break
                            else:
                                print('')
                                print('Moedas insuficientes')
                                os.system('pause')
                        if compra == 2:
                            if cash[0] >= 850:
                                cash[0] -= 850
                                armor_list.append(deepcopy(decentArmor))
                                print('')
                                print('Arma adquirida')
                                os.system('pause')
                                break
                            else:
                                print('')
                                print('Moedas insuficientes')
                                os.system('pause')
                        elif compra == 3:
                            break
                        else:
                            print('Opção inválida')
                            os.system('pause')
                elif opc == 3:
                    pass
                elif opc == 4:
                    break
                else:
                    print('Oção inválida')
                    os.system('pause')
        elif choice == 4:
            break
        else:
            print('Opção inválida')
            os.system('pause')



# ------------------------------------------------------------- #
def equipar(char):
    while True:
        os.system('cls')
        cab()
        print('')
        print('1 - Equipar arma')
        print('2 - Equipar armadura')
        print('3 - Sair')
        equip = int(input('Escolha sua opção: '))
        if equip == 1:
            if char.weapon == None:
                print('')
                cont = 0
                while cont < len(weapon_list):
                    print(cont, '-', weapon_list[cont].getName(), 'ATK:', weapon_list[cont].ATK)
                    cont+=1
                print(cont, '- SAIR')
                print('')
                while True:
                    selec = int(input('Selecione a arma a ser equipada: '))
                    if selec >= 0 and selec < len(weapon_list):
                        if weapon_list[selec].type == char.weapon_type:
                            char.setWeapon(deepcopy(weapon_list[selec]))
                            del weapon_list[selec]
                            print('')
                            print('Arma equipada')
                            print('')
                            os.system('pause')
                            break
                        else:
                            print('Arma não compatível com seu personagem')
                            os.system('pause')
                    elif selec == len(weapon_list):
                        break
                    else:
                        print('Inválido')
                        os.system('pause')
            else:
                print('')
                print('Arma já equipada')
                print('')
                os.system('pause')
        elif equip == 2:                
            if char.armor == None:
                print('')
                cont = 0
                while cont < len(armor_list):
                    print(cont, '-', armor_list[cont].getName(), 'DEF:', armor_list[cont].DEF)
                    cont+=1
                print(cont, '- SAIR')
                print('')
                while True:
                    selec = int(input('Selecione a armadura a ser equipada: '))
                    if selec >= 0 and selec < len(armor_list):
                        char.setArmor(deepcopy(armor_list[selec]))
                        del armor_list[selec]
                        print('')
                        print('Armadura equipada')
                        print('')
                        os.system('pause')
                        break
                    elif selec == len(armor_list):
                        break
                    else:
                        print('Inválido')
                        os.system('pause')
            else:
                print('')
                print('Armadura já equipada')
                print('')
                os.system('pause')
        elif equip == 3:
            break
        else:
            print('')
            print('Opção inválida')
            os.system('pause')

# ------------------------------------------------------------- #
def desequipar(char):
    while True:
        os.system('cls')
        cab()
        print('')
        print('1 - Desequipar arma')
        print('2 - Desequipar armadura')
        print('3 - Sair')
        desequip = int(input('Escolha sua opção: '))
        if desequip == 1:
            if char.weapon != None:
                weapon_list.append(deepcopy(char.weapon))
                char.setWeapon(None)
                print('')
                print('Arma desequipada')
                print('')
                os.system('pause')
                break
            else:
                print('')
                print('Nenhuma arma equipada')
                print('')
                os.system('pause')
        elif desequip == 2:                
            if char.armor != None:
                armor_list.append(deepcopy(char.armor))
                char.setArmor(None)
                print('')
                print('Armadura desequipada')
                print('')
                os.system('pause')
                break
            else:
                print('')
                print('Nenhuma armadura equipada')
                print('')
                os.system('pause')
        elif desequip == 3:
            break
        else:
            print('')
            print('Opção inválida')
            os.system('pause')

# ------------------------------------------------------------- #
def char_selection():
    print('          Bem vindo')
    print('Digite o nome do seu personagem:')
    char_name = input('>>>> ')

    classpick = None

    while True:
        os.system("cls")
        print('Paladinos empunham machados, Druidas são lanceiros e Arqueiros você consegue adivinhar\n')
        print('Escolha a classe de seu personagem:  1 - Paladino')
        print('                                     2 - Arqueiro')
        print('                                     3 - Druida')
        classpick = int(input(">>>> "))
        if classpick == 1:
            os.system("cls")
            print('Classe selecionada: Paladino')
            char = Paladin(char_name, decentArmor, starterAxe, 100, 100)
            os.system("pause")
            break
        elif classpick == 2:
            os.system("cls")
            print('Classe selecionada: Arqueiro')
            char = Ranger(char_name, decentArmor, starterBow, 100, 100)
            os.system("pause")
            break
        elif classpick == 3:
            os.system("cls")
            print('Classe selecionada: Druida')
            char = Druid(char_name, decentArmor, starterSpear, 100, 100)
            os.system("pause")
            break
        else:
            os.system("cls")
            print('Opção não disponível. Digite novamente')
            os.system("pause")
    return char

# ------------------------------------------------------------- #
def batlle(char1, char2):

    cont = 0

    while True:
        if cont == 0:
            cabbs(char1, char2)
            print('1 - Ataque Normal')
            print('2 - Ataque Carregado', end=' ')
            if char1.weapon_type == 'axe' and char1.getCharge() >= 40:
                print(f'(Pronto para usar)')
            elif char1.weapon_type == 'bow' and char1.getCharge() >= 30:
                print(f'(Pronto para usar)')
            elif char1.weapon_type == 'spear' and char1.getCharge() >= 22:
                print(f'(Pronto para usar)')
            else:
                print('(Carregando)')
            print('3 - Usar Poção')
            print('')
            while True:
                move = int(input('Digite seu movimento: '))
                if move == 1:
                    char1.getDamage(char2)
                    break
                elif move == 2:
                    if char1.charge >= char1.needed_charge:
                        char1.getUlt(char2)
                        break
                    else:
                        print('Ataque Carregado não está pronto para usar')
                        print('')
                        os.system('pause')
                elif move == 3:
                    if life_potion[0] > 0:
                        use_potion(char1)
                        break
                    else:
                        print('Não possui poções de vida')
                        os.system('pause')
                else:
                    pass
            if char2.getLife() <= 0:
                print(f'{char2.getName()} morreu')
                drop(char2)
                os.system('pause')
                break
            cont = 1
        elif cont == 1:


            cabbs(char1, char2)
            print('')

            if char2.charge >= char2.needed_charge:
                sorteio = random.randint(1, 7)
                if sorteio == 5:
                    move = 2 
                else:
                    move = 1

            if move == 1:
                char2.getDamage(char1)
            elif move == 2:
                char2.getUlt(char1)
            
            if char1.getLife() <= 0:
                print(f'{char1.getName()} morreu')
                os.system('pause')
                break

        
            cont = 0

# ------------------------------------------------------------- #
def start_game(obj_player, spot, board):
    while True:
        os.system('cls')
        cab()
        print('                    ', moneybag, cash[0])
        print((' ' * 6), 'Mover-se            Usar Poção de Vida - P')
        print((' ' * 6), '   W                   Desequipar Item - R')
        print((' ' * 6), 'A  S  D                   Equipar Item - E')
        print('')
        
        print(player_character, end='')
        qtd_life_heart = player.getLife() // 10
        if player.getLife() % 10 == 0:
            qtd_cracked_heart = 0
        elif player.getLife() % 10 > 0:
            qtd_cracked_heart = 1
        qtd_empty_heart = 10 - qtd_life_heart - qtd_cracked_heart
        print(f'{life_heart * qtd_life_heart}{cracked_heart * qtd_cracked_heart}{empty_heart * qtd_empty_heart}', end='                 ')

        print(potion, life_potion[0])

        if player.weapon != None:
            arma = player.weapon.getName()
        else:
            arma = 'Nenhuma arma equipada'
        if player.armor != None:
            armadura = player.armor.getName()
        else:
            armadura = 'Nenhuma armadura equipada'
        print('     Equipado: ', arma, ' / ', armadura)
        
        print_board(board)
        print('')
        while True:
            move = getch()
            if (move == 'a' or move == 'A') and spot[1] > 0:
                if board[spot[0]][spot[1] - 1] == '  ':
                    spot[1] -= 1
                    board[spot[0]][spot[1]] = player_character
                    board[spot[0]][spot[1] + 1] = '  '
                    break
                elif board[spot[0]][spot[1] - 1] == inimigo:
                    indice = random.randint(0, 2)
                    enemy = deepcopy(foe_list[indice])
                    os.system('cls')
                    cab()
                    print(f'Começando batalha com {enemy.getName()}')
                    print('')
                    os.system('pause')
                    batlle(player, enemy)
                    if enemy.getLife() <= 0:
                        spot[1] -= 1
                        board[spot[0]][spot[1]] = player_character
                        board[spot[0]][spot[1] + 1] = '  '
                    break
                elif board[spot[0]][spot[1] - 1] == chest:
                    open_chest(player)
                    board[spot[0]][spot[1] - 1] = '  '
                    break
                elif board[spot[0]][spot[1] - 1] == blacksmith:
                    talk_to_blacksmith(player)
                    break
            elif (move == 's' or move == 'S') and spot[0] < (linhas - 1): 
                if board[spot[0] + 1][spot[1]] == '  ':
                    spot[0] += 1
                    board[spot[0]][spot[1]] = player_character
                    board[spot[0] - 1][spot[1]] = '  '
                    break
                elif board[spot[0] + 1][spot[1]] == inimigo:
                    indice = random.randint(0, 2)
                    enemy = deepcopy(foe_list[indice])
                    os.system('cls')
                    cab()
                    print(f'Começando batalha com {enemy.getName()}')
                    print('')
                    os.system('pause')
                    batlle(player, enemy)
                    if enemy.getLife() <= 0:
                        spot[0] += 1
                        board[spot[0]][spot[1]] = player_character
                        board[spot[0] - 1][spot[1]] = '  '
                    break
                elif board[spot[0] + 1][spot[1]] == chest:
                    open_chest(player)
                    board[spot[0] + 1][spot[1]] = '  '
                    break
                elif board[spot[0] + 1][spot[1]] == blacksmith:
                    talk_to_blacksmith(player)
                    break
            elif (move == 'd' or move == 'D') and spot[1] < (colunas - 1):
                if board[spot[0]][spot[1] + 1] == '  ':
                    spot[1] += 1
                    board[spot[0]][spot[1]] = player_character
                    board[spot[0]][spot[1] - 1] = '  '
                    break
                elif board[spot[0]][spot[1] + 1] == inimigo:
                    indice = random.randint(0, 2)
                    enemy = deepcopy(foe_list[indice])
                    os.system('cls')
                    cab()
                    print(f'Começando batalha com {enemy.getName()}')
                    print('')
                    os.system('pause')
                    batlle(player, enemy)
                    if enemy.getLife() <= 0:
                        spot[1] += 1
                        board[spot[0]][spot[1]] = player_character
                        board[spot[0]][spot[1] - 1] = '  '
                    break
                elif board[spot[0]][spot[1] + 1] == chest:
                    open_chest(player)
                    board[spot[0]][spot[1] + 1] = '  '
                    break
                elif board[spot[0]][spot[1] + 1] == blacksmith:
                    talk_to_blacksmith(player)
                    break
            elif (move == 'w' or move == 'W') and spot[0] > 0:
                if board[spot[0] - 1][spot[1]] == '  ':
                    spot[0] -= 1
                    board[spot[0]][spot[1]] = player_character
                    board[spot[0] + 1][spot[1]] = '  '
                    break
                elif board[spot[0] - 1][spot[1]] == inimigo:
                    indice = random.randint(0, 2)
                    enemy = deepcopy(foe_list[indice])
                    os.system('cls')
                    cab()
                    print(f'Começando batalha com {enemy.getName()}')
                    print('')
                    os.system('pause')
                    batlle(player, enemy)
                    if enemy.getLife() <= 0:
                        spot[0] -= 1
                        board[spot[0]][spot[1]] = player_character
                        board[spot[0] + 1][spot[1]] = '  '
                    break
                elif board[spot[0] - 1][spot[1]] == chest:
                    open_chest(player)
                    board[spot[0] - 1][spot[1]] = '  '
                    break
                elif board[spot[0] - 1][spot[1]] == blacksmith:
                    talk_to_blacksmith(player)
                    break
            elif (move == 'p' or move == 'P') and life_potion[0] > 0:
                life_potion[0] -= 1
                player.recover(life_potion[1])
                print(player.getName(), 'recuperou', life_potion[1], 'de vida')
                os.system('pause')
                break
            elif (move == 'e' or move == 'E'):
                equipar(player)
                break
            elif (move == 'r' or move == 'R'):
                desequipar(player)
                break
            else:
                pass

        if player.getLife() <= 0:
            print('')
            print('FIM DE JOGO')
            print('')
            os.system('pause')
            break


# -------------------------- MAIN ------------------------- #

if __name__ == "__main__":
    os.system("cls")
    player = char_selection()

    vetor = ['  '] * colunas
    gameboard = []
    for times in range(linhas):
        gameboard.append(vetor.copy())

    gameboard[0][0] = player_character
    gameboard[5][1] = blacksmith
    

    for lista in wall_list:
        gameboard[lista[0]][lista[1]] = wall
    for lista in chest_list:
        gameboard[lista[0]][lista[1]] = chest
    for lista in enemy_list:
        gameboard[lista[0]][lista[1]] = inimigo

    player_coord = [0, 0]

    for times in range(5):
        while True:
            coord = get_random_spot(linhas, colunas)
            if gameboard[coord[0]][coord[1]] == '  ':
                gameboard[coord[0]][coord[1]] = inimigo
                break
            else:
                pass

    start_game(player, player_coord, gameboard)