# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SolutionMinMeetingRooms(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """        
        if not intervals: 
            return 0 
        
        meet_starts = [interval.start for interval in sorted(intervals, key=lambda i: i.start)]
        meet_ends = [interval.end for interval in sorted(intervals, key=lambda i: i.end)]
        
        i = 0
        j = 0
        max_overlaps = 1
        overlaps = 0 
        while i < len(intervals) and j < len(intervals): 
            if meet_starts[i] < meet_ends[j]:
                overlaps += 1
                if overlaps > max_overlaps: 
                    max_overlaps = overlaps
                i += 1
            else: 
                overlaps -= 1
                j += 1
            
        return max_overlaps 

if __name__ == '__main__':
    intervals = [Interval(l[0], l[1]) for l in [[6,17],[8,9],[11,12],[6,9]]]
    s = SolutionMinMeetingRooms()
    print(s.minMeetingRooms(intervals))