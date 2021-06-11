from csv import reader


HashTable = ['' for _ in range(739)]    #[latitude, longitude, logradouro, numero, telefone]

def reader_PontosdeTaxi(HashTable):
    with open('pontos_taxi.csv', encoding='utf-8') as csv_file:
        csv_reader = reader(csv_file, delimiter=';')

        csv_reader.__next__()

        for row in csv_reader:

            lat = float(row[6].replace(',','.'))
            lon = float(row[7].replace(',','.'))
            codigo = int(row[1])
            lograd = str(row[4])
            tel = str(row[3])
            tupla_aux =(lat, lon, lograd, tel)

            HashTable[codigo]=tupla_aux


reader_PontosdeTaxi(HashTable)
