import matplotlib.pyplot as plt
from numpy import *
from datetime import datetime
from matplotlib.pyplot import grid, figure, plot, savefig
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容'
epochlist=[]#存放数据
statelist=[]
def read_file(filename):
    with open(filename,"rt",encoding="ansi") as f:
        alllines=f.readlines()
    print(len(alllines))
    form=alllines[0][0:9]   #获取文件格式,第一行
    str2=alllines[1][15:-1] #获取开始时间，第二行
    str2=str2[0:19]
    start_time=datetime.strptime(str2, '%Y %m %d %H %M %S')
    print(start_time)
    #///read values///
    for i in range(2,len(alllines),2):
        svlist=[] #存放卫星编号,但每次都是通过读取后面卫星编号所处的位置的字符串得到，有时候就是空列表，所以需要定义全局变量，statelist
        line=alllines[i]#这一行需要加判断
        str=line.replace("  ",' ')
        str=str.replace("  ",' ')
        str=str.replace("  ",' ')#一点一点的消除每一行前面的空格
        str=str[1:-1]#在这里变为每行前面只有['', '30.0000', '-1']
        str=str.split(' ')
        epochtime=str[0]#获取这个历元时间
        statellite_number=str[1]#获取卫星数目
        if statellite_number!='-1':
            svlist=str[2:-1]#获取卫星编号列表
            #print(svlist)
        while len(svlist)!=0:
            statelist=svlist
            break
        #获取数值
        values=alllines[i+1][:-1]
        strv=values.replace("  ",' ')
        strv=strv.replace("  ",' ')
        strv=strv.replace("  ",' ')#一点一点的消除每一行前面的空格
        strv=strv[1:-1]#在这里变为每行前面只有['', '30.0000', '-1']
        valueslist=strv.split(' ')
        #print(epochtime)
        #print(valueslist)
        for sv in range(len(statelist)):
                epochlist.append([epochtime,statelist[sv],valueslist[sv]])
    #print(len(epochlist))
    #print(epochlist)
def make_plot():
    #绘制G05卫星的高度角数据
    G05=[]
    time5=[]
    G06=[]
    time6=[]
    G08=[]
    time08=[]
    for i in range(len(epochlist)):
        if epochlist[i][1]=="G05":
            G05.append(float(epochlist[i][2]))
            time5.append(round(float(epochlist[i][0])))
        if epochlist[i][1]=="G06":
            G06.append(float(epochlist[i][2]))
            time6.append(round(float(epochlist[i][0])))
        if epochlist[i][1]=="G08":
            G08.append(float(epochlist[i][2]))
            time08.append(round(float(epochlist[i][0])))
    plt.xlabel(u"time/(s)")
    plt.ylabel(u"电离层延迟变化率")
    plt.title(u"电离层延迟变化率图")
    plt.scatter(time5,G05,s=1,c='r',marker='.',label = '$G05$')
    plt.legend()
    plt.scatter(time6,G06,s=1,c='b',marker='.',label = '$G06$')
    plt.legend()
    plt.scatter(time08,G08,s=1,c='g',marker='.',label = '$G08$')
    plt.legend()
    plt.show()
def main():
    filename="abpo3300.d12"
    read_file(filename)
    make_plot()
if __name__ == '__main__':
    main()






