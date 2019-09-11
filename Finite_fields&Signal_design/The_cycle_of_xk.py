from fundamental_tools.PolynomialsForFq import *
from fundamental_tools.same_data_structures_methods import DictList
from primitiverootForp import gcd
import networkx as nx
import matplotlib.pyplot as plt


def sign_element(double_tuple):
	the_value = double_tuple[0]
	new_tuple = (the_value, 1)
	return new_tuple


class Fxk:
	@staticmethod
	def generate_k_power(k):
		list_afterbody = [0] * k
		list_body = [1]
		list_body.extend(list_afterbody)
		return list_body
	
	def __init__(self, the_irreducible_polynomial, p, k):
		self._context = PolynomialsField(the_irreducible_polynomial, p)
		self._setting = int(k)
		self._relationship = DictList()
		self.get_the_relationship()
	
	def x_powers_k_cycle(self, the_element_list):
		irreducible_polynomial = self._context
		powers = self._setting
		the_element = Field_q(the_element_list, irreducible_polynomial)
		save_list = [the_element]
		cycle_element = the_element ** powers
		while cycle_element != the_element:
			save_list.append(cycle_element)
			cycle_element = cycle_element ** powers
		return save_list
	
	def change_k(self, change_number):
		self._setting = int(change_number)
		
	def all_x_powers_k_cycle(self):
		irreducible_polynomial = self._context
		powers = self._setting
		the_character = irreducible_polynomial.get_home()
		liner_span = irreducible_polynomial.get_deg()
		n = the_character ** liner_span - 1
		initial_list = [1]
		for degree in range(1, n):
			initial_list.append((Field_q(Fxk.generate_k_power(degree), irreducible_polynomial), 0))
		middle_list = []
		finalli_list = []
		for count in range(1, len(initial_list)):
			if initial_list[count][1] == 0:
				the_element = initial_list[count][0]
				initial_list[count] = sign_element(initial_list[count])
				middle_list.append(the_element)
				cycle_count = (count * powers) % n
				while cycle_count != count:
					middle_list.append(initial_list[cycle_count][0])
					initial_list[cycle_count] = sign_element(initial_list[cycle_count])
					cycle_count = (cycle_count * powers) % n
			if len(middle_list) > 0:
				finalli_list.append(middle_list.copy())
			middle_list.clear()
		return finalli_list
	
	def get_the_relationship(self):
		irreducible_polynomial = self._context
		the_character = irreducible_polynomial.get_home()
		liner_span = irreducible_polynomial.get_deg()
		n = the_character ** liner_span - 1
		self._relationship.insert(Field_q(1, irreducible_polynomial), '1')
		for degree in range(1, n):
			the_element = Field_q(Fxk.generate_k_power(degree), irreducible_polynomial)
			self._relationship.insert(the_element, 'θ^'+str(degree))
	
	def all_x_powers_k_multipy_a_cycle(self, a_list):
		irreducible_polynomial = self._context
		powers = self._setting
		idq = Field_q(1, irreducible_polynomial)
		the_character = irreducible_polynomial.get_home()
		liner_span = irreducible_polynomial.get_deg()
		n = the_character ** liner_span - 1
		initial_list = DictList()
		initial_list.insert(idq, 0)
		for degree in range(1, n):
			initial_list.insert(Field_q(Fxk.generate_k_power(degree), irreducible_polynomial), 0)
		the_multipy_element = Field_q(a_list, irreducible_polynomial)
		middle_list = []
		finalli_list = []
		for element, sign in initial_list.entries():
			if sign == 0:
				the_element = idq * element
				initial_list.change(the_element, 1)
				middle_list.append(the_element)
				the_element = the_multipy_element * (the_element ** powers)
				while the_element != element:
					middle_list.append(the_element)
					initial_list.change(the_element, 1)
					the_element = the_multipy_element * (the_element ** powers)
			if len(middle_list) > 0:
				finalli_list.append(middle_list.copy())
			middle_list.clear()
		return finalli_list, the_multipy_element
	
	def get_relationship(self):
		return self._relationship
	
	def get_context(self):
		return self._context
	
	def get_powers(self):
		return self._setting


class ConsequenceOfFxk:
	
	def __init__(self, the_irreducible_polynomial, p, k):
		self._context = Fxk(the_irreducible_polynomial, p, k)
		
	def get_context(self):
		return self._context
	
	def cycle_of_a_element(self, number_list):
		cycle_list = self._context.x_powers_k_cycle(number_list)
		the_relationsip = self._context.get_relationship()
		cycle_list_str = []
		for element in cycle_list:
			cycle_list_str.append(the_relationsip.search(element))
		return cycle_list_str
	
	def cycle_of_all_element(self):
		finally_list = self._context.all_x_powers_k_cycle()
		the_relationsip = self._context.get_relationship()
		finally_list_str = []
		cycle_list_str = []
		for cnt in range(0, len(finally_list)):
			cycle_list = finally_list[cnt].copy()
			for element in cycle_list:
				cycle_list_str.append(the_relationsip.search(element))
			finally_list_str.append(cycle_list_str.copy())
			cycle_list.clear()
			cycle_list_str.clear()
		return finally_list_str
	
	def cycle_of_all_element_and_multipy(self, a_list):
		finally_list, the_multipy_element = self._context.all_x_powers_k_multipy_a_cycle(a_list)
		the_relationsip = self._context.get_relationship()
		finally_list_str = []
		cycle_list_str = []
		for cnt in range(0, len(finally_list)):
			cycle_list = finally_list[cnt].copy()
			for element in cycle_list:
				cycle_list_str.append(the_relationsip.search(element))
			finally_list_str.append(cycle_list_str.copy())
			cycle_list.clear()
			cycle_list_str.clear()
		return finally_list_str, the_relationsip.search(the_multipy_element)
	
	def graph_cycle_of_a_element(self, number_list):
		the_relationsip = self._context.get_relationship()
		cycle_list = self.cycle_of_a_element(number_list)
		cycle_list_str = [the_relationsip.search(ele) for ele in cycle_list]
		G = nx.DiGraph()
		G.add_cycle(cycle_list_str)
		nx.draw_shell(G, arrows=True, with_labels=True, node_size=800, width=2, node_color='r')
		plt.show()
		
	def graph_cycle_of_all_element(self):
		finally_cycle_list = self.cycle_of_all_element()
		G = nx.DiGraph()
		for cnt in range(0, len(finally_cycle_list)):
			cycle_list = finally_cycle_list[cnt]
			G.add_cycle(cycle_list)
		plt.figure(figsize=(16, 10))
		nx.draw_shell(G, arrows=True, with_labels=True, node_size=500, width=2, node_color='r')
		plt.savefig('C:/Users/lenovo/Desktop/python学习内容/工作成果/xk图/p={0}_and_n={1}_and_k={2}.png'
		            .format(self._context.get_context().get_home(), self._context.get_context().get_deg(), self._context.get_powers()),
		            bbox_inches='tight', dpi=200)
		# plt.show()
	
	def graph_cycle_of_all_element_and_multipy(self, a_list):
		finally_cycle_list, the_multipy_str = self.cycle_of_all_element_and_multipy(a_list)
		G = nx.DiGraph()
		for cnt in range(0, len(finally_cycle_list)):
			cycle_list = finally_cycle_list[cnt]
			G.add_cycle(cycle_list)
		plt.figure(figsize=(16, 10))
		nx.draw_shell(G, arrows=True, with_labels=True, node_size=500, width=2, node_color='r')
		plt.savefig('C:/Users/lenovo/Desktop/python学习内容/工作成果/a_xk图/p={0}_n={1}_k={2}_a={3}.png'
		            .format(self._context.get_context().get_home(), self._context.get_context().get_deg(),
		                    self._context.get_powers(), the_multipy_str),
		            bbox_inches='tight', dpi=200)
		# plt.show()
		

# the_text = ConsequenceOfFxk([1, 1, 0, 0, 2], 3, 49)
# print(the_text.cycle_of_all_element_and_multipy([1]))
# the_text.graph_cycle_of_all_element()
# the_text.change_k(14)
# list1 = the_text.all_x_powers_k_multipy_a_cycle([1, 0])
# list1 = the_text.cycle_of_all_element_and_multipy([1, 0])
# for i in range(0, len(list1)):
# 	for j in range(0, len(list1[i]) - 1):
# 		print(list1[i][j], end='-->')
# 	print(list1[i][-1])


def all_cycle_of_k(a_irreducible_polynomial, p):
	"""
	走遍所有可能的k值
	"""
	n = len(a_irreducible_polynomial) - 1
	cycle_order = p ** n - 1
	for the_k in range(2, cycle_order):
		if gcd(the_k, cycle_order) == 1:
			the_item = ConsequenceOfFxk(a_irreducible_polynomial, p, the_k)
			the_item.graph_cycle_of_all_element()
	return


# all_cycle_of_k([1, 1, 2], 5)


def all_multipy(a_text):
	"""
	遍历a的所有可能
	"""
	if not isinstance(a_text, ConsequenceOfFxk):
		return
	f_ply = a_text.get_context()
	p = f_ply.get_context().get_home()
	n = f_ply.get_context().get_deg()
	the_order = p**n - 1
	for k in range(0, the_order):
		a_list = Fxk.generate_k_power(k)
		a_text.graph_cycle_of_all_element_and_multipy(a_list)
	return


# all_multipy(the_text)
# the_text.graph_cycle_of_all_element()
# for i in [31, 41]:
# 	the_text = ConsequenceOfFxk([1, 1, 3], 7, i)
# 	all_multipy(the_text)
# 简单置换多项式和置换表