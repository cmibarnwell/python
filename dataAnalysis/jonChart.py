import matplotlib.pyplot as plt

#open the data file
c = open('data.txt', 'r')

x = []
y = []
i = 0

line = c.readline()
while(line != ''):
    i+=1
    line = int(line)
    x.append(i)
    y.append(line)
    line = c.readline()

j = open('jonData.txt', 'r')

x1 = []
y1 = []
i1 = 0

line1 = j.readline()
while(line1 != ''):
    i1+=1
    line1 = int(line1)
    x1.append(i1)
    y1.append(line1)
    line1 = j.readline()





plt.bar(x, y, label = "Caleb", color = '#181127')
plt.bar(x1, y1, label = "Jon", color = 'r')
plt.ylabel('Minutes between Coffee and Bowel Movement')
plt.xlabel('Days Elapsed')


plt.title("Jon's request")

plt.legend()

plt.show()
