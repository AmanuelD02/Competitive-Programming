class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        output = []
        visited = set()
        graph = defaultdict(list)
        for i, food in enumerate(recipes):
            graph[food] = ingredients[i]
        
        def dfs(food):
            count = 0
            visited.add(food)
            
            for ingred in graph[food]:
                if ingred in supplies:
                    count += 1
                else:
                    if ingred not in visited:
                        dfs(ingred)
                        if ingred in supplies:
                            count += 1
            
            if count and count == len(graph[food]):
                output.append(food)
                supplies.add(food)
        
        for f in recipes:
            if f not in visited:
                dfs(f)
        
        return output