import csv

fields = ["Kunst", "Gesellschaft", "MINT", "Musik", "Sprache", "Sport"]
choices = {"Kunst":{}, "Gesellschaft":{}, "MINT":{}, "Musik":{}, "Sprache":{}, "Sport":{}}

with open('wu.csv', newline='',encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile,delimiter=';',quotechar='"')
    for row in reader:
        #print(row)
        #print(row['Name2'], row['Klasse'])
        # Hier nun für jeden Schüler (row) die Liste an Wahlunterichten durchgehen
        # und in ein Dict von Wahlunterrichten, jeweils dem Array von Schülern den aktuellen
        # Schüler hinzufügen
        for field in fields:
            if row[field]:
                userchoices = row[field].split(';')
                userchoices.pop()
                for uc in userchoices:
                    if uc in choices[field]:
                        choices[field][uc].append([row['Name2'], row['Klasse']])
                    else:
                        choices[field][uc] = [[row['Name2'], row['Klasse']]]
                    
#Ausgabe der einzelnen Elemente des WU-Dicts, jeweils eine Liste mit Name und Klasse 
f = open("Wahlunterrichte.txt", "w", encoding="utf-8")
for choice in choices:
    for mcoption in choices[choice]:
        #print(mcoption, end="\n")
        #print("-----")
        f.write("\n"+mcoption+"\n")
        f.write("-----\n")
        for user in choices[choice][mcoption]:
            #print(user[0], ", ", user[1], sep="", end="\n")
            f.write(user[0]+", "+user[1]+"\n")
        #print("\n")
        f.write("\n")
f.close()