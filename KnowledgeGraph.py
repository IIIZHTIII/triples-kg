import json
from models import Entity, Relation, Triple
from collections.abc import Iterable, Iterator, Sequence
import logging

logger = logging.getLogger(__name__)

class KnowledgeGraph:

	def __init__(self)-> None:
		self.triples: list[Triple] = []

	def __len__(self) -> int:
		return len(self.triples)

	def __iter__(self) -> Iterator[Triple]:
		return iter(self.triples)

	def __str__(self) -> str:
		return json.dumps(
			[[t.subject.name, t.predicate.name, t.object.name] for t in self.triples],
			ensure_ascii=False)

	def _to_entity(self, value: str | Entity) -> Entity:
		return value if isinstance(value, Entity) else Entity(value)

	def _to_relation(self, value: str | Relation) -> Relation:
		return value if isinstance(value, Relation) else Relation(value)

	def add_triple(self, subject: str | Entity, predicate: str | Relation, obj: str | Entity) -> bool:
		# 添加三元组：字符串自动包装成 Entity/Relation 对象
		triple = Triple(self._to_entity(subject), self._to_relation(predicate), self._to_entity(obj))
		if triple not in self.triples:
			self.triples.append(triple)
			logger.debug(f"added triple: {triple}")
			return True
		logger.debug(f"triple is already exists: {triple}")
		return False

	def add_triples(self, triples: Iterable[Sequence[str]]) -> bool:
		for subject, predicate, obj in triples:
			self.add_triple(subject, predicate, obj)
		return True

	def delete_triple(self, subject: str | Entity, predicate: str | Relation, obj: str | Entity) -> bool:
		triple = Triple(self._to_entity(subject), self._to_relation(predicate), self._to_entity(obj))
		if triple in self.triples:
			self.triples.remove(triple)
			return True
		return False

	# def find_entity(self, entity) -> list[Triple]:
	# 	entity = self._to_entity(entity)
	# 	return [t for t in self.triples if t.subject == entity or t.object == entity]

	def find_entity(self, entity: str | Entity) -> Iterator[Triple]:
		entity = self._to_entity(entity)
		for triple in self.triples:
			if entity == triple.subject or entity == triple.object:
				yield triple

	# def find_relation(self, predicate) -> list[Triple]:
	# 	predicate = self._to_relation(predicate)
	# 	return [t for t in self.triples if t.predicate == predicate]

	def find_relation(self, predicate: str | Relation) -> Iterator[Triple]:
		predicate = self._to_relation(predicate)
		for triple in self.triples:
			if predicate == triple.predicate:
				yield triple

	def get_neighbors(self, entity: str | Entity) -> list[tuple]:
		entity = self._to_entity(entity)
		results = []
		for triple in self.triples:
			if triple.subject == entity:
				results.append(('out', triple.predicate.name, triple.object.name))
			elif triple.object == entity:
				results.append(('in', triple.predicate.name, triple.subject.name))
		return results

	def load_from_file(self, filename: str) -> None:
		try:
			with open(filename, 'r', encoding='utf-8') as file:
				data = json.load(file)
		except FileNotFoundError:
			logger.warning(f'File {filename} not found.')
			self.triples = []
			return
		self.triples = [Triple(Entity(s), Relation(p), Entity(o)) for s, p, o in data]
		logger.info(f'Loaded {len(self.triples)} triples from {filename}.')

	def save_to_file(self, filename: str) -> None:
		with open(filename, 'w', encoding='utf-8') as file:
			json.dump(
				[[t.subject.name, t.predicate.name, t.object.name] for t in self.triples],
				file, ensure_ascii=False, indent=2)

	def iter_triples(self) -> Iterator[Triple]:
		for triple in self.triples:
			yield triple

