import heapq

class ProductRanking:
    def __init__(self, k):
        self.k = k
        self.products = []  # Min Heap เก็บ k สินค้าขายดีที่สุด
    
    def update_sales(self, product_id, sales):
        if len(self.products) < self.k:
            heapq.heappush(self.products, (sales, product_id))
        else:
            if sales > self.products[0][0]:
                heapq.heapreplace(self.products, (sales, product_id))
    
    def get_top_k(self):
        return sorted(self.products, reverse=True)

# ตัวอย่างการใช้งาน
ranking = ProductRanking(3)  # เก็บ 3 อันดับสินค้าขายดี
ranking.update_sales("สินค้า A", 100)
ranking.update_sales("สินค้า B", 150)
ranking.update_sales("สินค้า C", 80)
ranking.update_sales("สินค้า D", 200)

top_k = ranking.get_top_k()
print("สินค้าขายดี 3 อันดับแรก:")
for sales, product_id in top_k:
    print(f"{product_id}: {sales} ยอดขาย")