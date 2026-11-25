#=============================== Leafpaw's Medicine Cat tracker ==================================
print("=============================== Leafpaw's Medicine Cat tracker ==================================")
print("For those of you who are total Leafpool Ctats not to offend you but i think i like her as a kit better (Sorry for the get to work on squirrelflight but i thin i did good with naming t he variables after her & her mate.")
print()
medicine = ("Completing all medicine tasks (also reading cause its the best and taking care of my naughty sister Squirrelpaw)", True, 21, 27.9)
print(medicine)
H1= int(input("Enter 1 for completed medicine day and 0 for incomplete medicine day: "))
H2= int(input("Enter 1 for completed medicine day and 0 for incomplete medicine day: "))
print("Your weeklymedicine cat habits will appear as 1 fo cmpleted and 0 for incompleted")
weekly_habits = (H1, H2)
print(weekly_habits)
Leafpaw= input("Have you added all your medicine cat days (Y/N): ")
if Leafpaw == "N":
    H3= int(input("Enter 1 for completed medicine day and 0 for incomplete medicine day: "))
    forwards= input("Do you want to add more days (Y/N): ")
    if forwards == "Y":
       print("re run code to add another day") 

    weekly_habits = weekly_habits + (H3,)
    print("After adding one more day:", weekly_habits)

print("Total days tracked:", len(weekly_habits))
 
print("Day 1 status:", weekly_habits[0])
print("Day 4 status:", weekly_habits[3])
 

first_three_days = weekly_habits[0:3]
print("First three days:", first_three_days)
 
weekend_days = weekly_habits[5:7]
print("Weekend days:", weekend_days)

 

completed = weekly_habits.count(1)
missed = weekly_habits.count(0)
 
print("Completed days:", completed)
print("Missed days:", missed)
 

done = 0
not_done = 0
 
for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        done += 1
    else:
        not_done += 1
 
if done > not_done:
    print("Great habit progress!")
else:
    print("Try to be more consistent!")
 

print("")
print("===== WEEKLY HABIT TRACKER =====")
print("Habit Name:", [0])
print("Weekly Record:", weekly_habits)
print("Completed:", done)
print("Missed:", not_done)
print("================================")
