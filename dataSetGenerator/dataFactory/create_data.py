from time import sleep
from dataSetGenerator.dataFactory.printer import printer
from dataSetGenerator.dataFactory.loading import loading
from dataSetGenerator.dataFactory.generate_data_set import generate_data_set
from dataSetGenerator.dataFactory.show_data_set import show_data_set

def create_data():

    data_blocks = 0

    while data_blocks < 2:
        try:
            data_blocks = int(input("\n * Entrez le nombre de blocks de données que vous voulez utiliser :"))
            if data_blocks < 2:
                printer("\n !! Vous devez entrer au moins 2 blocks de données !! \n")
        except ValueError:
            printer("\n !! Veuillez entrer un entier !! \n")
            sleep(1)

    block_lengths = []

    for num in range(1 , data_blocks + 1):
        current_length = 0
        while current_length < 1:
            try:
                length = int(input(f"\n * Quelle est la taille du block no{num} ? :"))
                current_length = length
            except ValueError:
                printer("\n !! Veuillez entrer un entier !! \n")
                sleep(1)
        block_lengths.append(current_length)

    data = []

    for block_index in range(data_blocks):
        printer(f"\n -- Entrez les données du dataBlock no{block_index + 1} -- \n")
        sleep(1)
        current_data = []
        for current_data_block_index in range(1 , block_lengths[block_index] + 1):
            current_data_block = input(f"\n * Donnée no{current_data_block_index} du block : ")
            current_data.append(current_data_block)
        data.append(current_data)

    printer("\n * Traitement des données * \n")
    sleep(1.2)

    loading("-- Génération du DataSet" , 10)

    data_set = generate_data_set(data)

    printer("\n * DataSet généré avec succès * \n")
    sleep(1)

    print()

    show_data_set(data_set)