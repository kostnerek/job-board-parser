import json

#check if file.json exists if not create it
def checkIfFileExist(file:str):
    try:
        with open(f"data/{file}.json", encoding='utf8') as json_file:
            pass
    except:
        with open(f"data/{file}.json", 'w', encoding='utf8') as outfile:
            json.dump({}, outfile, ensure_ascii=False)


def parseData(file:str, job_title, company, salary, working_place, link, print_messages = False):
    checkIfFileExist(file)
    company_buff= company
    data={}
    with open(f"data/{file}.json", encoding='utf8') as json_file:
        data = json.load(json_file)
    c=0
    for company_buff in data:
        for y in data[company_buff]:
            c=int(y)+1
    #check if company exists in data dict if not create 
    if company not in data:
        data[company] = {}
        c=0
    else:
        c=int(list(data[company].keys())[-1])+1
    #check if new job appeared
    duplicate=False
    for x in data[company]:
        job = data[company][x]
        try:
            if job['job_title'] == job_title:
                if print_messages == True:
                    print('nothing new')    
                duplicate=True
                break
        except:
            pass
    #if not exist create new job entry
    if duplicate != True:
        data[company][c] = {'job_title': job_title, 'salary': salary, 'working_place': working_place, 'link': link}
        #notify
        if print_messages == True:
            print(f"New job on {file}")
    c+=1
    with open(f"data/{file}.json", 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)