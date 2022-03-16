
from request_tx import BabiesDegenFlipTx

#select the period
date_from = "2022-03-16 08:00:00"
date_to = "2022-03-16 17:00:00"

BDF = BabiesDegenFlipTx(date_to = date_to, date_from = date_from) #Starting session to scrap data from BabiesDegenFlip

BDF.get_all_tx() #get every transaction with the following info : sender, receiver, value bet, date
print("\nWin/Lose status :")

BDF.get_wallet_WoL(thread = 150) #getting sc results for every tx, then deciding if win or lose according to it

BDF.get_winstreak() #get the maximum winstreak per player

BDF.update_data(name = "BabiesDegenFlipTX.json") #save data into json file
