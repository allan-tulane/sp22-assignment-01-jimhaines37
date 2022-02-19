"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def recrFib(x):
    if x <= 1:
        return x 
    else:
        aVar = recrFib(x-1) 
        bVar = recrFib(x-2)
        return aVar + bVar
        pass

def longest_run(mylist, key):
    streak = 0
    maxStreak = 0
    
    for i in mylist:
        if i == key:
            streak += 1
            if streak > maxStreak:
                maxStreak = streak
        else: 
            streak = 0
    return maxStreak
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def combine(firstResult, secondResult):
    #3 cases: both results perfectly match key, one result is matches key perfectly but other does not, longest run is from combination of both results
    
    #1, both results are entire range
    if firstResult.is_entire_range:
        
    
def longest_run_recursive(mylist, key):
    
    #2 bases cases: 1 element in the list that is the key, or 1 element that is not the key
    if len(mylist) == 1 and mylist[0] = key: result = Result(1,1,1,True)
    elif len(mylist) == 1 and mylist[0] != key: result = Result(0,0,0,False)
        
    #actual recursive calls
    else:
        mid = len(mylist)//2
        firstResult = longest_run_recursive(mylist[0:mid], key)
        secondResult = longest_run_recursive(mylist[mid:len(mylist)], key)
        result = combine(firstResult, secondResult)
    return result
    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


