class Person:
	count = 0
	staff = 0
	all_salary = 0
	staff_assistants = []
	
	def __init__(self, name, status, salary, pay_basis, position_title):
		self.name = name
		self.status = status
		self.salary = salary
		self.pay_basis = pay_basis
		self.position_title = position_title
		self.__class__.count += 1
		if self.status != 'Detailee':
			self.__class__.staff += 1
		self.__class__.all_salary += self.salary
		if position_title == 'STAFF ASSISTANT':
			self.__class__.staff_assistants.append(self)
	
	def __repr__(self):
		return self.name
	
	def __del__(self):
		self.__class__.count -= 1
		if self.status != 'Detailee':
			self.__class__.staff -= 1
		self.__class__.all_salary -= self.salary
	
	@classmethod
	def report(cls):
		print(f'Всего {cls.count} сотрудников, общая зарплата {cls.all_salary}, средняя зарплата {cls.all_salary/cls.count}, средняя зарплата штатных сотрудников {cls.all_salary/cls.staff}')
	
	@classmethod
	def assistants_report(cls):
		for a in cls.staff_assistants:
			print(f'assistant: {a.name} / salary: ${a.salary}')

class WH:
	def __init__(self, name_file):
		self.sotr = []
		self.get_sotr(name_file)
	def get_sotr(self, name_file):
		f = open(name_file, 'r')
		t = f.readlines()
		f.close()
		for s in t[1:]:
			sp = s.strip().split(';')
			k = sp[2]
			salary = float(k.strip().replace('$','').replace(',',''))
			p = Person(sp[0], sp[1], salary, sp[3], sp[4])
			self.sotr.append(p)
			
	def summa(self):
		su = 0
		for s in self.sotr:
			su += s.salary
		return su/len(self.sotr)
	def top10(self):
		def sal(i):
			return i.salary
		top = self.sotr.copy()
		top2 = sorted(top, key=sal, reverse = True)
		return top2[:10]
	def detailees(self):
		return [i for i in self.sotr if i.status == 'Detailee' ]
	def staff(self):
		return len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT' ])
	def rep(self):
		for i in self.sotr:
			print(i)
	
	def recount(self):
		''' Изменение зарплаты сотрудника и пересчет all_salary'''
		total = 0
		for i in self.sotr:
			total += i.salary
		Person.all_salary = total
	
	def count_sotr(self):
		print(f'Всего {Person.count} сотрудников, из них {Person.staff} на постоянной основе общий заработок {Person.all_salary}')
	
	@staticmethod
	def sum_salary(some):
		total = 0
		for p in some:
			total += p.salary
		return total
	
	@staticmethod
	def avg_salary(some):
		total = 0
		for p in some:
			total += p.salary
		return total/len(some)
			
	
if __name__ == '__main__':
	wh = WH('white_house_2017_salaries_com.csv')
	wh.rep()

	wh.count_sotr()
	wh.sotr[140].salary = 10000000
	wh.recount()
	wh.count_sotr()
	print(Person.staff_assistants)
	del Person.staff_assistants[0]
	print(Person.staff_assistants)
	Person.report()
	del wh.sotr[133]
	Person.report()
	Person.assistants_report()
	print(wh.sum_salary(Person.staff_assistants))
	print(wh.avg_salary(Person.staff_assistants))
