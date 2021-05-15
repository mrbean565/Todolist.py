#Hello this is my to do list tool.

#This will allow users to add and store simple tasks.


print("To Do List Tool.")
print("------------------------------------------------------------------------------------")
print("Credit: Bean!!! aka Trucker Bean")

#This will be a commad line system that will collect the to list info and then print it to the screen.
#It will allow users to upon running the file ask something like this Do you want to add something to the to do list, or view the to list.


print("Would you like to Add To The To-Do-List or View The To-Do-List?")
choice = input("Respond with add or view now.")

if choice == 'add':
 print("You have picked add")
 additem = input("Please Type What You Want To Add")
 print(f"Thanks {additem} has been added.")



elif choice == 'view':
       print("You have picked View") 
       print(additem)

else: 
    print("Not a valid option")
    print("Now Ending Please Re Run Code To Try Again...")
