import matplotlib.pyplot as plot
import pandas as pand 
dataMpg = pand.read_csv('Z:\Documents\_INF 354\Assignment 11\Assignment_11\mpg.csv')

#Add column of price per person
dataMpg ['Displacement_Per_Sec'] = dataMpg['displacement']/dataMpg['acceleration']

#Conditional
light = dataMpg['weight'] < 3300



#Correlation
dataMpg['Cor_Co_Effecient'] = dataMpg['weight'].corr(dataMpg['horsepower'])

print(dataMpg[light])

#Plot
plot.plot(dataMpg['weight'], dataMpg['mpg'], 'ro')
plot.title('How weight influences the Mile Per Gallon')
plot.xlabel('weight')
plot.ylabel('MPG')

#Display
plot.show()
