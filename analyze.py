import csv
import matplotlib.pyplot as plt

with open('Output.txt') as csvfile:
    txtread = csv.reader(csvfile,quotechar="|")
    total=0
    arr = []
    for row in txtread:
        arr.append(list(map(lambda x:int(x,16),row[1:])))
        # print(row[:1],total)
        total += len(row)-1
        # print type(row)
        # print ', '.join(row)
    # print arr
    flat_list = [item for sublist in arr for item in sublist]
    # print flat_list
    # print (len(flat_list))
    xval = []
    for y in xrange(22):
        xval.append(y)
    fig,axes = plt.subplots(nrows=3,ncols=2)
    axes[0,0].bar(xval,flat_list[523:523+22])
    axes[0,0].set_title("1:43")
    axes[0,1].bar(xval,flat_list[2033:2033+22])
    axes[0,1].set_title("1:50")
    axes[1,0].bar(xval,flat_list[3051:3051+22])
    axes[1,0].set_title("2:30")
    axes[1,1].bar(xval,flat_list[4990:4990+22])
    axes[1,1].set_title("2:36")
    axes[2,0].bar(xval,flat_list[6521:6521+22])
    axes[2,0].set_title("2:41")

    print(flat_list[523:523+22])
    plt.show()

    # plt.bar(xval,flat_list,align='center')
    # plt.show()


    # 1:43, 523
    # 1:50, 2033
    # 2:30, 3051
    # 2:36, 4990
    # 2:41, 6521




