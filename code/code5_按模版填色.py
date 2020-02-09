"""
@Author : Wilson79
@Date   : 2020年2月9日 星期日 13:55:19
"""

# 导入绘图库matplotlib和词云制作库wordcloud
# 按模版填色适用于英文txt文本
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# 读入文本
filename = 'doinb2.txt'
with open(filename) as f:
    text = f.read()

# 导入imageio库中的imread函数，用这个函数读取本地图片，作为词云形状图片
import imageio

mk = imageio.imread("doinb.png")

# 创建词云对象w
wc = WordCloud(background_color="white",
               mask=mk, )

wc.generate(text)

########
# 调用wordcloud库中的ImageColorGenerator()函数，提取模板图片各部分的颜色
image_colors = ImageColorGenerator(mk)

# 显示原生词云图、按模板图片颜色的词云图和模板图片，按左、中、右显示
fig, axes = plt.subplots(1, 3)
# 左:显示原生词云图
axes[0].imshow(wc)
# 中:显示按模板图片颜色生成的词云图（采用双线性插值的方法显示颜色）
axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
# 右:显示模板图片
axes[2].imshow(mk, cmap=plt.cm.gray)
for ax in axes:
    ax.set_axis_off()
plt.show()

########

# 给词云对象wc按模板图片的颜色重新上色
wc = wc.recolor(color_func=image_colors)

# 将词云图片导出到当前文件夹
wc.to_file('picture5_doinb.png')
