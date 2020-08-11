# ------------单链表--------------
class Note:
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
        self.header = q = Note()
        self.length = 0
        if not iter:
            return
        for value in iter:
            q.next = Note(value)
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
        note = Note(value)
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
# ------------栈--------------
class Stack:
    def __init__(self,iter=None):
        '''
        初始化栈
        :param iter:可迭代对象 初始化数据
        '''
        self.header = Note()
        self.length = 0
        if not iter:
            return
        for i in iter:
            note = Note(i)
            note.next,self.header.next = self.header.next,note
            self.length += 1

    def is_empty(self):
        '''
        判断栈是否为空
        :return: 布尔值
        '''
        return self.header.next == None

    def peek(self):
        '''
        返回栈顶元素
        :return: 栈顶元素
        '''
        if self.is_empty():
            raise IndexError('栈为空')
        return self.header.next.value

    def size(self):
        '''
        返回栈的大小
        :return: 栈的大小
        '''
        return self.length

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, val):
        '''
        入栈
        :param val: 元素
        :return: None
        '''
        if not val:
            raise ValueError('val的值为空')
        note = Note(val)
        self.header.next, note.next = note, self.header.next
        self.length += 1

    def pop(self):
        '''
        出栈
        :return: 栈顶元素
        '''
        if self.is_empty():
            raise IndexError('栈为空')
        res = self.header.next.value
        self.header.next = self.header.next.next
        self.length -= 1
        return res

def conversion(n:int, x:int)->str:
    '''
    十进制转其他进制
    :param n: 需要转换进制的十进制数
    :param x: 进制
    :return: 转换后的数
    '''
    s = Stack()
    res = ''
    while n>0:
        s.push(n%x)
        n //= x
    while not s.is_empty():
        res += str(s.pop())
    return res

def pareMacthing(string:str)->bool:
    '''
    验证字符串中的括号是否匹配
    :param s: 字符串
    :return: bool
    '''
    if not string:
        return True
    s = Stack()
    for i in string:
        if i in ['(','[','{']:
            s.push(i)
        if i == ')':
            if s.peek() == '(':
                s.pop()
            else:
                return False
        elif i == ']':
            if s.peek() == '[':
                s.pop()
            else:
                return False
        elif i == '}':
            if s.peek() == '{':
                s.pop()
            else:
                return False
    return True if s.is_empty() else False
# --------------队列-----------------
class Queue:
    def __init__(self,iter=None):
        '''
        初始化队列
        :param iter: 可迭代对象
        '''
        self.rear=self.header = Note()
        self.length = 0
        if not iter:
            return
        for i in iter:
            note = Note(i)
            self.rear.next = note
            self.rear = self.rear.next
            self.length += 1

    def put(self,value):
        '''
        入队
        :param value: 入队的数据
        :return: None
        '''
        self.rear.next = Note(value)
        self.rear = self.rear.next
        self.length += 1

    def pop(self):
        '''
        出队
        :return: 出队的数据
        '''
        if not self.length:
            raise ValueError('队列为空')
        res = self.header.next
        self.header.next = self.header.next.next
        return res

if __name__ == '__main__':
    from queue import deque
    dq = deque(['a','b'])
    print(dq)




