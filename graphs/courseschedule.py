"""
Problem:
College courses have pre-requisites. Given the total num of courses and a list of pre-requisites 
return all courses can be completed or not. A course can only be taken if all of its pre-requiste courses 
are completed. 

Pre-requisite data is in form [[1, 0], [2, 0]]. Data tells us courses 1 and 2 require course 0 to be completed. 

Algorithm: 
We know courses with no pre-requisites can be taken first. We also initialize a CNode object per course that lists 
all dependencies on that course. As we process courses with no pre-requisites we decrement by 1 number of dependencies on 
each course that lists this course as a pre-requisite. During this process if number of dependencies on a course becomes 0 
we can add this course to the queue to process. 
"""
print(__doc__)

class CNode(object):
    def __init__(self, val):
        self.val = val
        self.dependents = [] 
        self.no_of_dependencies = 0
        self.is_traversed = False
        
class SolutionCourseSchedule(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        
        numCourses tells us total number of courses 
        including those with no dependencies 
        """
        all_nodes = {}
        no_d_nodes = {}
        
        # Create CNode for each course and add it to 
        # all_nodes and no_d_nodes
        for i in range(numCourses):
            n = CNode(i)
            all_nodes[i] = n 
            no_d_nodes[i] = n
            
        
        # Iterate through prerequisites list         
        for p in prerequisites:
            # get pre-requisite node 
            c_node = all_nodes[p[0]]
            # Increment dependencies for node 
            c_node.no_of_dependencies += 1
                
            # remove this node from list of 
            # nodes with not dependencies 
            if p[0] in no_d_nodes:
                del no_d_nodes[p[0]]
            
            # add as dependent course to pre-requisite    
            all_nodes[p[1]].dependents.append(c_node)
        
        # if no nodes end up in non-dependent nodes 
        # return false 
        if not no_d_nodes:
            return False 
        
        # Add all non dependent nodes to queue 
        queue = [n for n in no_d_nodes.values()]
        
        while len(queue) > 0:
            # Process non-dependent nodes            
            node = queue.pop(0)
            # mark as traversed 
            node.is_traversed = True
            
            # iterate through children
            for c in node.dependents:     
                # reduce number of dependencies by 1                            
                c.no_of_dependencies -= 1
                # if number of number of pre-requisites drops to 0 
                # add to processing q. 
                if c.no_of_dependencies == 0 and not c.is_traversed:
                    queue.append(c)
        
        # if any node hasn't been traversed return false 
        if any(a for a in all_nodes.values() if not a.is_traversed):
            return False 
        
        return True

if __name__ == '__main__':
    s = SolutionCourseSchedule()
    print(s.canFinish(2, [[1,0],[0,1]]))
    print(s.canFinish(2, [[1,0]]))