import matplotlib.pyplot,numpy,pandas,seaborn
data = numpy.array([('food',658),('shopping',394),('study',447),('entertainment',355),('other',102)],
                   dtype=[('item', 'U10'),('expense', 'i8')])
expenses = pandas.DataFrame(data)
matplotlib.pyplot.bar(expenses['item'],expenses['expense'],color=['green','yellow','orange','pink','red'])
matplotlib.pyplot.xlabel('Item')
matplotlib.pyplot.ylabel('Expenses')
matplotlib.pyplot.title('Amy living expenses')
matplotlib.pyplot.show()