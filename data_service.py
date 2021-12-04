def get_balances():
    """читання файлу балансу підприємства 'table1'
    та формування списку балансів 
    і повернення цього списку
     """

    # накопиченя даних файлу 
    with open("./data/table1.csv" , 'r' ) as f:
        balances = f.readlines()

    # підготовка даних для подальшої обробки
    balances_splitted = []
    # порізати в циклі строки на окремі елементи
    for balance in balances:
        obj = split_line(balance)
        obj[0] = int(obj[0])
        balances_splitted.append(obj)

        return balances_splitted

def split_line(line):
    """повертає список балансів із рядка"""
    object = line.split(',')
    return object

def show_balances(balances):
    """виводить список балансів підприємства по заданому інтервалу кодів"""

    # задання інтервалу кодів
    balance_code_from = int(input("З якого коду баланс ?"))
    balance_code_to = int(input("По який код ?"))

    # відбiр списку заданих кодів
    filtered_balances = []
    for balance in balances:
        if balance_code_from <= balance[0] <= balance_code_to:
            filtered_balances.append(balance)
    if len(filtered_balances) == 0:
        print ("В списку балансів підприємства даних кодів не виявлено")
        return

    # вивід відфільтрованого спискі балансів підприємства
    print("ДОВІДНИК БАЛАНСІВ ПІДПРИЄМСТВА")
    for balance in filtered_balances:
        print(f'код рядка:{balance[0]:3} показник: {balance[1]:20} ')



def get_indexes():
    """читання файлу балансу підприємства 'table2'
    та формування списку балансів 
    і повернення цього списку
     """

    # накопиченя даних файлу 
    with open("./data/table2.csv" , 'r' ) as f:
        indexes = f.readlines()

    # підготовка даних для подальшої обробки
    indexes_splitted = []
    # порізати в циклі строки на окремі елементи
    for index in indexes:
        obj = split_line(index)
        obj[0] = int(obj[0])
        indexes_splitted.append(obj)

        return indexes_splitted

def new_func(obj):
    obj[0] = int(obj[0])

def split_line(line):
    """повертає список балансів із рядка"""
    object = line.split(',')
    return object

def show_indexes(indexes):
    """виводить список балансів підприємства по заданому інтервалу кодів"""

    # задання інтервалу кодів
    index_code_from = int(input("З якого коду баланс ?"))
    index_code_to = int(input("По який код ?"))

    # відбiр списку заданих кодів
    filtered_indexes = []
    for index in indexes:
        if index_code_from <= index[0] <= index_code_to:
            filtered_indexes.append(index)
    if len(filtered_indexes) == 0:
        print ("В списку балансів підприємства даних кодів не виявлено")
        return

    # вивід відфільтрованого спискі балансів підприємства
    print("ДОВІДНИК БАЛАНСІВ ПІДПРИЄМСТВА")
    for index in filtered_indexes:
        print(f'код рядка:{index[0]:3} показник: {index[1]:20} ')

#  читання файлу балансів підприємства `table1`
# вивід списку всіх балансів 

if __name__ == '__main__':
    balances = get_balances 
    indexes = get_indexes