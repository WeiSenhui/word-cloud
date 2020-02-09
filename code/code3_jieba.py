"""
@Author : Wilson79
@Date   : 2020年2月9日 星期日 12:41:38
"""

# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud

w = wordcloud.WordCloud(width=1500,
                        height=1100,
                        background_color='white',
                        font_path="/System/Library/fonts/PingFang.ttc")

# 调用jieba的lcut()方法对原始文本进行中文分词，得到string
txt = '让适合的人走进你的生活吧，让旧梦逝去吧，让不合适的那个离开吧'
txtlist = jieba.lcut(txt)
# txtlist:['让', '适合', '的', '人', '走进', '你', '的', '生活', '吧', '，', '让', '旧梦', '逝去', '吧', '，', '让', '不', '合适', '的', '那个', '离开', '吧']

str = " ".join(txtlist)
# str:让 适合 的 人 走进 你 的 生活 吧 ， 让 旧梦 逝去 吧 ， 让 不 合适 的 那个 离开 吧

w.generate(str)

w.to_file('picture3.png')
