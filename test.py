from KnowledgeGraph import *
import unittest
import os
import tempfile

class Test(unittest.TestCase):
	def setUp(self):
		self.data = [
			["Geoffrey Hinton", "works_at", "Google"],
			["Geoffrey Hinton", "researches", "Deep Learning"],
			["Geoffrey Hinton", "student_of", "Christopher Bishop"],
			["Yann LeCun", "works_at", "Meta"],
			["Yann LeCun", "researches", "Computer Vision"],
			["Yann LeCun", "researches", "Deep Learning"],
			["Yoshua Bengio", "works_at", "University of Montreal"],
			["Yoshua Bengio", "researches", "Deep Learning"],
			["Andrew Ng", "works_at", "Stanford University"],
			["Andrew Ng", "researches", "Machine Learning"],
			["Andrew Ng", "founded", "Coursera"],
			["Fei-Fei Li", "works_at", "Stanford University"],
			["Fei-Fei Li", "researches", "Computer Vision"],
			["Sam Altman", "works_at", "OpenAI"],
			["Ilya Sutskever", "works_at", "OpenAI"],
			["Ilya Sutskever", "researches", "Deep Learning"],
			["Google", "located_in", "USA"],
			["Meta", "located_in", "USA"],
			["Stanford University", "located_in", "USA"],
			["University of Montreal", "located_in", "Canada"]
		]
		self.kg = KnowledgeGraph()
		self.kg.add_triples(self.data)

	def test_add_dedup(self):
		self.assertTrue(self.kg.add_triple("A", "rel", "B"))
		self.assertFalse(self.kg.add_triple("A", "rel", "B"))  # 重复添加返回 False

	def test_delete(self):
		self.assertTrue(self.kg.delete_triple("Google", "located_in", "USA"))
		self.assertFalse(self.kg.delete_triple("Google", "located_in", "USA"))

	def test_find_entity(self):
		self.assertEqual(len(list(self.kg.find_entity("Geoffrey Hinton"))), 3)

	def test_find_relation(self):
		self.assertEqual(len(list(self.kg.find_relation("works_at"))), 7)

	def test_get_neighbors(self):
		neighbors = self.kg.get_neighbors("Google")
		self.assertIn(("out", "located_in", "USA"), neighbors)
		self.assertIn(("in", "works_at", "Geoffrey Hinton"), neighbors)

	def test_save_load_roundtrip(self):
		path = os.path.join(tempfile.gettempdir(), "kg_test.json")
		self.kg.save_to_file(path)
		kg2 = KnowledgeGraph()
		kg2.load_from_file(path)
		self.assertEqual(len(kg2), len(self.kg))  # 需要 __len__
		os.remove(path)


if __name__ == '__main__':
	unittest.main()