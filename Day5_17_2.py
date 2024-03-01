class Document(object):  # 抽象类
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")  # 子类必须重写show方法，不然报错


class Pdf(Document):
    def show(self):
        return "Show PDF contents"


class Word(Document):
    def show(self):
        return "Show Word contents"


pdf_obj = Pdf("NM.pdf")
word_obj = Word("NU.doc")

objs = [pdf_obj, word_obj]
for o in objs:
    print(o.show())