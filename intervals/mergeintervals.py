"""
Problem: 
Given a list of intervals merge them to remove overlaps. Intervals where end value of 
one equals to start value of the other should be merged  

Algorithm 1:
Idea of the algorithm is this. We pick first interval and iterate through rest of the list 
to find intervals that need to be merged into this interval. As we iterate, we update start 
and end of the first interval to what merged interval would look like. If we do not find any 
intervals that merge with this first interval, we can move to next interval else repeat process 
for same first interval since the previous iteration interval update could 
now bring in new intervals to merge. See, below for explanation
Example 
[1, 4], [5, 6], [3, 8]

Iteration 1: 
[1, 4] is merged with rest of the list. 
[1, 4] currently does not merge with [5, 6] but merges with [3, 8]
So at end of iteration 1 we will update [1, 4] to [1, 8] and remove interval [3, 8]

So our new interval list looks like 
[1, 8], [5, 6]

Iteration 2: 
In this iteration [1, 8] merges with [5, 6] 
At end of iteration 2 we remove [5, 6]. 
First interval does not change. 

Iteration 3: 
Interval list is reduced to just [1, 8]. 
Inner loop has no 

Interval list is empty 
return output. 

Comments provide a better explanation for merging two individual intervals 

Time Complexity = O(n ^ 2) 
Space Complexity = O(1)

Algorithm 2: 
We first sort interval list by start value. Now we can start merging 
intervals. Start with first interval. 
Add it to result. 
Two possibilities for next interval: 
1. Next interval merges with last interval in result (interval.start <= result[-1].end). 
Update last interval with max of interval.end and result[-1].end 
2. Next interval lies to the right last interval in result. In this case 
we can add next interval to result
3. Move to next interval and repeat 

Time Complexity = O(n * log n) + O(n) 
Space Complexity = O(n). (Possible to reduce to O(1) by deleting intervals instead of appending to result list) 
"""

print(__doc__)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)
    
    def __str__(self):
        return "[{},{}]".format(self.start, self.end)


class SolutionMergeInterval(object):
    def merge1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) == 1:
            return intervals
        
        interval_index = 0      
        while interval_index < len(intervals):
            # Pick interval for processing            
            f = intervals[interval_index]            
            rm_list = []
            
            # try to merge with intervals that follow  
            for i in range(interval_index + 1, len(intervals)):
                # current intervals completely covers check interval 
                if f.start <= intervals[i].start and f.end >= intervals[i].end:                    
                    rm_list.append(i)
                # if current interval start lies between check interval                
                elif intervals[i].start <= f.start <= intervals[i].end:
                    # new start is check interval start 
                    f.start = intervals[i].start
                    # end is check interval end if check interval is greater 
                    if f.end < intervals[i].end: 
                        f.end = intervals[i].end
                    # mark check interval for removal                      
                    rm_list.append(i)
                # if current interval end lies between check interval start and end
                # check interval end becomes merged interval end 
                elif intervals[i].start <= f.end <= intervals[i].end: 
                    f.end = intervals[i].end                    
                    rm_list.append(i)
            
            # Remove intervals in rm_list
            if rm_list: 
                while rm_list: 
                    del intervals[rm_list.pop()]
            else: 
                # else go to next interval 
                interval_index += 1
        
        return intervals 
    
    def merge2(self, intervals):
        result = []
        # sort by interval start.
        # and iterate through list of intervals
        for interval in sorted(intervals, key= lambda x: x.start):
            # if result array is not empty check if 
            # current interval lies between last interval stored 
            # in result list
            if result and interval.start <= result[-1].end:
                # if yes set result.end to max of result.end and 
                # current interval end 
                result[-1].end = max(interval.end, result[-1].end) 
            else:
                # new interval falls outside so add to result
                result.append(interval)
        
        return result 
                      
                      
if __name__ == '__main__':    
    tests = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1, 3],[3, 6]],
        [[3, 6],[1, 3]],
        [[1, 4],[5, 6],[3, 8]]
    ]
    
    s = SolutionMergeInterval()
    for l in tests:
        interval_list = []
        for li in l:   
            interval_list.append(Interval(li[0], li[1]))
        print("Input:") 
        print(interval_list)
        print("Answer:")
        print(s.merge2(interval_list))
        print()
#         print(s.merge1(interval_list))
    
    
    