def main():
    ##################################################
    # Comlete your code here
    ##################################################
    """
    Use following variables to save your result
    total 
    average
    """
    val1 = int(input("Enter first value: "))
    val2 = int(input("Enter second value "))
    val3 = int(input("Enter third value: "))
    total = (val1 + val2 + val3)
    average = (int(total)) / 3
    
    print(total)
    print (f'Average: \t {average:.2f}')

    ########################################
    # Do not delete the return statement
    ########################################
    return total, average


if __name__ == '__main__':
    main()
