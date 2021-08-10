from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import pylab as pl

"""
画图工具

提供与图形用户化界面相关的方法
"""


def drawing():
    """
    画图
    """
    plt.figure(num=1, figsize=(8, 8), dpi=80, clear=False)  # 创建一个新的图形，或者激活一个现有图形  [num: 图形标识, figsize: 图形大小, dpi:数字分辨率, clear: 为 True 时图形存在则清空]
    plt.suptitle("title")  # 设置图形标题
    subgraph = plt.subplot(1, 1, 1)  # 创建子图  [行数， 列数， 图片位置(从左至右，从上至下)]

    subgraph.plot(["x"], ["y"], linewidth=1, color="red", label="label")  # 画折线图 [x轴， y轴， linewidth:线宽， color:颜色, label:标签]
    # plt.boxplot(data, notch, position)  #绘制一个箱形图
    # plt.bar(left, height, bottom)  #绘制一个条形图
    # plt.barh(width, bottom, left, height)  #绘制一个横向条形图
    # plt.polar(theta, r)  #绘制极坐标图
    # plt.pie(data, explode)  #绘制饼图
    # plt.psd(x, NFFT=256, pad_to, Fs)  #绘制功率谱密度图
    # plt.specgram(x, NFFT=256, pad_to, F)  #绘制谱图
    # plt.cohere(x, y, NFFT=256, Fs)  #绘制X - Y的相关性函数
    # plt.scatter(x, y)  #绘制散点图，其中，x和y长度相同
    # plt.step(x, y, where)  #绘制步阶图
    # plt.hist(x, bins, normed)  #绘制直方图
    # plt.contour(X, Y, Z, N)  #绘制等值图
    # plt.vlines()  #绘制垂直图
    # plt.stem(x, y, linefmt, markerfmt)  #绘制柴火图
    # plt.plot_date()  #绘制数据日期

    subgraph.set_title("title")  # 设置子图标题

    pl.xticks(rotation=80)  # 设置x轴文本标签和属性  [rotation: 逆时针旋转]
    pl.yticks(rotation=0)

    plt.legend(loc='upper right')  # 加上一个图例, 展示每根线的标签

    present_coordinate_axis = plt.gca()  # 获取当前坐标轴
    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(1)
    present_coordinate_axis.yaxis.set_major_locator(y_major_locator)  # 设置 x 轴间隔刻度
    present_coordinate_axis.xaxis.set_major_locator(x_major_locator)

    plt.subplots_adjust(top=0.96, bottom=0.1, left=0.05, right=1, hspace=0, wspace=0)  # 调整画布参数
    plt.savefig("./img.jpg", dpi=150)  # 保存图片
    plt.show()  # 显示图形窗口
    plt.close()  # 关闭图形窗口


if __name__ == '__main__':
    drawing()
