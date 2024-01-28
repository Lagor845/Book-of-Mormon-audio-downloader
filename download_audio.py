import requests

options = ["D&C","New Testiment","Old Testiment","Book of mormon","Peral of Great Price"]

with open("config","r") as file:
    data = file.read()
    string = data.split("\n")
    string = string[-1].split(":")
    option = options[int(string[1].strip(" "))-1]

with open("links.txt","r") as file:
    data = file.read()
    links = data.split("\n")

number = 1
for url in links:
    if url != "":
        name_temp = url.split("/")
        unabridged_file_name = name_temp[6]
        unabridged_file_name = unabridged_file_name.split("-")
        title = ""
        for num in range(3,100):
            if unabridged_file_name[num] == "male":
                break
            else:
                if num == 3:
                    title = title + unabridged_file_name[num]
                else:
                    title = title + " " + unabridged_file_name[num]
        print(f"[Downloading] {title.upper()}...")
        r = requests.get(url, allow_redirects=True)
        print("Completed")
        open(f'{option}/{number} {title.upper()}.mp3', 'wb').write(r.content)
        number += 1