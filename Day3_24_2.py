# 吃包子 c1, c2, c3
# 生产者
def consumer(name):
    print("消费者%s准备吃包子了" % name)
    while True:
        baozi = yield  # 接收外面的包子
        print("消费者%s收到包子编号：%s" % (name, baozi))


c1 = consumer("C1")
c2 = consumer("C2")
c3 = consumer("C3")
c1.__next__()
c2.__next__()
c3.__next__()

for i in range(1, 11):
    print("生成了第%s批包子".center(20, "-") % i)
    c1.send(i)
    c2.send(i)
    c3.send(i)
