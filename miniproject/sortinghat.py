 

house_counter={'gryffindor':0,'ravenclaw':0,'huffelpuff':0, 'slytherin':0}

question1 = input("Enter the number of your favorite color?:\n1) Maroon\n2) Blue\n3) Yellow\n4) Green\n")

if question1=='1':
    house_counter['gryffindor']+=1
elif question1=='2':
    house_counter['ravenclaw']+=1
elif question1=='3':
    house_counter['huffelpuff']+=1
elif question1=='4':
    house_counter['slytherin']+=1
else: 
    print("Invalid input")


question2 = input("Which of your skills are you most proud of?\n1)My ability to make new friends.\n2)My ability to absorb new information\n3)My ability to keep secrets.\n4)My ability to get what I want.\n")

if question2=='1':
    house_counter['gryffindor']+=1
elif question2=='2':
    house_counter['ravenclaw']+=1
elif question2=='3':
    house_counter['huffelpuff']+=1
elif question2=='4':
    house_counter['slytherin']+=1
else:
    print("Invalid input")


question3 = input("Pick one word to describe yourself:\n1)Brave\n2)Clever\n3)Patient\n4)Determined\n")

if question3=='1':
    house_counter['gryffindor']+=1
elif question3=='2':
    house_counter['ravenclaw']+=1
elif question3=='3':
    house_counter['huffelpuff']+=1
elif question3=='4':
    house_counter['slytherin']+=1
else:
    print("Invalid input")

#print(house_counter.values())
max_value = max(house_counter,key=house_counter.get)
print("Your house is " + max_value + "!!!!!!!")
