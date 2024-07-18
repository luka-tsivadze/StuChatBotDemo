import json

with open('data/raw data/faculties.json', 'r', encoding='utf-8') as file:
    faculty_data = json.load(file)

def degree_language_detector(level, language): #ქართულ ფორმატში გარდაქმნა
    if level == "bachelor":
        degree = "საბაკალავრო"
    elif level == "magister":
        degree = "სამაგისტრო"
    elif level == "doctorate":
        degree = "სადოქტორო"
    else:
        degree = "შეფერხება"
    
    if language == "georgian":
        lang = "ქართულენოვანი"
    elif language == "english":
        lang = "ინგლისურენოვანი"
    elif language == "russian":
        lang = "რუსულენოვანი"
    else:
        lang = "შეფერხება"
    
    return degree, lang


def programs_adder(faculty): #პროგრამების ერთ სიაში დამატება
    programs = []

    for level in ["bachelor", "magister", "doctorate"]:
        for language in ["georgian", "english", "russian"]:
            if faculty["programs"][level][language]:  # Check if list is not empty
                degree, lang = degree_language_detector(level, language)
                programs.append(f"\n{degree} {lang} პროგრამები: ")
                programs.extend(faculty["programs"][level][language])

    return "\n".join(programs), len(programs)


def extract_qa_pairs(data):
    qa = []
    facs = []
    for faculty in data["faculties"]:
        programs = programs_adder(faculty)
        # qa.append([,])
        qa.append(
            [f"{faculty["name"]}", #ფაკულტეტის შესახებ
             f"{faculty["name"]}ს დეკანია {faculty["dean"]}, ვინც ამბობს: {faculty["phrase"]}.\n\nფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}\n\nფაკულტეტის შესახებ 10 ფაქტია: \n{"\n".join(faculty["10-facts"])}"])
        
        qa.append(
            [f"რა იცი {faculty["name"][0:-1]}-ზე?", #ფაკულტეტის შესახებ
             f"{faculty["name"]}ს დეკანია {faculty["dean"]}, ვინც ამბობს: {faculty["phrase"]}.\n\nფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}\n\nფაკულტეტის შესახებ 10 ფაქტია: \n{"\n".join(faculty["10-facts"])}"])
        
        qa.append(
            [f"რა იცი {faculty["name"]}ს შესახებ?", #ფაკულტეტის შესახებ
             f"{faculty["name"]}ს დეკანია {faculty["dean"]}, ვინც ამბობს: {faculty["phrase"]}.\n\nფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}\n\nფაკულტეტის შესახებ 10 ფაქტია: \n{"\n".join(faculty["10-facts"])}"])
        
        qa.append(
            [f"მითხარი {faculty["name"]}ს შესახებ?", #ფაკულტეტის შესახებ
             f"{faculty["name"]}ს დეკანია {faculty["dean"]}, ვინც ამბობს: {faculty["phrase"]}.\n\nფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}\n\nფაკულტეტის შესახებ 10 ფაქტია: \n{"\n".join(faculty["10-facts"])}"])
        
        qa.append(
            [f"რა პროგრამებია {faculty["name"][0:-1]}ში?", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"გთხოვ მითხარი რა პროგრამებია {faculty["name"][0:-1]}ში?", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"გთხოვ მითხარი {faculty["name"][0:-1]}ში არსებული პროგრამების შესახებ", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"რა პროგრამები არსებობს {faculty["name"][0:-1]}ში?", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"რა სასწავლო პროგრამები არსებობს {faculty["name"][0:-1]}ში?", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"რა პროგრამები ფუნქციონირებს {faculty["name"][0:-1]}ში?", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"რა პროგრამებია აქტიური {faculty["name"][0:-1]}ში?", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"რა სასწავლო პროგრამებია აქტიური {faculty["name"][0:-1]}ში?", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"გთხოვ მითხარი {faculty["name"][0:-1]}ში არსებული აქტიური პროგრამების შესახებ", #პროგრამების შესახებ ფაკულტეტში
             f"ფაკულტეტში არსებობს {programs[1]} პროგრამა: {programs[0]}"])
        
        qa.append(
            [f"რამდენი პროგრამა აქვს {faculty["name"][0:-1]}ს?", #პროგრამების რაოდენობა ფაკულტეტში
             f"{faculty["name"][0:-1]}ს აქვს {programs[1]} სასწავლო პროგრმა"])
        
        qa.append(
            [f"რამდენი სასწავლო პროგრამა აქვს {faculty["name"][0:-1]}ს?", #პროგრამების რაოდენობა ფაკულტეტში
             f"{faculty["name"][0:-1]}ს აქვს {programs[1]} სასწავლო პროგრმა"])
        
        qa.append(
            [f"გთხოვ მითხარი რამდენი სასწავლო პროგრამა აქვს {faculty["name"][0:-1]}ს?", #პროგრამების რაოდენობა ფაკულტეტში
             f"{faculty["name"][0:-1]}ს აქვს {programs[1]} სასწავლო პროგრმა"])
        
        qa.append(
            [f"რამდენი სასწავლო პროგრამა ფუნქციონირებს {faculty["name"][0:-1]}ში?", #პროგრამების რაოდენობა ფაკულტეტში
             f"{faculty["name"][0:-1]}ში ფუნქციონირებს {programs[1]} სასწავლო პროგრმა"])
        
        qa.append(
            [f"რამდენი აქტიური პროგრამაა {faculty["name"][0:-1]}ში?", #პროგრამების რაოდენობა ფაკულტეტში
             f"{faculty["name"][0:-1]}ში აქტიურია {programs[1]} სასწავლო პროგრმა"])
        
        qa.append(
            [f"{faculty["name"][0:-1]}ში რამდენი აქტიური პროგრამაა?", #პროგრამების რაოდენობა ფაკულტეტში
             f"{faculty["name"][0:-1]}ში აქტიურია {programs[1]} სასწავლო პროგრმა"])
        
        qa.append(
            [f"{faculty["name"][0:-1]}ში რამდენი პროგრამაა?", #პროგრამების რაოდენობა ფაკულტეტში
             f"{faculty["name"][0:-1]}ში აქტიურია {programs[1]} სასწავლო პროგრმა"])
        
        qa.append(
            [f"იცი რამდენი პროგრამა აქვს {faculty["name"][0:-1]}ს?", #პროგრამების რაოდენობა ფაკულტეტში
             f"{faculty["name"][0:-1]}ს აქვს {programs[1]} სასწავლო პროგრმა"])
        
        qa.append(
            [f"ვინ არის {faculty["name"]}ს დეკანი?", #ფაკულტეტის დეკანი
            f"{faculty["name"]}ს დეკანია {faculty["dean"]}"])
        
        qa.append(
            [f"ვინ არის {faculty["name"]}ს დეკანი სტუ-ში?", #ფაკულტეტის დეკანი
            f"{faculty["name"]}ს დეკანია {faculty["dean"]}"])
        
        qa.append(
            [f"ვინ არის {faculty["name"]}ს ამჟამინდელი დეკანი?", #ფაკულტეტის დეკანი
            f"{faculty["name"]}ს დეკანია {faculty["dean"]}"])
        
        qa.append(
            [f"ვინ არის დეკანი {faculty["name"][0:-1]}ზე?", #ფაკულტეტის დეკანი
            f"{faculty["name"]}ს დეკანია {faculty["dean"]}"])
        
        qa.append(
            [f"ვინ არის ამჟამად {faculty["name"]}ს დეკანი?", #ფაკულტეტის დეკანი
            f"{faculty["name"]}ს ამჟამინდელი დეკანია {faculty["dean"]}"])
        
        qa.append(
            [f"გთხოვ მითხარი ვინ არის {faculty["name"]}ს დეკანი?", #ფაკულტეტის დეკანი
             f"{faculty["name"]}ს დეკანია {faculty["dean"]}"])
        
        qa.append(
            [f"იცი ვინ არის {faculty["name"]}ს დეკანი?", #ფაკულტეტის დეკანი
             f"{faculty["name"]}ს დეკანია {faculty["dean"]}"])
        
        qa.append(
            [f"რა არის {faculty["name"]}ს შესახებ 10 ფაქტი?", #ფაკულტეტის დეკანი
             f"{"\n".join(faculty["10-facts"])}"])
        
        qa.append(
            [f"რატომ {faculty["name"]}?", #ფაკულტეტის დეკანი
             f"{"\n".join(faculty["10-facts"])}"])
        
        qa.append(
            [f"რა შეღავათებია {faculty["name"][0:-1]}ში?", #ფაკულტეტის დეკანი
             f"{"\n".join(faculty["10-facts"])}"])
        
        qa.append(
            [f"რატომაა კარგი {faculty["name"]}?", #ფაკულტეტის დეკანი
             f"{"\n".join(faculty["10-facts"])}"])

        facs.append(f"{faculty["id"]}- {faculty["name"]}") #ფაკულტეტის სია

    qa.append(["საქართველოს ტექნიკურ უნივერსიტეტის ფაკულტეტები?", f"სტუ-ს აქვს {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["სტუ-ის ფაკულტეტები?", f"სტუ-ს აქვს {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["ფაკულტეტები?", f"სტუ-ს აქვს {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["რამდენი ფაკულტეტი აქვს საქართველოს ტექნიკურ უნივერსიტეტს?", f"სტუ-ს აქვს {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["რამდენი ფაკულტეტი არსებობს საქართველოს ტექნიკურ უნივერსიტეტს?", f"სტუ-ს აქვს {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["რამდენი ფაკულტეტი ფუნქციონირებს საქართველოს ტექნიკურ უნივერსიტეტს?", f"სტუ-ს აქვს {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["საქართველოს ტექნიკურ უნივერსიტეტში რამდენი ფაკულტეტია?", f"სტუ-ს აქვს {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["გთხოვ მითხარი რამდენი ფაკულტეტი აქვს საქართველოს ტექნიკურ უნივერსიტეტს?", f"სტუ-ს აქვს {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["რამდენი ფაკულტეტი არის აქტიური საქართველოს ტექნიკურ უნივერსიტეტში?", f"სტუ-ში აქტიურია {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["სტუში რამდენი ფაკულტეტია?", f"სტუ-ში აქტიურია {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["რამდენი ფაკულტეტია სტუში?", f"სტუ-ში აქტიურია {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["რამდენი ფაკულტეტია საქართველოს ტექნიკურ უნივერსიტეტში?", f"სტუ-ში აქტიურია {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    qa.append(["რამდენი ფაკულტეტი გაქვთ?", f"სტუ-ში აქტიურია {len(facs)} ფაკულტეტი: \n{"\n".join(facs)}"]) #ფაკულტეტების რაოდენობა
    return qa

qa = extract_qa_pairs(faculty_data)
new_data = []
for i in range(len(qa)):
    new_data.append({
        "question": qa[i][0],
        "answer": qa[i][1]
    })
    
with open('data/qa-dataset/faculties-qa.json', 'w', encoding='utf-8') as json_file:
    json.dump(new_data, json_file, ensure_ascii=False, indent=4)