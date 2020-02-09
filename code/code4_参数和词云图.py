"""
@Author : Wilson79
@Date   : 2020年2月9日 星期日 13:32:18
"""

# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud

# 导入imageio库中的imread函数，用这个函数读取本地图片，作为词云形状图片（图片一定要求是白底的）
import imageio

mk = imageio.imread("doinb.png")

# 创建并配置词云对象w,scale参数值越大，图片越清晰
w = wordcloud.WordCloud(width=1500,
                        height=1100,
                        background_color='white',
                        font_path="/System/Library/fonts/PingFang.ttc",
                        mask=mk,
                        scale=10,  # 清晰度
                        # contour_width=0.5,  # 轮廓宽度
                        # contour_color='blue'  # 轮廓颜色
                        )

filename = 'doinb.txt'
with open(filename) as f:
    txt = f.read()

txtlist = jieba.lcut(txt)
str = " ".join(txtlist)

w.generate(str)

# 按模版的颜色填色
image_colors = wordcloud.ImageColorGenerator(mk)
w = w.recolor(color_func=image_colors)

w.to_file('out_doinb.png')

