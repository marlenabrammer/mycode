counter= 0
with open("dracula.txt","r") as text:
    with open("vampytimes.txt","w") as text2:
        for line in text:
            if "vampire" in line.lower():
                counter+=1
                print(line)
                text2.write(line)

print(counter)
