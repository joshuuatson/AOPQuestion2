import math
import numpy as np
import random
import matplotlib.pyplot as plt
N = int(input("How many iterations would you like to run?  "))
print("The true value of ln(2) is ", math.log(2))

iterations = []
results = []
xvalues = []
yvalues = []
count_in = 0
for i in range (N ):
    x = random . random ()
    y = random . random ()
    xvalues.append(x)
    yvalues.append(y)    

    outcome = 1 if y <= 1/(x+1) else 0
    count_in += outcome
    fraction_in = count_in /( i +1)
    results . append (fraction_in )
    iterations . append (i +1)

print("the best approximation to ln(2) is ", results[-1])

fig = plt . figure ()
plt . plot ( iterations , results , label =" numerical ln(2) ")
plt . plot ([0 , iterations [ -1]] , [ math .log(2) , math . log(2) ],
            label =" ln(2) ")


plt . grid ( True )
plt . legend ()
plt.ylim(0,1)
plt . ylabel ("Result")
plt . xlabel ("Iteration")
plt . title("Plot of approximation against number of iterations")

plt . show ()


plt.rcParams["figure.figsize"] = [7.00, 7.00]
plt.rcParams["figure.autolayout"] = True
fig2 = plt.figure()
plt.grid(True)
x = np.linspace(0,1, 10000)
y = 1/(x+1)
plt.plot(x, y, label = "1/x plot")
plt.fill_between(x,y, color='pink', alpha=.2)
plt.plot(xvalues, yvalues, ",", linewidth=.5, label = "random coordinates")
plt.legend(loc='upper right')
plt.title("Plot of randomly generated coordinates")
plt.show()

input(print("press ENTER to finish"))

