import json

with open('data/raw data/rectors.json', 'r', encoding='utf-8') as file:
    rector_data = json.load(file)


def extract_qa_pairs(data):
    qa = []
    rectors = []
    for rector in data["rectors"]:
        if rector["id"] == 14:
            iyo_aris = "არის"
            wlebi = ""
            mogvaweoba = "მოღვაწეობს"
        else:
            iyo_aris = "იყო"
            wlebi = " წლებში"
            mogvaweoba = "მოღვაწეობდა"

        qa.append(
            [f"ვინ იყო სტუ-ის {rector["rector"]}?", #რექტორის შესახებ
            f"უნივერსიტეტის {rector["rector"]} {iyo_aris} {rector["name"]}, რომელიც ამ თანამდებობაზე {mogvaweoba} {rector["date"]}{wlebi}."])
        
        qa.append(
            [f"{rector["rector"]}", #რექტორის შესახებ
            f"უნივერსიტეტის {rector["rector"]} {iyo_aris} {rector["name"]}, რომელიც ამ თანამდებობაზე {mogvaweoba} {rector["date"]}{wlebi}."])
        
        qa.append(
            [f"ვინ იყო საქართველოს ტექნიკური უნივერსიტეტის {rector["rector"]}?", #რექტორის შესახებ
            f"უნივერსიტეტის {rector["rector"]} {iyo_aris} {rector["name"]}, რომელიც ამ თანამდებობაზე {mogvaweoba} {rector["date"]}{wlebi}."])
        
        qa.append(
            [f"ვინ არის სტუ-ის {rector["rector"]}?", #რექტორის შესახებ
            f"უნივერსიტეტის {rector["rector"]} {iyo_aris} {rector["name"]}, რომელიც ამ თანამდებობაზე {mogvaweoba} {rector["date"]}{wlebi}."])
        
        qa.append(
            [f"ვინ არის საქართველოს ტექნიკური უნივერსიტეტის {rector["rector"]}?", #რექტორის შესახებ
            f"უნივერსიტეტის {rector["rector"]} {iyo_aris} {rector["name"]}, რომელიც ამ თანამდებობაზე {mogvaweoba} {rector["date"]}{wlebi}."])
        
        qa.append(
            [f"ვინ იყო {rector["date"]}{wlebi} საქართველოს ტექნიკური უნივერსიტეტის რექტორი?", #რექტორის შესახებ
            f"{rector["date"]}{wlebi} უნივერსიტეტის რექტორი {iyo_aris} {rector["name"]}"])
        
        qa.append(
            [f"ვინ იყო {rector["date"]}{wlebi} სტუ-ის რექტორი?", #რექტორის შესახებ
            f"{rector["date"]}{wlebi} უნივერსიტეტის რექტორი {iyo_aris} {rector["name"]}"])
        
        qa.append(
            [f"ვინ არის {rector["date"]}{wlebi} საქართველოს ტექნიკური უნივერსიტეტის რექტორი?", #რექტორის შესახებ
            f"{rector["date"]}{wlebi} უნივერსიტეტის რექტორი {iyo_aris} {rector["name"]}"])
        
        qa.append(
            [f"ვინ არის {rector["date"]}{wlebi} სტუ-ის რექტორი?", #რექტორის შესახებ
            f"{rector["date"]}{wlebi} უნივერსიტეტის რექტორი {iyo_aris} {rector["name"]}"])
        
        qa.append(
            [f"ვინ იყო {rector["name"]}?", #რექტორის შესახებ
            f"{rector["name"]} {iyo_aris} უნივერსიტეტის {rector["rector"]}.\n\t{rector["description"]}"])
        
        qa.append(
            [f"{rector["rector"]}-ის შესახებ", #რექტორის შესახებ
            f"უნივერსიტეტის {rector["rector"]} {iyo_aris} {rector["name"]}, რომელიც ამ თანამდებობაზე {mogvaweoba} {rector["date"]}{wlebi}."])
        
        qa.append(
            [f"ვინ არის {rector["name"]}?", #რექტორის შესახებ
            f"{rector["name"]} {iyo_aris} უნივერსიტეტის {rector["rector"]}.\n\t{rector["description"]}"])
        
        qa.append(
            [f"რა იცი {rector["name"]}-ის შესახებ?", #რექტორის შესახებ
            f"{rector["name"]} {iyo_aris} უნივერსიტეტის {rector["rector"]}.\n\t{rector["description"]}"])
        
        qa.append(
            [f"მითხარი {rector["name"]}-ის შესახებ?", #რექტორის შესახებ
            f"{rector["name"]} {iyo_aris} უნივერსიტეტის {rector["rector"]}.\n\t{rector["description"]}"])
        
        qa.append(
            [f"{rector["name"]}-ის შესახებ?", #რექტორის შესახებ
            f"{rector["name"]} {iyo_aris} უნივერსიტეტის {rector["rector"]}.\n\t{rector["description"]}"])

        rectors.append(f"{rector["id"]}- {rector["name"]}- {rector["date"]}") #რექტორის სია

    qa.append(["რამდენი რექტორი ჰყავდა საქართველოს ტექნიკურ უნივერსიტეტს?", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["რექტორები", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["რამდენი რექტორი მოღვაწეობდა საქართველოს ტექნიკურ უნივერსიტეტში?", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["რამდენი რექტორი ჰყავდა სტუ-ში?", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["რამდენი რექტორი მოღვაწეობდა სტუ-ში?", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["ჩამომითვალე საქართველოს ტექნიკური უნივერსიტეტის რექტორები?", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["საქართველოს ტექნიკური უნივერსიტეტის რექტორები?", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["ჩამომითვალე სტუ-ის რექტორები?", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["სტუ-ის რექტორები?", f"სტუ-ს დღემდე ჰყავდა {len(rectors)} რექტორი: \n{"\n".join(rectors)}"]) #რექტორების რაოდენობა
    qa.append(["ვინ არის საქართველოს ტექნიკური უნივერსიტეტის რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["ვინ არის სტუ-ის რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["ვინ არის სტუ-ის დღევანდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["ვინ არის სტუ-ის ახლანდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["ვინ არის სტუ-ის ამჟამინდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["ვინ არის საქართველოს ტექნიკური უნივერსიტეტის დღევანდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["ვინ არის საქართველოს ტექნიკური უნივერსიტეტის ამჟამინდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["საქართველოს ტექნიკური უნივერსიტეტის დღევანდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["საქართველოს ტექნიკური უნივერსიტეტის ამჟამინდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["სტუ-ის დღევანდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    qa.append(["სტუ-ის ამჟამინდელი რექტორი?", f"სტუ-ის რექტორად მოღვაწოებს 2020 წლიდან დღემდე პროფესორი დავით გურგენიძე"]) #დღევანდელი რექტორი
    return qa

qa = extract_qa_pairs(rector_data)
new_data = []
for i in range(len(qa)):
    new_data.append({
        "question": qa[i][0],
        "answer": qa[i][1]
    })
    
with open('data/qa-dataset/rectors-qa.json', 'w', encoding='utf-8') as json_file:
    json.dump(new_data, json_file, ensure_ascii=False, indent=4)