def calculate(r, unit, arr, n):
    if arr is None or n == 0:
        return -1 
    
    totalfoodRequired = r*unit 
    foodTillNow = 0 
    
    for house in range(n):
        foodTillNow += arr[house]
        if foodTillNow >= totalfoodRequired:
            return house + 1 
    return 0 

r = int(input("Enter number of rats: "))
unit = int(input("Enter the value of units: "))
n = int(input("Number of elements in a array: "))
arr = list(map(int, input("List elements with space separated: ").split()))
print(calculate(r, unit, arr, n))