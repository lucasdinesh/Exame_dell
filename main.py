from reader_PontosdeTaxi import reader_taxi
from menu import menu



HashTable = ['' for _ in range(739)]    #[latitude, longitude, logradouro, numero, telefone]
reader_taxi(HashTable)
menu(HashTable) #design pattern proxy

print("eu amo arroz com feijao, certamente comeria todo dia")

