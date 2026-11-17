def wait():
    """
    Good example of a function, it is used multiple times in this code
    """
    input("\nPress Enter to Continue")
    print("==============================\n")







# Variables
lat = 26.96578211
latitude = 26.96578211
URL = "www.google.com"
fruit_list = ["Apple", "Orange", "Banana", "Potato"]


print("Latitude", latitude)
print("URL", URL)
print("Fruits", fruit_list)





#==============================================
wait()
#==============================================





# If/Else

# Simple Example - Option 1
if type(latitude) == float:
    if latitude > 25:
        if latitude < 30:
            print("Satelite in View")
        else:
            print("Satelite not in View")
    else:
        print("Satelite not in View")
else:
    print("Satelite not in View")


wait()







# Option 2 - If statements flattened:
if type(latitude) == float and latitude > 25 and latitude < 30:
    print("Satelite in View")
else:
    print("Satelite not in View")







# Option 3 - Advanced Example - Negative programming, rule out parts 
# -> (only works in functions because you can exit the funciton at any point):
def detect_satelite(latitude):
    if not type(latitude) == float:
        print("Latitude Value is not Float")
        return
    if latitude <= 25:
        print("Latitude is too low")
        return
    
    if latitude >= 30:
        print("Latitude is too high")
        return
    
    print("Satelite in View")
detect_satelite(25)





#==============================================
wait()
#==============================================





# Loops
# Example 1
print("Loop:", 0)
print("Loop:", 1)
print("Loop:", 2)
print("Loop:", 3)
print("Loop:", 4)




#==============================================
wait()
#==============================================




# Example 2
for index in range(5):
    print("Loop:", index)




#==============================================
wait()
#==============================================




# Example 3
for fruit in fruit_list:
    print(fruit)




#==============================================
wait()
#==============================================




# Example 4, combining for loops and if/else statements
for fruit in fruit_list:
    if fruit == "Potato":
        print("A potato is not a fruit")
    else:
        print("Our fruit is", fruit)





#==============================================
wait()
#==============================================





# Functions (Reusable code blocks)

number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
sum1 = number1 + number2
print("Sum1: ", sum1, "\n")

number3 = int(input("Enter number: "))
number4 = int(input("Enter number: "))
sum2 = number3 + number4
print("Sum2: ", sum2, "\n")



#==============================================
wait()
#==============================================




def add_numbers():
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    number_sum = number1 + number2
    print("Our sum is: ", number_sum, "\n")

add_numbers()
add_numbers()
