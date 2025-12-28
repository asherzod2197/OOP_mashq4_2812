class BankHisob:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.balans = balans

    def pul_qoshish(self, summa):
        if summa > 0:
            self.balans += summa
            print(f"{summa} so‘m qo‘shildi")
        else:
            print("Noto‘g‘ri summa")

    def pul_olish(self, summa):
        if 0 < summa <= self.balans:
            self.balans -= summa
            print(f"{summa} so‘m yechildi")
        else:
            print("Balans yetarli emas")

    def malumot(self):
        print(f"Egasi: {self.egasi} | Balans: {self.balans} so‘m")


hisob = BankHisob("Ali", 100_000)

hisob.malumot()
hisob.pul_qoshish(50_000)
hisob.pul_olish(30_000)
hisob.malumot()
