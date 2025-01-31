import heapq

# ฟังก์ชันที่ใช้สร้าง Max Heap
def max_heap_insert(heap, val):
    heapq.heappush(heap, -val)  

def print_heap(heap):
    print([-x for x in heap])

max_heap = []

values = [5, 3, 8, 1, 2, 7, 6, 4]

# แทรกค่าทีละตัว
for val in values:
    max_heap_insert(max_heap, val)

print_heap(max_heap)
