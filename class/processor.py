# -*- coding:utf-8 -*-
"""
流处理器
"""
class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self):
        assert False,'converter must be default'


class UpperCase(Processor):
    def converter(self,data):
        return data.upper()

if __name__ == "__main__":
    import sys
    obj = UpperCase(open('spam.txt'), sys.stdout)
    obj.process()