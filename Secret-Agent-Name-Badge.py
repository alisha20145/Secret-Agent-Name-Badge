#Part1 : Ask for their details
name=input("Enter your real name,Agent: ")
gadget=input("Enter the name of your favourite gadget: ")

#Part 2:Store the agent's details using different data types
agent_number=9
flying_skills=8.75
is_active=True

print("Name : ",name,"Type : ----",type(name))
print("Gadget : ",gadget,"Type : ----",type(gadget))
print("Agent Number : ",agent_number,"Type : ----",type(agent_number))
print("Flying Skills : ",flying_skills,"Type : ----",type(flying_skills))
print("Is Active : ",is_active,"Type : ----",type(is_active))

#Slice the name to create a secret code name
first_three=name[0:3]
last_letter=name[-1]
code_name=first_three+last_letter
print("Secret Agent Code Name :",code_name)
agent_number=str(agent_number)
print("Agent Number : ",agent_number,"Type : ----",type(agent_number))

reversed_gadget=gadget[::-1]
print("Reversed Gadget Name :",reversed_gadget,"Type : ----",type(reversed_gadget))