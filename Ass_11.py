import matplotlib.pyplot as graph
import pandas as pand 
dataMpg = pand.read_csv('Z:\Documents\_INF 354\Assignment 11\Assignment_11\mpg.csv')

#Add column of price per person
dataMpg ['Displacement_Per_Sec'] = dataMpg['displacement']/dataMpg['acceleration']

print('_________Display Dispalcement Per Accelleration___________________________________________________________')
print(dataMpg)

#Conditional
light = dataMpg['weight'] < 3300

print('_________Display Display weight under 3300 lbs______________________________________________________________')
print(dataMpg[light])

#Correlation
dataMpg['Cor_Co_Effecient'] = dataMpg['weight'].corr(dataMpg['horsepower'])

print('_________display Cor Co-Eff__________________________________________________________________________________')
print(dataMpg)

#Plot graph
graph.bar(dataMpg['weight'], dataMpg['mpg'], color='purple', width= 125)
graph.title('How weight influences the Mile Per Gallon')
graph.xlabel('weight(lbs)')
graph.ylabel('MPG')
#graph.plot(dataMpg['weight'], dataMpg['mpg']- dataMpg['weight'], color='orange')

#Display graph
graph.show()
