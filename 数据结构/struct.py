class LNote:
    '''线性节点类'''
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LinearLinked:
    '''线性链表'''
    def __init__(self,iter=None):
        '''
        将可迭代对象转成线性链表
        :param ite:可迭代对象
        '''
        self.header = q = LNote()
        self.length = 0
        for value in iter:
            q.next = LNote(value)
            self.length += 1
            q = q.next

    def insert(self,value,index=0):
        '''
        将数据插入指定位置
        :param value: 数据
        :param index: 位置
        '''
        if index>=self.length:
            raise IndexError('linear index out of range')
        note = LNote(value)
        q = self.header
        for i in range(index):
            q = q.next
        note.next,q.next = q.next,note
        self.length += 1

    def delete(self,index=0):
        '''
        删除指定节点,默认删除
        :param index: 位置
        :return: 被删除节点的值
        '''
        if not self.header.next:
            raise ValueError('linear is empty')
        if index>=self.length:
            raise IndexError('linear index out of range')
        q = self.header
        for i in range(index):
            q = q.next
        q.next = q.next.next
        self.length -= 1

    def clear(self):
        '''
        重置为空表
        :return:
        '''
        self.header.next = None
        self.length = 0

    def getValue(self,index):
        '''
        获取指定节点的值
        :param index: int 索引
        :return: 值
        '''
        if index>=self.length:
            raise IndexError('linear index out of range')
        q = self.header
        for i in range(index):
            q = q.next
        return q.value

    def setValue(self,index,value):
        '''
        修改指定节点的值
        :param index: int 索引
        :param value: 新值
        '''
        if index>=self.length:
            raise IndexError('linear index out of range')
        q = self.header
        for i in range(index):
            q = q.next
        q.value = value

    def __iter__(self):
        return LinearLinkedIterator(self.header)

class LinearLinkedIterator:
    '''线性链表迭代器'''
    def __init__(self,note):
        self.note = note
    def __next__(self):
        if not self.note.next:
            raise StopIteration
        self.note = self.note.next
        return self.note.value

if __name__ == '__main__':
    pass



