import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
APIWHOP = os.getenv('APIWHOP')
url = "https://api.whop.com/api/v2/customers?page=1&per=999"
urlPaid = "https://api.whop.com/api/v2/payments?page=1&per=999&status=paid"
urlWalletDiscords = "https://api.whop.com/api/v2/payments?page=1&per=999&expand=user"
headers = {
    "accept": "application/json",
    "Authorization": APIWHOP
}
listOfAccounts = []
paymentList = []
walletList = []
def walletListDiscords():
    response = requests.get(urlWalletDiscords, headers=headers)
    z = json.loads(response.text)
    k = range(len(z["data"])-1)
    counter = 0
    beforew = []
    befored = []
    for i in k: 
        t = z["data"][i]["user"]["social_accounts"]
        r = range(len(t))
        if len(t) == 1:
            tempw = z["data"][i]["wallet_address"]
            tempD = z["data"][i]["user"]["social_accounts"][0]["username"]
            beforew.append(tempw)
            befored.append(tempD)
        else:
            for j in r:
                if(list(t[j].values())[0] == "discord"):
                    counter+=1
                    if counter >1:
                        continue
                    else:
                            tempw = z["data"][j]["wallet_address"]
                            tempD = z["data"][j]["user"]["social_accounts"][0]["username"]
                            beforew.append(tempw)
                            befored.append(tempD)
    walletList = list(zip(befored,beforew))
    return set(walletList)
def accounts():
    response = requests.get(url, headers=headers)
    y = json.loads(response.text)
    total_subs = (y["pagination"]["total_count"])
    n = range(total_subs-1)
    for i in n:
        counter = 0
        temp = y["data"][i]
        t = temp["social_accounts"]
        r = range(len(t))
        if (len(t) == 1):
            listOfAccounts.append(list(t[0].values()))
        else:
            for j in r:
                if(list(t[j].values())[0] == "discord"):
                    counter+=1
            if counter >1:
                continue
            else:
                listOfAccounts.append(list(t[0].values()))
    return listOfAccounts
        # print(y["data"][i]["social_accounts"][0])
        #print(temp)
def payments():
    responsePayments = requests.get(urlPaid, headers=headers)
    z = json.loads(responsePayments.text)
    total_count = (z["pagination"]["total_count"])
    m = range(total_count-1)
    tempTotal = []
    tempWallet = []
    for j in m:
        tempTotal.append(z["data"][j]["final_amount"])
        tempWallet.append(z["data"][j]["wallet_address"])
        
        
        # print(z["data"][j]["final_amount"])
        # print(z["data"][j]["wallet_address"])
        # print()
    paymentList = list(zip(tempWallet,tempTotal))
    walletList = set(tempWallet)
    return walletList
# payments()
