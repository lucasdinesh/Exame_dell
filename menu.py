from Haversine import haversine

def print_menu():
    menu = 'MENU'
    print(menu.center(30, '='))
    print(' 1. Listar todos os pontos de taxi\n',
          '2. Informar minha localização \n',
          '3. Encontrar pontos próximos \n',
          '4. Buscar pontos por logradouro \n',
          '5. Terminar o programa \n'
          )
    
    
def option_1(HashTable):
    for i in range(len(HashTable)):
        if (HashTable[i] == ''):
            pass
        else:
            print('Endereço:', HashTable[i][2], HashTable[i][3], f'Telefone: {HashTable[i][3]} ')
            
            
def option_2():
        print('Informe sua localização: ')
        input_lat = float(input('Digite sua latitude:').replace(',', '.'))
        input_lon = float(input('Digite sua longitude:').replace(',', '.'))
        return input_lat, input_lon

    
    
def option_3(HashTable, lat, lon):
    #try, except caso a latitude e longitude da opção 2 não for enviada.
    try:
        distance_tables = haversine(lat, lon, HashTable)
        distance_tables.sort(key=lambda x: x[1])  #metodo sort para ordenamento das distancias
        print('Os pontos mais proximos são:')
        for pontos in range(3):
            codigo = distance_tables[pontos][0]
            print(HashTable[codigo][2], HashTable[codigo][3],
                f'  Distancia entre usuario e ponto: {(distance_tables[pontos][1])}')
    except:
        print('Digite uma latide e uma Longitude na opção 2')
        
        

def option_4(HashTable):
        have_lograd = False
        input_lograd = str(input('Digite todo ou parte do nome do logradouro:\n')).upper()
        print(f'Os pontos de taxi ao longo de {input_lograd} são:')
        for i in range(len(HashTable)):
            if (HashTable[i] == ''):
                pass
            else:
                if (input_lograd in HashTable[i][2]):
                    print(HashTable[i][2], HashTable[i][3])
                    have_lograd = True
        if have_lograd == False:
            print('Não existe ponto de taxi com esse logradouro !!!')

def menu(HashTable):
    while(True):
        print_menu()
        try:
            option = int(input('Escolha uma das opções:\n'))
        except: print('Só são aceitos caracteres numéricos. ')
        if (option == 1):
            option_1(HashTable)

        elif(option == 2):
            try:
                input_lat, input_lon = option_2()
            except:
                print('Digite os campos corretamente!!')
        elif (option == 3):
            option_3(HashTable, input_lat, input_lon)

        elif(option == 4):
            option_4(HashTable)

        elif (option == 5):
            exit()
        else:
            print('Digite uma opção valída')
