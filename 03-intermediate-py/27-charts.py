import matplotlib.pyplot as plt 


def generate_bar_chart(labels, values): 
    print('Charts!')
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values): 
    print('Charts!')
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()



if __name__ == '__main__': 
    labels = ['a','b', 'c']
    values = [100,300, 80]
    generate_pie_chart(labels, values)