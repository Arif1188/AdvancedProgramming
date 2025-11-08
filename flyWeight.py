from typing import Any, Dict


class TreeType:
    def __init__(self, name: str, color: str, texture: dict):
        self.name = name
        self.color = color
        self.texture = texture

    def display(self):
        return f"Tree type: {self.name}, color: {self.color}, texture: {self.texture}"


class TreeTypeFactory:
    _tree_type: Dict[str, TreeType] = {}
    @staticmethod

    def create(name: str, color: str, texture: dict):
        key: str = f"{name}_{color}_{texture}"
        if key not in TreeTypeFactory._tree_type:
            TreeTypeFactory._tree_type[key] = TreeType(name, color, texture)
            return TreeTypeFactory._tree_type[key]
        return TreeTypeFactory._tree_type[key]


class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        return self.tree_type.display() + f"Drawing Tree on x: {self.x}, y: {self.y}"


if __name__ == "__main__":
    trees = []
    for i in range(100):
        tree_type = TreeTypeFactory.create("Juniper", "Green", {})
        trees.append(Tree(i, i * 2, tree_type))

    print(trees[0].draw())
    print(trees[99].draw())
    print(len(trees))
    print(len(TreeTypeFactory._tree_type))
