class Assoc:
	def __init__(self, key, value):
		self.key = key
		self.value = value
	
	# def __lt__(self, other):  # 有时可能会需要关键码的排序
	# 	return self.key < other.key
	
	# def __le__(self, other):
	# 	return self.key < other.key or self.key == other.key
	
	def __str__(self):
		return 'Assoc({0},{1})'.format(self.key, self.value)


class DictList:
	def __init__(self):
		self._elems = []
	
	def is_empty(self):
		return not self._elems
	
	def num(self):
		return len(self._elems)
	
	def search(self, key1):
		n = self.num()
		for i in range(n):
			if self._elems[i].key == key1:
				return self._elems[i].value
		return False
	
	def insert(self, key1, value1):
		# n = self.num()
		# for i in range(n):
		# 	if self._elems[i].key == key1:
		# 		self._elems[i].value = value1
		# 		return
		self._elems.append(Assoc(key1, value1))
	
	def delete(self, key1):
		n = self.num()
		for i in range(n):
			if self._elems[i].key == key1:
				self._elems.pop(i)
				return
	
	def value(self):
		n = self.num()
		for i in range(n):
			yield self._elems[i].value
	
	def entries(self):
		n = self.num()
		for i in range(n):
			yield self._elems[i].key, self._elems[i].value
	
	def change(self, key1, vaule1):
		n = self.num()
		for i in range(n):
			if self._elems[i].key == key1:
				self._elems[i].value = vaule1


class StackUnderflow(ValueError):
	pass


class SStack:
	"""
	用顺序表实现栈，在python中因为有list的定义，所以可以直接使用list来实现栈
	由于python中list采用动态顺序表技术，所以栈采用的也是动态顺序表技术
	栈是list的一个真子集，对于list来说正常的操作对于栈都是非法的，所以不能用list直接表示栈
	但是可以将栈看做一个类，这个类具有一个list属性，这样可以对这个属性进行限制和定义比较严格的栈的操作
	这种看法即用list函数来实现栈
	"""
	
	def __init__(self):
		self._elems = []
	
	def is_empty(self):  # 判空
		return self._elems == []
	
	def top(self):  # 访问最上面的数据，也就是最后进入的数据
		if len(self._elems) == 0:
			raise StackUnderflow('in SStack top{}')
		return self._elems[-1]
	
	def push(self, elem):  # 存入数据，存入在结构的最上面
		self._elems.append(elem)
	
	def pop(self):  # 弹出数据，根据后进先出，弹出最后进入的数据
		if len(self._elems) == 0:
			raise StackUnderflow('in SStack pop{}')
		return self._elems.pop()


class LNode:  # 使用链表就要定义结点
	def __init__(self, elem, next_=None):
		self._elem = elem
		self._next = next_


class LStack:
	"""
	使用链表来实现栈类，因为单链表对表头的操作最简单，所以把表头看做是栈的最上面
	每次存入数据，删除数据或者访问数据就可以直接对表头进行操作
	这种方法是用链表实现栈
	"""
	
	def __init__(self):
		self._top = None
	
	def is_empty(self):  # 判空
		return self._top is None
	
	def top(self):  # 访问最上面数据
		if self._top is None:
			raise StackUnderflow('in LStack top{}')
		return self._top.elem
	
	def push(self, elem):  # 存入数据
		self._top = LNode(elem, self._top)
	
	def pop(self):  # 删除数据
		if self._top is None:
			raise StackUnderflow('in LStack pop{}')
		p = self._top
		self._top = p.next
		return p.elem


class QueueUnderflow(ValueError):
	pass


class SQueue:
	"""
	通过列表表示队列
	"""
	
	def __init__(self, init_len=8):
		self._len = init_len
		self._elems = [0] * init_len
		self._head = 0  # 队首的索引，相关的加减法都要取模
		self._num = 0
	
	def is_empty(self):
		return self._num == 0
	
	def peek(self):
		if self._num == 0:
			raise QueueUnderflow
		return self._elems[self._head]
	
	def dequeue(self):
		if self._num == 0:
			raise QueueUnderflow
		e = self._elems[self._head]  # 不需要更改self._elems[self._head]的值是因为这个位置储存区直接可以被无视
		self._elems[self._head] = 0
		self._head = (self._head + 1) % self._len
		self._num -= 1
		return e
	
	def enqueue(self, e):
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head + self._num) % self._len] = e  # 因为采用的是循环列表的形式
		self._num += 1
	
	def __extend(self):  # 进行存储空间的扩张
		old_len = self._len
		self._len *= 2  # 直接将长度扩大二倍
		new_elems = [0] * self._len  # 新建一个列表，然后通过列表复制的方式进行扩建
		for i in range(old_len):  # 扩建之后self._head从零开始记值
			new_elems[i] = self._elems[(self._head + i) % old_len]
		self._elems = new_elems
		self._head = 0
	
	def dequeue_2(self):
		if self._num == 0:
			raise QueueUnderflow
		e = self._elems[(self._head + self._num - 1) % self._len]
		self._elems[(self._head + self._num - 1) % self._len] = 0
		self._num -= 1
		return e
	
	def enqueue_2(self, e):
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head - 1) % self._len] = e
		self._head = (self._head - 1) % self._len
		self._num += 1


'''
优先队列，与栈和队列作用一样，是一个缓存结构，但是其中的每一个数据有具有一个优先级的值
基于对二叉树的应用，可以高效地实现这种数据结构
一般来讲，为了实现高效，在对于相同优先级的数据处理时，应当采取随机处理某一个数据
可以基于5.1中二叉树基于线性表的实现来实现优先队列，也可以用链表，更方便
'''


class PrioQueueError(ValueError):
	pass


class PrioQue:
	def __init__(self, elist=None):
		if elist is None:
			elist = []
		self._elems = list(elist)
		self._elems.sort(reverse=True)  # 用列表的排序方法进行排序，基于小数优先级高，也可反过来
	
	def enqueue(self, e):  # 基于优先级相同的数据先进先出，可以更改小于等于使其变为后进先出
		i = len(self._elems) - 1
		while i >= 0:
			if self._elems[i] <= e:  # 因为是反序，所以要找到最小的比e大的数
				i -= 1
			else:
				break
		self._elems.insert(i + 1, e)  # insert不会引发错误，如果i+1大于元列表的最大索引则等于进行append
	
	def is_empty(self):
		return not self._elems
	
	def peek(self):  # 访问优先级最高的一组数据中最先进入的那个数据
		if self.is_empty():
			raise PrioQueueError
		return self._elems[-1]
	
	def dequeue(self):
		if self.is_empty():
			raise PrioQueueError
		return self._elems.pop()


'''
堆：采用树形结构实现优先队列的一种有效技术，堆就是每个结点都存储数据的完全二叉树
堆序：每个结点的数据优先级小于等于其父结点，大于等于其子结点（每个结点只与其父结点和子结点比较）
由于完全二叉树与连续表同构，所以一般也可以用连续表实现堆
在堆上删除根元素或最后一个元素生成的结构仍是堆（一个或两个），加入新元素未必是堆（不一定满足堆序）
用堆可以优化在5.1中优先队列的插入或者删除操作，能够把O(n)时间的算法优化为O(logn)时间的算法
基于list可以实现堆
'''


class PrioQueue:
	def __init__(self, elist=None):
		if elist is None:
			elist = []
		self._elems = list(elist)
		if elist:
			self.buildheap()  # 建立一个堆
	
	def is_empty(self):
		return not self._elems
	
	def peek(self):
		if self.is_empty():
			raise PrioQueueError
		return self._elems[0]
	
	def enqueue(self, e):
		self._elems.append(None)  # 加入一个空结点
		self.siftup(e, len(self._elems) - 1)
	
	def siftup(self, e, last):
		"""
		向上筛选法：在堆的最后添加一个包含e的结点，然后这个结点与其父结点比较，如果e的优先级更大，则交换位置
		重复上面比较交换操作直到e不动，由堆的性质可以得到所有操作完成之后得到的仍然是一个堆
		其中，因为初始的根结点在列表中的位置是0，所以求每个结点的父结点要取下整
		"""
		i, j = last, (last - 1) // 2  # 取下整，得到其父结点的索引
		while i > 0 and e < self._elems[j]:  # 不需要交换，将所有下面的值调整好之后，上面直接赋e，可以省略交换的过程
			self._elems[i] = self._elems[j]
			i, j = j, (j - 1) // 2
		self._elems[i] = e
	
	def dequeue(self):  # 弹出根结点
		if self.is_empty():
			raise PrioQueueError
		elems = self._elems
		e0 = elems[0]
		e = elems.pop()
		if len(elems) > 0:
			self.siftdown(e, 0, len(elems))
		return e0
	
	def siftdown(self, e, begin, end):
		"""
		向下筛选法：指针指向某一个父结点，e与其两个子结点进行比较，让优先级最高的值的结点作为这一个父结点
		如果是e，则结束，否则指针指向优先级最高的那个子结点，使其作为下一轮的父结点
		这样e的比较路径总是沿着优先级最高的向下筛选
		同shiftup的思路类似，在比较过程中不需要实际的交换，而是给每个元素找合适的位置，找到了之后直接赋值
		"""
		elems, i, j = self._elems, begin, begin * 2 + 1  # 乘2加1可以保证j总是i的子结点中的左子结点
		while j < end:
			if j + 1 < end and elems[j + 1] < elems[j]:
				j += 1  # elems[j+1]更小的情况，则与e比较的使命交给elems[j+1]
			if e < elems[j]:  # 此时e是三者中最小的，这个时候已经给e找好了位置，就是i
				break
			elems[i] = elems[j]  # 否则，如果e不是最小的，那么就让e往下继续比较
			i, j = j, j * 2 + 1
		elems[i] = e  # 最后赋值
	
	def buildheap(self):
		end = len(self._elems)
		for i in range(end // 2, -1, -1):  # 到零为止
			self.siftdown(self._elems[i], i, end)
	
	def another_way(self):
		"""
		不节省空间实现优先队列排序的方法
		"""
		a = []
		while self._elems:
			a.append(self.dequeue())
		return a


class BinTNode:
	"""
	使用递归调用结点的方式定义二叉树，先定义结点类
	"""
	def __init__(self, dat, left=None, right=None):
		self.data = dat
		self.left = left
		self.right = right
		
		
class BinTree:
	"""
	真正的二叉树类
	"""
	
	def __init__(self):
		self._root = None
	
	def is_empty(self):
		return self._root is None
	
	def root(self):
		return self._root
	
	def leftchild(self):
		return self._root.left
	
	def rightchild(self):
		return self._root.right
	
	def set_root(self, rootnode):
		if not isinstance(rootnode, BinTNode):
			raise ValueError('this root is not a BinTNode')
		self._root = rootnode
	
	def set_left(self, leftchild):
		if not isinstance(leftchild, BinTNode):
			raise ValueError('this root is not a BinTNode')
		self._root.left = leftchild
	
	def set_right(self, rightchild):
		if not isinstance(rightchild, BinTNode):
			raise ValueError('this root is not a BinTNode')
		self._root.right = rightchild
	
	def preorder_elements(self):  # 前根序生成器
		t, s = self._root, SStack()
		while t is not None or not s.is_empty():
			while t is not None:
				s.push(t.right)  # 右子结点入栈
				yield t.data
				t = t.left
			t = s.pop()
