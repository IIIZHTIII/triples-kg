from dataclasses import dataclass

@dataclass(frozen=True)
class Entity:

	name: str

	def __str__(self):
		return self.name


@dataclass(frozen=True)
class Relation:
	name: str

	def __str__(self):
		return self.name

@dataclass(frozen=True)
class Triple:
	subject: Entity
	predicate: Relation
	object: Entity

	def __str__(self):
		return f'({self.subject.name}, {self.predicate.name}, {self.object.name})'

	def __repr__(self) -> str:
		return f'\nTriple(\n\tsubject={self.subject!r}, \n\tpredicate={self.predicate!r}, \n\tobject={self.object!r}\n)'




