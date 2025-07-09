import matplotlib.pyplot as plt

labels = ("python", "java", "C++", "PHP", "Scala")
index = (1,2,3,4,5)
sizes = [45 , 10 , 15, 30, 22]

plt.bar(index,sizes, tick_label=labels)

plt.xlabel("programming language")
plt.ylabel("usage")

plt.show()