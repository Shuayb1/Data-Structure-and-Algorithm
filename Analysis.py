
'''' Given a list of numbers in random order, write an algorithm that works in O(n**2) , O(n)
  and O(nlog(n)) to find the kth smallest number in the list. '''


# O(n**2)
def do(me):
    myself = ''
    for i in me:
        im = True
        for j in me:
            if i>j:
                im = False
        if im:
            myself = i
    return myself

# o(n)
def do(me):
    myself = me[0]
    for i in me:
        if i < myself:
            myself = i
    return myself


print(do([3,4,2]))

# O(nlogn)
def analysis():
    random_list = [3,0,7, 4]    #list input
    random_list.sort()         #Sort the list
    print(random_list[0])      #the minimum will be at the first index after the sort


analysis()
