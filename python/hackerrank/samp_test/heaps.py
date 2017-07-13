def heapify(heap):
    root = (len(heap)-1)/2   
    while root >= 0:        
      down_heapify(heap, root)
      root -= 1
        
def down_heapify(heap, root):
    large_index = root
    left_child = 2*root+1
    right_child = 2*root+2
    if (left_child < len(heap)) and (heap[large_index] < heap[left_child]):
        large_index = left_child 
    if (right_child < len(heap)) and (heap[large_index] < heap[right_child]):
        large_index = right_child      
    if root != large_index:
        heap[large_index], heap[root] = heap[root], heap[large_index]
        down_heapify(heap,large_index)

def find_key(heap,root,k):
    left_child = 2*root+1
    right_child = 2*root+2
    found = False
    while not found:
      heap

def findNumber(arr, k):
    #build heap and then search it
    heapify(arr)
    print arr
    res = find_key(arr, 0, k)
    return res

a = [5,2,3,6,7,20,21,99]
print a
print findNumber(a, 7)
print findNumber(a,3)
print findNumber(a,21)
print findNumber(a,20)
print findNumber(a,99)
print findNumber(a,98)
print findNumber(a,4)

