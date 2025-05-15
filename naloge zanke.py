# user_input = ""
# while user_input != "skrivnost":
#     user_input = input("Vnesi geslo: ")
#     if user_input == "skrivnost":
#         print("dostop dovoljen")
#     else:
#         print("nimas pravic")

# imena = ["Ana", "Borut", "Andraž", "Cene", "Ajda"]
# for ime in imena:
#     firstletter = ime[0]
#     if firstletter == "A":
#         print(ime)

# poskusi = 0
# user_input = ""
# while user_input != "0":
#     user_input = input("Vnesi naključno število do 20: ")
#     if user_input != "0":
#         poskusi += 1
#         print("poskusi se enkrat")
#     else:
#         print("cestitke izbral si pravo")
# print("Število poskusov: "poskusi)

import random

ucenci = ["Ana", "Borut", "Cene", "Daša", "Eva"]
preostali_ucenci = ucenci.copy()
while True:
    if len(preostali_ucenci) == 0:
        vsi_ucenci = ucenci.copy()
        
        izbran_ucenec = random.choice(preostali_ucenci)
        print(izbran_ucenec)
        preostali_ucenci.remove(izbran_ucenec)
    elif len(ucenci) != 0: