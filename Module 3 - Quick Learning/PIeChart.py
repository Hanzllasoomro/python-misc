import matplotlib.pyplot as pyplot


labels = ("python", "java", "C++", "PHP", "Scala")
sizes = [45 , 10 , 15, 30, 22]

pyplot.pie(sizes, labels=labels, autopct='%1.1f%%', counterclock=False, startangle=105)

pyplot.show()