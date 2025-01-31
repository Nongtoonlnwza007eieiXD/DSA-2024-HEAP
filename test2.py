import heapq

# ฟังก์ชันที่ใช้สร้าง Max Heap
def max_heap_insert(heap, val):
    heapq.heappush(heap, -val)  # การแทรกค่าโดยใช้ค่าติดลบ

def print_heap(heap):
    print([-x for x in heap])

# ฟังก์ชันที่ใช้ลบค่าที่สูงสุดจาก Max Heap
def max_heap_pop(heap):
    largest = -heapq.heappop(heap)  
    return largest

# เริ่มต้นด้วย Max Heap ที่ว่างเปล่า
max_heap = []

# ข้อมูลที่ต้องการแทรก
values = [5, 3, 8, 1, 2, 7, 6, 4]

# แทรกค่าทุกตัวลงใน Max Heap
for val in values:
    max_heap_insert(max_heap, val)

print("Initial Max Heap:")
print_heap(max_heap) 

# ลบค่าสูงสุด 3 ครั้ง
for i in range(3):
    removed_value = max_heap_pop(max_heap)
    print(f"After removing the largest value ({removed_value}):")
    print_heap(max_heap)
