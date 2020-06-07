import json
import requests
import subprocess as sp

url = "https://api.rootnet.in/covid19-in/stats/latest"
response = requests.get(url)
parsed=response.text
data=json.loads(parsed)

def clear():
    tmp = sp.call('cls',shell=True)
    print("WELCOME TO COVID TRACKER INDIA BY AVILASH GHOSH")
    print("\nLIVE COUNTRY WIDE DATA FROM OFFICIAL SORCES\n\n")

def official_data():
    clear()
    #data printing of official data
    cc=data['data']['summary']['total']
    print(f"Total number of confirmed cases: {cc}\n")
    
    cci=data['data']['summary']['confirmedCasesIndian']
    print(f"Number of confirmed cases of Indian Nationality: {cci}\n")
    
    ccf=data['data']['summary']['confirmedCasesForeign']
    print(f"Number of confirmed cases of Non-Indian Nationality: {ccf}\n")

    recv=data['data']['summary']['discharged']
    print(f"Number of patients recovered: {recv}\n")


    dead=data['data']['summary']['deaths']
    print(f"Number of patients dead: {dead}\n")

    active=cc-(recv+dead)
    print(f"Number of active cases: {active}\n")

    print("Last Refreshed on: "+str(data['lastRefreshed'])+"\n")

def unofficial_data():
    clear()
    #data printing of official data
    cc=data['data']['unofficial-summary'][0]['total']
    print(f"Total number of confirmed cases: {cc}\n")

    recv=data['data']['unofficial-summary'][0]['recovered']
    print(f"Number of patients recovered: {recv}\n")


    dead=data['data']['unofficial-summary'][0]['deaths']
    print(f"Number of patients dead: {dead}\n")

    active=data['data']['unofficial-summary'][0]['active']
    print(f"Number of active cases: {active}\n")

    print("Last Refreshed on: "+str(data['lastRefreshed'])+"\n")

def selct_state():
    select=int(input('''                                  List Of States

1. Andaman and Nicodar Islands    12. Haryana               23. Mizoram
2. Andhra Pradesh                 13. Himachal pradesh      24. Odisa
3. Arunachal Pradesh              14. Jammu and Kashmir     25. Puducherry
4. Assam                          15. Jharkhand             26. Punjab
5. Bihar                          16. Karnataka             27. Rajasthan
6. Chandigarh                     17. Kerala                28. Tamil Nadu
7. Chattisgarh                    18. Ladakh                29. Telengana
8. Dadar Nagar Haveli             19. Madhya Pradesh        30. Tripura
9. Delhi                          20. Maharashtra           31. Uttarakhand
10. Goa                           21. Manipur               32. Uttar Pradesh
11. Gujrat                        22. Meghalaya             33. West Bengal

Select a State (Enter the number): '''))
    return (select-1)

def state_data():
    clear()
    select=selct_state()
    clear()
    #data printing of state data
    state_info=data['data']['regional'][select]
    state_name=state_info['loc']
    print(f"Name of the State: {state_name}\n")

    cc=state_info['totalConfirmed']
    print(f"Total number of confirmed cases: {cc}\n")
    
    cci=state_info['confirmedCasesIndian']
    print(f"Number of confirmed cases of Indian Nationality: {cci}\n")
    
    ccf=state_info['confirmedCasesForeign']
    print(f"Number of confirmed cases of Non-Indian Nationality: {ccf}\n")

    recv=state_info['discharged']
    print(f"Number of patients recovered: {recv}\n")


    dead=state_info['deaths']
    print(f"Number of patients dead: {dead}\n")

    active=cc-(recv+dead)
    print(f"Number of active cases: {active}\n")

    print("Last Refreshed on: "+str(data['lastRefreshed'])+"\n")

while True:
    official_data()
    choice=int(input("\n1. View data from covid19idia.org\n2. View data of individual states\n3. Exit\n"))
    if choice==1:
        choice2=0
        while True:
            unofficial_data()  
            choice1=int(input("\n1. View data from Official Sources\n2. View data of individual states\n3. Exit\n"))
            if choice1 == 1:
                break
            elif choice1==2:
                while True:
                    state_data()
                    choice2=int(input("\n1. View data from Official Sources\n2. View data from covid19idia.org\n3. Select a different state\n4. Exit\n"))
                    if choice2==1:
                        break
                    elif choice2==2:
                        break
                    elif choice2==3:
                        pass
                    elif choice2==4:
                        exit()
                    else:
                        print("Invalid Input")
            elif choice1==3:
                exit()
            else:
                print("Invalid Input")
            if choice2==1:
                break
    elif choice==2:
        choice4=0
        while True:
            state_data()
            choice3=int(input("\n1. View data from Official Sources\n2. View data from covid19idia.org\n3. Select a different state\n4. Exit\n"))
            if choice3==1:
                break
            elif choice3==2:
                while True:
                    unofficial_data()
                    choice4=int(input("\n1. View data from Official Sources\n2. View data of individual states\n3. Exit\n"))
                    if choice4==1:
                        break
                    elif choice4==2:
                        break
                    elif choice4==3:
                        exit()
                    else:
                        print("Invalid Input")
            elif choice3==3:
                pass
            elif choice3==4:
                exit()
            else:
                print("Invalid Input")
            if choice4==1:
                break
    elif choice==3:
        break
    else:
        print("Invalid Input")