"""
# BFS-1

# Problem 2
Course Schedule (https://leetcode.com/problems/course-schedule/)

Time Complexity : O(v+e) where v is vertices e is edges
Space Complexity : O(v+e) where v is vertices e is edges
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Your code here along with comments explaining your approach:
Below problem comes under Topological Sort where we have:
Adjacency Matrix/List - which stores the node that has dependencies in the map key is node , value is edges list
In degrees - vertex indexed array which will keep count of nodes that has no incoming edges

Queue is used to store the vertex whose indegree becomes 0 i.e., nodes that has no incoming edges.

Trick is to first store all the nodes whose indegree is 0 and also create the hashmap(adjacency list) of node - dependecies.
Now iterate over queue and pop the node and check if it is there is in adjacency list if no ignore it as it might have indegree
0 else get the edges present. Now iterate over each edge substract the indegree by 1 and check if the current node indegree is 0
if yes then increment the count and push the node to queue to fetch its edge as it's no longer dependent on any else continue.

Once the iteration is completed check if count is matching with no of vertices i.e., numCourses if yes return true else false.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True

        in_degrees = [0] * numCourses
        adjacency_list = {}
        count = 0
        queue = collections.deque()

        for pre_req in prerequisites: # O(e)
            if pre_req[1] not in adjacency_list:
                adjacency_list[pre_req[1]] = []
            adjacency_list[pre_req[1]].append(pre_req[0])
            in_degrees[pre_req[0]] += 1
        
        for i in range(numCourses): # O(v)
            if in_degrees[i] == 0:
                count += 1   
                queue.append(i)

        while len(queue) > 0:
            popped_val = queue.popleft()
            
            if popped_val not in adjacency_list:
                continue

            edges = adjacency_list[popped_val]
            if len(edges) == 0:
                continue

            for edge in edges:
                in_degrees[edge] -= 1

                if in_degrees[edge] == 0:
                    queue.append(edge)
                    count += 1

        return count == numCourses
            
            


        