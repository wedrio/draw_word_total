import jieba
import matplotlib.pyplot as plt

txt = open('斗破苍穹.txt', 'r', encoding='utf-8').read()
for ch in '-#$%^&*()@:{}_+[]~.':
    txt = txt.replace(ch, " ")
    # 将文本中的特殊字符转换为空格替代

words = jieba.lcut(txt)  # 使用jieba库对中文进行中文分词，输出可能的分词的精确模式
counts = {}  # 创建一个空字典
for word in words:
    if len(word) == 1:  # 挑出单个的分词(不计数)
        continue
    else:
        counts[word] = counts.get(word, 0) + 1  # word不在words时，返回0，在时，返回+1，累加计数
item_s = list(counts.items())
item_s.sort(key=lambda x: x[1], reverse=True)  # 对items进行降序排列

for i in range(50):
    word, count = item_s[i]  # 返回相应的键值对
    print('{0:<10}{1:<5}'.format(word, count))  # word左对齐10个字符 count右对齐5个字符


def draw(dics, num=10):
    word1 = []
    total = []
    i = 0
    for dic in dics:
        i += 1
        if i < num + 1:
            word1.append(dic[0])
            total.append(dic[1])
        else:
            break
    # 设置matplotlib正常显示中文和负号
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(14, 16))
    plt.barh(word1, total, align='center', color=['r', 'g', 'b'], alpha=0.5)
    plt.title('斗破苍穹词频统计图')
    plt.ylabel('词汇')
    plt.xlabel('出现次数')

    plt.savefig('./word_total.svg')
    plt.show()


draw(item_s, 50)
