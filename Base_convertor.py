"""
This code asks the user for a number and a required base.
And converts the number to the required base. 
"""
def main():
    Baseten = int(input("Your Base 10 number: "))
    base_required = int(input("Your base to convert to: "))
    remainder_list = Binary_converter(Baseten, base_required) #call Binary converter function.
    Binary_str = string_from_integer_list(remainder_list)
    print (Binary_str)

def Binary_converter(Baseten, base_required):
    remainder_list = [] #create a new list to append the remainders to.
    new_num = Baseten // base_required #New_num is the number you get after each division
    remainder = Baseten % base_required #remainder is the remainder you get after each division
    remainder_list.append(remainder) #adds the remainder to the a list
    while new_num >= remainder:
        Baseten = new_num # Baseten should take the value of new_num
        new_num = Baseten // base_required 
        remainder = Baseten % base_required
        remainder_list.append(remainder) 
    binary_length = len(remainder_list) #get the length of the Binary number.
    remainder_list.reverse() #reverses the order of elements in a list
    return remainder_list

def string_from_integer_list(remainder_list): # converts a list of intergers into strings.
    Binary_str = ""
    for x in remainder_list: 
        str_mode = str(x)
        Binary_str += str_mode
    return Binary_str

if __name__ == '__main__':
    main()