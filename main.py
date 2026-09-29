from KnowledgeGraph import *
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
# main.py 里，basicConfig 之后追加
file_handler = logging.FileHandler('triples.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
logging.getLogger('KnowledgeGraph').addHandler(file_handler)

if __name__ == "__main__":
    kg = KnowledgeGraph()
    # kg.save_to_file()

    kg.load_from_file("triple.json")
    print(kg)

    # 1. 查实体
    print("查Hinton相关：")
    print(list(kg.find_entity("Geoffrey Hinton")))

    # 2. 查关系
    print("\n查works_at关系：")
    print(list(kg.find_relation("works_at")))

    # 3. 查邻居
    print("\nGoogle的邻居：")
    print(kg.get_neighbors("Google"))

    # 删除
    kg.delete_triple("Google", "located_in", "USA")
    print("\n删除后Google的邻居：")
    print(kg.get_neighbors("Google"))
