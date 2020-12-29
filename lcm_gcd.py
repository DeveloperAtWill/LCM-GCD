def main_activity(x,y):  #x,y are integers
    int1 = x
    int2 = y
    remainder = x % y
    while(remainder != 0):
        x = y
        y = remainder
        remainder = x % y
    gcd = y
    lcm = int(int1 * int2 / gcd)
    return [lcm,gcd]

def general_operation(z): #z is a list containing all type of numbers except complex.
    denominator = []
    neumerator = []
    for i in range(len(z)):
        data = str(z[i]).split(".")
        if(len(data) == 2):
            denominator_of_each_element = 10**len(data[1]) / main_activity(int(data[0]), int(data[1]))[1]
            denominator.append(int(denominator_of_each_element))
            neumerator.append(int(int(data[0] + data[1]) / main_activity(int(data[0]), int(data[1]))[1]))
        else:
            denominator.append(1)
            neumerator.append(int(data[0]))
    lcm_neumerator = neumerator[0]
    gcd_denominator = denominator[0]
    for j in range(len(z) - 1):
        lcm_neumerator = main_activity(lcm_neumerator, neumerator[j+1])[0]
        gcd_denominator = main_activity(gcd_denominator, denominator[j+1])[1]
    gcd_neumerator = neumerator[0]
    lcm_denominator = denominator[0]
    for j in range(len(z) - 1):
        gcd_neumerator = main_activity(gcd_neumerator, neumerator[j+1])[1]
        lcm_denominator = main_activity(lcm_denominator, denominator[j+1])[0]
    lcm = lcm_neumerator / gcd_denominator
    gcd = gcd_neumerator / lcm_denominator
    return [lcm, gcd]
     
number_list = list(eval(input("Enter numbers in a,b,c,... format : ")))
print(f"The LCM of the entries is : {general_operation(number_list)[0]} \nThe GCD of the entries is : {general_operation(number_list)[1]}")