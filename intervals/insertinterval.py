"""
Problem: 
Given a set of intervals and a new interval insert new interval in such a way 
that new set of intervals do not overlap. 
Example 1: Inserting [1, 8] in set [1, 2], [4, 5] results in [1, 8]
Example 2: Inserting [3, 6] in set [1, 2], [2, 4], [7, 9] results in [1, 2], [2, 6], [7, 9]

ASSUMPTIONS: 
1. Current set of intervals are sorted in ascending order. 
2. No overlap between successive intervals in current set. 

Algorithm: 
Comments paint a better picture. 

In short, solution involves finding out new interval merge point by iterating 
through current intervals. Algorithm involves checking  if new interval merges 
with, lies to left of or lies to right of current interval. We add new interval 
to output if it lies to left of current interval, move to next interval in current 
set if it lies to right. If neither are True, we know new interval merges with 
current interval and we know the start index for merged interval is minimum 
of current interval and new interval. Now we look for end index for merged interval 
by iterating through remaining current intervals. Again, algorithm difficult to 
explain in abstract, use comments for better understanding.   
"""
print(__doc__)

# Inteval class
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)
    
    def __str__(self):
        return "[{},{}]".format(self.start, self.end)
    
class SolutionInterval(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals or not intervals[0]:
            return [newInterval]
        
        # represents merged list of intervals 
        output = []
        ci = 0 
        is_inserted = False
        # Iterate through current set of intervals
        while ci < len(intervals):
            # New interval lies to the left of current interval  
            if newInterval.end < intervals[ci].start : 
                # Add new interval and break
                output.append(newInterval)
                is_inserted = True
                break
            # New interval lies to the right of current interval 
            if(newInterval.start > intervals[ci].end):
                # Add current interval and continue
                output.append(intervals[ci])
                ci += 1
                continue
            
            # We found starting index for merging, 
            # minimum of new interval start and 
            # current interval start
            si = min(newInterval.start, intervals[ci].start)
            ei_found = False
            
            # Iterate through remaining set of intervals 
            while ci < len(intervals) and not ei_found:
                # Possibility Number 1: 
                # Merged interval end is before current interval
                # START, merged interval lies to left of current 
                # interval. ei is NEW INTERVAL end
                # NOTE: This statement will always be False 
                # for first current interval. It is by design 
                if newInterval.end < intervals[ci].start:
                    ei = newInterval.end
                    ei_found = True
                # Possibility Number 2: 
                # Merged interval end is before or equal to current interval 
                # END, merged interval merges with current interval 
                # ei index is CURRENT INTERVAL end. 
                elif newInterval.end <= intervals[ci].end:
                    ei = intervals[ci].end
                    ei_found = True
                    ci += 1
                # Possibility 3:
                # Merge end lies to right of current interval. Move to next interval 
                else:
                    ci += 1
            
            # We found an end index. Append to output 
            if ei_found:
                output.append(Interval(si, ei))
            # No end index found, means merged interval end > last 
            # interval end from current interval set. 
            # merged interval end = new interval end 
            else:
                output.append(Interval(si, newInterval.end))
            is_inserted = True
            break
        
        # is_inserted will stay False if new interval is to the right 
        # of last interval. Append to output. 
        if not is_inserted: 
            output.append(Interval(newInterval.start, newInterval.end))
        else:
            # new interval was merged. Append any remaining intervals
            # from current set 
            while ci < len(intervals):
                output.append(intervals[ci])
                ci += 1
        
        return output
    
    def insert2(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals or not intervals[0]:
            return [newInterval]
        
        output = []
        merged_start = None
        i = 0
        intervals.sort(key=lambda interval: interval.start)
        
        # Look for start index of merged interval
        while i < len(intervals):
            # new interval start lies to the left of current interval
            # start index is start of new interval
            if newInterval.start < intervals[i].start: 
                merged_start = newInterval.start
                break 
            # new interval start lies between start and end of current interval 
            # start index is start of current interval
            elif intervals[i].start <= newInterval.start <= intervals[i].end:
                merged_start = intervals[i].start 
                break 
            # start of merged interval lies to the right of current interval
            # add current interval to the output and move to next interval 
            output.append(intervals[i])
            i += 1
        
        # merged_start is still None. newInterval lies to the right of 
        # all existing intervals. Add newInterval to output and return 
        if merged_start == None: 
            output.append(newInterval)
            return output 
        
        # We use merged_end to figure out if end point lies to right 
        # of all remaining intervals. 
        merged_end = None
        while i < len(intervals):
            # newInterval.end is to left of current interval end
            # merged_end is newInterval.end. 
            # We've found both start and end. 
            # add interval to output and break 
            if newInterval.end < intervals[i].start:
                merged_end = newInterval.end
                output.append(Interval(merged_start, merged_end))
                break
            # merged interval ends within current interval. 
            # cur_interval end is the merged_end
            # add the merged interval. 
            # make sure we increment i by 1 before breaking
            # since we should move to the next remaining interval
            elif newInterval.end <= intervals[i].end:
                merged_end = intervals[i].end
                output.append(Interval(merged_start, merged_end))
                i += 1
                break 
            # move to next interval. 
            i += 1
        
        # merged_end is still none. 
        # newInterval encloses all remaining intervals. 
        # add merged interval to output and return output. 
        if merged_end == None: 
            output.append(Interval(merged_start, newInterval.end))
            return output 
        
        # Add any remaining intervals. 
        while i < len(intervals):
            output.append(intervals[i])
            i += 1
        
        # return result 
        return output    
                    
if __name__ == '__main__':
    print("Answer: ")    
    interval_list = [Interval(li[0], li[1]) for li in [[1,2],[3,5],[6,7],[8,10],[12,16]]]
    
    new_interval = Interval(4, 9)
    s = SolutionInterval()
    print(s.insert(interval_list, new_interval))
    print(s.insert2(interval_list, new_interval))
        