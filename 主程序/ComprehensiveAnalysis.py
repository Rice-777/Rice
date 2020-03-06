import numpy as np
import matplotlib.pyplot as plt
from ConnectSqlServer import ConnectSqlServer


class Analysis:
    def fun(self):
        plots_array_x = np.zeros((6, 8), int)
        plots_array_y = np.zeros((6, 8), int)
        connect = ConnectSqlServer(host='127.0.0.1', port=1433, user='sa', pwd='777', db='Rice')
        result_cash = connect.ExecQuery('select * from Cash')
        result_cunkuan = connect.ExecQuery('select * from Cunkuan')
        result_touzi = connect.ExecQuery('select * from Touzi')
        result_jiedai = connect.ExecQuery('select * from Jiedai')

        if not result_cash:
            pass
        else:
            for _ in range(len(result_cash)):
                plots_array_y[_][0] = (int(result_cash[_][3]))
                plots_array_y[_][1] = (int(result_cash[_][4]))
                plots_array_x[_][0] = (int(result_cash[_][2][-2:]))
                plots_array_x[_][1] = (int(result_cash[_][2][-2:]))

        if not result_cunkuan:
            pass
        else:
            for _ in range(len(result_cunkuan)):
                plots_array_y[_][2] = (int(result_cunkuan[_][4]))
                plots_array_y[_][3] = (int(result_cunkuan[_][6]))
                plots_array_x[_][2] = (int(result_cunkuan[_][3][-2:]))
                plots_array_x[_][3] = (int(result_cunkuan[_][3][-2:]))

        if not result_touzi:
            pass
        else:
            for _ in range(len(result_touzi)):
                plots_array_y[_][4] = (int(result_touzi[_][4]))
                plots_array_y[_][5] = (int(result_touzi[_][5]))
                plots_array_x[_][4] = (int(result_touzi[_][2][-2:]))
                plots_array_x[_][5] = (int(result_touzi[_][2][-2:]))

        if not result_jiedai:
            pass
        else:
            for _ in range(len(result_jiedai)):
                plots_array_y[_][6] = (int(result_jiedai[_][3]))
                plots_array_y[_][7] = (int(result_jiedai[_][4]))
                plots_array_x[_][6] = (int(result_jiedai[_][2][-2:]))
                plots_array_x[_][7] = (int(result_jiedai[_][2][-2:]))

        y = np.array([0, 0, 0, 0, 0, 0])
        labels = ["Cash_in", "Cash_out", "Cunkuan_in", "Cunkuan_out", "Touzi_in", "Touzi_out", "Jiedai_in", "Jiedai_out"]
        plt.figure(figsize=(17, 9),
                   dpi=97,  # 分辨率
                   facecolor='cyan',  # 图像的背景颜色 (默认白色)
                   edgecolor='blue',  # 图像的边框颜色 (默认黑色)
                   )  # 确定画布 当只有一个图时 可不写 , 参数 图像尺寸(长, 宽)

        for _ in range(plots_array_y.shape[1]):  # shape() 返回x的形状(10, 2) shape[1] --> 2 , 即 : 循环两次
            plt.scatter(plots_array_x[y == 0, _], plots_array_y[y == 0, _],  # 横坐标, 纵坐标,
                        s=37,  # 点的尺寸
                        c=np.array(plt.cm.tab10(_/7)).reshape(1, -1),  # 点的颜色 reshape(1, -1)装换维度
                        label=labels[_]  # 标签内容
                        )  # 画散点图

        #  标签中存在几种类别就循环几次 , 一次画一个颜色的点(其实画了两个图,但是是同时显示在一个画布上)

        plt.gca().set(xlim=(1, 31), ylim=(0, 7777))  # 设置坐标范围
        plt.xticks(fontsize=17)  # 设置x轴上标尺字体大小
        plt.yticks(fontsize=17)  # 设置y轴上标尺字体大小
        plt.xlabel('date', fontsize=17)  # 设置x轴上标签及字体大小
        plt.ylabel('money', fontsize=17)  # 设置y轴上标签及字体大小
        plt.title('Comprehensive analysis of personal property', fontsize=23)
        plt.legend(fontsize=17)  # 装饰图形(显示scatter中的label)参数: 标签的字体大小
        plt.show()  # 显示图例


if __name__ == '__main__':
    ca = Analysis()
    ca.fun()
