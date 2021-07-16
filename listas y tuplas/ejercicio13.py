import math

nums = input("Ingrese una lista de números separados por coma: ").split(",")
sum = 0
sumsq = 0
count = len(nums)

for num in nums:
    sum += int(num)
    sumsq += int(num)**2

mean = sum/count
stdev = (sumsq/count-mean**2)**(1/2)

print(
    "La media es {} y la desviación típica es {}.".format(
        round(mean, 2), 
        round(stdev, 2)
    )
)
