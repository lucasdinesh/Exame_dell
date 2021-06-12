from csv import reader

def reader_taxi(HashTable):
    with open('pontos_taxi.csv', encoding='utf-8') as csv_file:
        csv_reader = reader(csv_file, delimiter=';')

        csv_reader.__next__()

        for row in csv_reader:

            lat = float(row[6].replace(',','.')) #tratamento do objeto recebido, de virgula para ponto
            lon = float(row[7].replace(',','.'))
            codigo = int(row[1])
            lograd = str(row[4])
            num = str(row[5])
            tel = str(row[3])
            tupla_aux =(lat, lon, lograd,num, tel)

            HashTable[codigo]=tupla_aux
