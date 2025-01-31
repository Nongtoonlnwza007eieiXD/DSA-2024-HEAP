def is_max_heap(arr):
  
  n = len(arr)

  for i in range((n // 2) - 1, -1, -1):
    # ตรวจสอบว่าลูกซ้ายมีค่ามากกว่าพ่อหรือไม่
    if 2 * i + 1 < n and arr[i] < arr[2 * i + 1]:
      return False

    # ตรวจสอบว่าลูกขวามีค่ามากกว่าพ่อหรือไม่
    if 2 * i + 2 < n and arr[i] < arr[2 * i + 2]:
      return False

  return True

# ตัวอย่างการใช้งาน
array1 = [16, 4, 10, 1, 3, 5, 7]
print(f"{array1} Max Heap: {is_max_heap(array1)}")

array2 = [1, 3, 5, 7, 4, 10, 16]
print(f"{array2} Max Heap: {is_max_heap(array2)}") 
