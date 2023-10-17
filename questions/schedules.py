"""
Problem: Ordering of Tasks with Prerequisites

Description:
Given a number of tasks and a list of prerequisite pairs, determine all possible orderings of tasks that satisfy the prerequisite conditions. Each task is labeled from 0 to N-1 and might have other tasks that should be completed before it can be scheduled.

Function Signature:
def possible_task_orders(tasks: int, prerequisites: List[List[int]]) -> List[List[int]]:

Inputs:
    - tasks (int): The total number of tasks.
    - prerequisites (List[List[int]]): A list of pairs, where the first task in the pair is a prerequisite for the second task.

Returns:
    - List[List[int]]: A list of all possible orderings of tasks that meet all prerequisites.

Examples:
1. Input: tasks=3, prerequisites=[[0, 1], [1, 2]]
   Output: [[0, 1, 2]]
   Explanation: There's only one possible ordering of tasks that meets the prerequisites.

2. Input: tasks=4, prerequisites=[[3, 2], [3, 0], [2, 0], [2, 1]]
   Output: 
   [
      [3, 2, 0, 1],
      [3, 2, 1, 0]
   ]
   Explanation: There are two possible orderings of tasks that meet the prerequisites.

3. Input: tasks=6, prerequisites=[[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
   Output: 
   [
      [0, 1, 4, 3, 2, 5],
      [0, 1, 3, 4, 2, 5],
      [0, 1, 3, 2, 4, 5],
      [0, 1, 3, 2, 5, 4],
      [1, 0, 3, 4, 2, 5],
      [1, 0, 3, 2, 4, 5],
      [1, 0, 3, 2, 5, 4],
      [1, 0, 4, 3, 2, 5],
      [1, 3, 0, 2, 4, 5],
      [1, 3, 0, 2, 5, 4],
      [1, 3, 0, 4, 2, 5],
      [1, 3, 2, 0, 5, 4],
      [1, 3, 2, 0, 4, 5]
   ]
   Explanation: There are several possible orderings of tasks that meet the prerequisites.

Notes:
    - This problem can be solved through topological sorting. Specifically, a modified version of the Kahn's algorithm for topological sorting can be used.
    - By iteratively removing nodes (tasks) with zero in-degree (i.e., tasks with no prerequisites) and considering them in all possible orderings, we can construct valid task sequences.
    - The problem can also be visualized as a directed graph where tasks are nodes and prerequisites are directed edges. 

Tags:
    - Graphs
    - Topological Sorting
"""

from typing import List

def possible_task_orders(tasks: int, prerequisites: List[List[int]]) -> List[List[int]]:
  return [['a', 'l', 'a', 'n'], ['w', 'a', 's'], ['h', 'e', 'r', 'e']]