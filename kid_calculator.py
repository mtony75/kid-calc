#----------------------------------------------
# Program by Mark Fleming
# Simple Math Calculator
# A program to help the boys check their Math
# homework. Will help Add, Subtract, Multiply, Divide
#----------------------------------------------

def menu():
    print "************************************************"
    print "* 1. Addition                                 **"
    print "* 2. Subtraction                              **"
    print "* 3. Multiplication                           **"
    print "* 4. Division                                 **"
    print "* 5. Factors                                  **"
    print "* 6. Multiples                                **"
    print "* 7. First Common Multiple                    **"
    print "************************************************"

def addition():
    addONE = retrive_numbers()
    addTWO = retrive_numbers()
    if (safety_check_numbers(addONE) and safety_check_numbers(addTWO)):
        addone = int(addONE)
        addtwo = int(addTWO)
        print "Your numbers equal: ",addone+addtwo
        raw_input("Press Any Key")
    else:
        print "One of your choices was not a number"
        raw_input("Press Any Key")

def subtraction():
    subONE = retrive_numbers()
    subTWO = retrive_numbers()
    if (safety_check_numbers(subONE) and safety_check_numbers(subTWO)):
        subone = int(subONE)
        subtwo = int(subTWO)
        print "Your difference is: ",subone-subtwo
        raw_input("Press Any Key")
    else:
        print "One or both of your choices was not a number"
        raw_input("Press Any Key")
    
def multiplication():
    mulONE = retrive_numbers()
    mulTWO = retrive_numbers()
    if (safety_check_numbers(mulONE) and safety_check_numbers(mulTWO)):
        mulone = int(mulONE)
        multwo = int(mulTWO)
        print "Your product is: ",mulone*multwo
        raw_input("Press Any Key")
    else:
        print "One or both of your choices was not a number"
        raw_input("Press Any Key")
    
def division():
    divONE = retrive_numbers()
    divTWO = retrive_numbers()
    if (safety_check_numbers(divONE) and safety_check_numbers(divTWO)):
        divone = int(divONE)
        divtwo = int(divTWO)
        print "Your quotent is: ",divone//divtwo," Remainder ",divone%divtwo
        raw_input("Press Enter")
    else:
        print "One or both of your choices was not a number"
        raw_input("Press Any Key")

def factors():
    factorONE = retrive_numbers()
    if (safety_check_numbers(factorONE)):
        factorone = int(factorONE)
        print "Your factors are: "
        for factors_loop in range(1,factorone):
            if factorone%factors_loop == 0:
                print factors_loop
        print factorone
    else:
        print "One or both of your choices was not a number"
        raw_input("Press Enter")

def multiples_of():
    multipleONE = retrive_numbers()
    multipleTWO = retrive_numbers()
    if (safety_check_numbers(multipleONE) and safety_check_numbers(multipleTWO)):
        multipleone = int(multipleONE)
        multipletwo = int(multipleTWO)
        print "The next ",multipletwo," multiples of ",multipleone," are:"
        for multiple_loop in range(2,multipletwo+2):
            print multipleone*multiple_loop
    else:
        print "One or both of your choices was not a number"
        raw_input("Press Enter")
        
def first_common_multiple():
    commonONE = retrive_numbers()
    commonTWO = retrive_numbers()
    if (safety_check_numbers(commonONE) and safety_check_numbers(commonTWO)):
        commonone = int(commonONE)
        commontwo = int(commonTWO)
        if (commonone > commontwo):
            the_common = find_common(commonone,commontwo)
        elif (commonone < commontwo):
            the_common = find_common(commontwo,commonone)
        else:
            the_common = commonone
        print "The common multiple of ",commonone," and ",commontwo," is ",the_common
    else:
        print "one or both of your choices was not a number"
        raw_input("Press Enter")

def find_common(first_number,second_number):
    loop = 1
    newfirst_number = first_number
    newsecond_number = second_number
    while (loop == 1):
        if (newsecond_number > newfirst_number):
            newfirst_number = newfirst_number+first_number
        elif (newsecond_number < newfirst_number):
            newsecond_number = newsecond_number+second_number
        else:
            loop = 0
#        print "1 = ",newfirst_number
#        print "2 = ",newsecond_number
    return(newfirst_number)
    
def retrive_numbers():
    print "Please Give me a number"
    numberONE = raw_input("Enter Number: ")
    return numberONE
    
def safety_check_numbers(dirty_number):
    try: 
        int(dirty_number)
        return True
    except ValueError:
        return False
    
# Main Program Function
def main():
    menu_loop = 1
    while menu_loop == 1:
        print "Welcome to the Kid Calculator."
        menu()
        menu_slection = raw_input("Choose A Mathmatical Function: ")
        if menu_slection == "1":
            addition()
        elif menu_slection == "2":
            subtraction()
        elif menu_slection == "3":
            multiplication()
        elif menu_slection == "4":
            division()
        elif menu_slection == "5":
            factors()
        elif menu_slection == "6":
            multiples_of()
        elif menu_slection == "7":
            first_common_multiple()
        else:
            menu_loop = 0
        
    
    
    



# Main Program Block
main()
