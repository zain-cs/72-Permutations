def generate_permutations(nums):
    """
    Generate all permutations of nums using recursion/backtracking.
    """
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        # Base case: if current path has all elements
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                backtrack(path)      # recurse
                path.pop()           # backtrack
                used[i] = False      # mark as unused

    backtrack([])
    return result
nums = [1, 2, 3]
print(generate_permutations(nums))
