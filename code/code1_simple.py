"""
@Author : Wilson79
@Date   : 2020年2月9日 星期日 12:28:04
"""

# 导入wordcloud词云制作库
import wordcloud

# 创建词云对象w,设置词云图片宽、高、字体、背景颜色等参数
# Mac设置font_path='/System/Library/fonts/PingFang.ttc'
# Win设置font_path='msyh.ttc'
w = wordcloud.WordCloud(width=1500, height=1100, background_color='white',
                        font_path='/System/Library/fonts/PingFang.ttc')

# 调用词云对象的generate方法，将文本作为参数传入
w.generate(
    'Give up worrying about what others think of you。What they think isn’t important. What is important is how you feel about yourself.')

# 将生成的词云保存为picture1.png文件，且保存到当前文件夹中
w.to_file('picture1.png')
