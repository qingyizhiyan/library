import matplotlib.pyplot,numpy,pandas,seaborn
data = numpy.array([('food',658),('shopping',394),('study',447),('entertainment',355),('other',102)],
                   dtype=[('item', 'U10'),('expense', 'i8')])
expenses = pandas.DataFrame(data)
matplotlib.pyplot.pie(expenses['expense'],labels=expenses['item'],autopct='%1.1f%%',colors=['green','yellow','orange','pink','red'])
matplotlib.pyplot.title('Expenses  Proportion')
matplotlib.pyplot.show()