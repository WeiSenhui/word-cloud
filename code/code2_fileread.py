"""
@Author : Wilson79
@Date   : 2020年2月9日 星期日 12:40:00
"""

import wordcloud

# 从外部同目录下.txt文件中读取文本，并存入变量txt中
filename = 'textfile.txt'
with open(filename) as f:
    txt = f.read()

w = wordcloud.WordCloud(width=1500,
                        height=1100,
                        background_color='white',
                        font_path="/System/Library/fonts/PingFang.ttc")

w.generate(txt)

w.to_file('picture2.png')
