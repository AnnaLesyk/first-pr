""""""
from data_service import get_balances, get_indexes

TITLE = "Аналіз динаміки оборотних коштів та оборотного капіталу підприємства" 
HEADER = \
  """
  ===================================================================================================================
  НАЗВА БАЛАНСУ:    ПОКАЗНИК:   НА ПОЧАТОК РОКУ:   НА ПОЧАТОК 2 КВ: НА ПОЧАТОК 3 КВ:  НА ПОЧАТОК 4 КВ: НА КІНЕЦЬ РОКУ 
  ===================================================================================================================
  """

indexes = get_indexes()
balances = get_balances()

def find_name_of_index(index_code):
      """пошук назви підрозділу балансу за показником"""

      for index in indexes:
        if index_code == index[0]:
          return index[1]

      return "немає назви"

def str_to_num(str_num):

  """перетворює строкове число в звичайне"""
  if str_num.insumeric():
        return float(str_num)
  else:    
        return float(str_num[:-1])

def show_application(applications ):
    """вивід результатів на екран"""
    print(TITLE)
    print(HEADER)
    for row in application:
      print(f"{row['unit']}",
            f"{row ['beg']} ",  
            f"{row['2_quarter']}",
            f"{row['3_quarter']}",
            f"{row['4_quarter']}",
            f"{row['end']}" )   

    pass

application = {
  'unit'      : ""  ,  # назва підрозділу балансу (table_2)
  'index'     : ""  ,  # показник                 (table_1)
  'beg'       : 0.0 ,  # на початку року          (table_2)
  '2_quarter' : 0.0 ,  # на початок 2 кварталу    (table_2)
  '3_quarter' : 0.0 ,  # на початок 3 кварталу    (table_2)
  '4_quarter' : 0.0 ,  # на початок 4 кварталу    (table_2)
  'end'       : 0.0 ,  # на кінець року           (table_2)
}

applications = []

for index in indexes:
  application['unit']      = index[0]
  application['beg']       = index[2]
  application['2_quarter'] = index[3]
  application['3_quarter'] = index[4]
  application['4_quarter'] = index[5]
  application['end']       = index[6]

  applications.append(application)

show_application(application)