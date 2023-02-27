import whop
import pygsheets
import pandas as pd
gc = pygsheets.authorize(service_file='gold-378922-99c5daa27a7e.json')
users = whop.accounts()
payments = whop.payments()
walletList = whop.walletListDiscords()
# Create empty dataframe
dfAmount = pd.DataFrame()
dfListofUsers = pd.DataFrame()
dfPayments = pd.DataFrame()
dfWallets = pd.DataFrame()

#pad data out to get discords[0] and wallets[1] 
discordsT = []
walletT = []
for i in walletList:
    discordsT.append(i[0])
    walletT.append(i[1])

# Create a column
dfAmount['Amount of subs'] = [len(users)]
dfListofUsers['Discords'] = discordsT
dfPayments['PaymentList'] = [payments]
dfWallets['Wallet'] = walletT
#open the google spreadsheet 
sh = gc.open('Gold role')

#select the third sheet,start at 0
wks = sh[2]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(dfAmount,(1,1))
wks.set_dataframe(dfWallets,(1,3))
wks.set_dataframe(dfListofUsers,(1,2))
# wks.set_dataframe(dfPayments, (3,2))
