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
            if (HashTable[i][4] == ' '):
                print('Endereço:', HashTable[i][2], HashTable[i][3])
            else:
                print('Endereço:', HashTable[i][2], HashTable[i][3], f'Telefone: {HashTable[i][4]}')
            
            
def option_2():
        print('Informe sua localização: ')
        input_lat = float(input('Digite sua latitude:').replace(',', '.'))
        input_lon = float(input('Digite sua longitude:').replace(',', '.'))
        return input_lat, input_lon

    
    
def option_3(HashTable, lat1, lon1):
        distance_tables=[]
        for codigo in range(len(HashTable)):
            if(HashTable[codigo] == ''):
                pass
            else:
                lat2= HashTable[codigo][0]
                lon2= HashTable[codigo][1]
                aux = haversine(lat1,lon1,lat2,lon2,codigo)
                print(aux)
                distance_tables.append(aux)
                
        distance_tables.sort(key=lambda x: x[1])  #metodo sort para ordenamento das distancias
        print('Os pontos mais proximos são:')
        for pontos in range(3):
            codigo = distance_tables[pontos][0]
            print(HashTable[codigo][2], HashTable[codigo][3],
                f'  Distancia entre usuario e ponto: {(distance_tables[pontos][1])}')
        

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
        try:
            print_menu()
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
     #try, except caso a latitude e longitude da opção 2 não for enviada.
            try:
                option_3(HashTable, input_lat, input_lon)
            except:
                 print('Digite uma latide e uma Longitude na opção 2')
        elif(option == 4):
            option_4(HashTable)

        elif (option == 5):
            exit()
        else:
            print('Digite uma opção valída')
