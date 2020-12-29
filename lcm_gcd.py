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
            denominator_of_each_element = 10**len(data[1])
            neumerator_of_each_element = int(int(data[0] + data[1]))
            divisor = main_activity(neumerator_of_each_element,denominator_of_each_element)[1]
            denominator.append(denominator_of_each_element/divisor)
            neumerator.append(neumerator_of_each_element/divisor)
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
data  = general_operation(number_list)
print(f"The LCM of the entries is : {data[0]} \nThe GCD of the entries is : {data[1]}")
