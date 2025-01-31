import heapq
from datetime import datetime
import time

class BankCustomer:
    def __init__(self, queue_number, service_type, is_premium=False):
        self.queue_number = queue_number  # ใช้หมายเลขคิวแทนชื่อ
        self.service_type = service_type
        self.is_premium = is_premium
        self.arrival_time = datetime.now()

        # กำหนดลำดับความสำคัญตาม service_type และสถานะลูกค้า
        self.priority = self._calculate_priority()

    def _calculate_priority(self):
        # ลำดับความสำคัญ (ยิ่งน้อยยิ่งสำคัญ)
        priority = {
            'ฝาก-ถอน': 3,
            'ชำระค่าบริการ': 2,
            'เปิดบัญชี': 1,
            'สินเชื่อ': 0
        }

        # ลูกค้า Premium จะได้ priority สูงกว่าปกติ 1 ระดับ
        base_priority = priority.get(self.service_type, 4)
        if self.is_premium:
            base_priority -= 0.5

        return base_priority

    def __lt__(self, other):
        # เปรียบเทียบลำดับความสำคัญ
        if self.priority == other.priority:
            # ถ้าความสำคัญเท่ากัน ใช้เวลามาก่อน-หลัง
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority

class BankQueue:
    def __init__(self):
        self.queue = []  # heap queue
        self.waiting_count = 0
        self.queue_number = 1  # เริ่มต้นที่เลขคิว 1

    def add_customer(self, service_type, is_premium=False):
        # เพิ่มลูกค้าในคิวและใช้หมายเลขคิว
        customer = BankCustomer(self.queue_number, service_type, is_premium)
        heapq.heappush(self.queue, customer)
        self.waiting_count += 1
        self.queue_number += 1
        
        print(f"หมายเลขคิว: {customer.queue_number}")
        print(f"บริการ: {customer.service_type}")
        print(f"สถานะ: {'Vip' if customer.is_premium else 'ทั่วไป'}")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)

    def serve_next_customer(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return None

        customer = heapq.heappop(self.queue)
        self.waiting_count -= 1

        wait_time = datetime.now() - customer.arrival_time
        print(f"\nเรียกลูกค้าหมายเลขคิว: {customer.queue_number}")
        print(f"บริการ: {customer.service_type}")
        print(f"เวลารอ: {wait_time.seconds} วินาที")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)

        return customer

    def display_queue(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return

        print("\nรายการคิวที่รอ:")
        # สร้าง copy ของคิวเพื่อไม่ให้กระทบคิวจริง
        temp_queue = self.queue.copy()
        position = 1

        while temp_queue:
            customer = heapq.heappop(temp_queue)
            print(f"{position}. คิว {customer.queue_number} - {customer.service_type}")
            position += 1
        print("-" * 30)

# ตัวอย่างการใช้งาน
def demo_bank_queue():
    bank = BankQueue()

    while True:
        print("เลือกประเภทของธุรกรรมที่ต้องการ:")
        print("1. ฝาก-ถอน")
        print("2. ชำระค่าบริการ")
        print("3. เปิดบัญชี")
        print("4. สินเชื่อ")
        print("5. ดูรายการคิวทั้งหมด")
        print("6. เรียกลูกค้าต่อไป")
        print("0. ออกจากโปรแกรม")

        choice = input("กรุณาเลือก (1-6 หรือ 0 เพื่อออก): ")

        if choice == '1':
            bank.add_customer("ฝาก-ถอน")
        elif choice == '2':
            bank.add_customer("ชำระค่าบริการ")
        elif choice == '3':
            bank.add_customer("เปิดบัญชี")
        elif choice == '4':
            vip_status = input("ลูกค้าคือ Vip หรือไม่? (y/n): ")
            is_vip = vip_status.lower() == 'y'
            bank.add_customer("สินเชื่อ", is_vip)
        elif choice == '5':
            bank.display_queue()
        elif choice == '6':
            bank.serve_next_customer()
        elif choice == '0':
            print("ออกจากโปรแกรม")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่.")

        time.sleep(1)  # เวลาหน่วงเล็กน้อย

if __name__ == "__main__":
    demo_bank_queue()
