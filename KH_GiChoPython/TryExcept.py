class Toilet:
    using=False #이렇게해도되네.
    
    # def __init__(self):
    #     self.using=False
    
    def in_use(self):
        if self.using==False:
            print("화장실을 사용합니다.")
            self.using=True
        else :
            raise Exception("안에 사람이 있어요 기다려주세요.")
    
    def not_in_use(self):
        self.using=False
        print("안에사람이없습니다.")

man1=Toilet()
while True:
    use= input("화장실을 사용하시겠습니까?y/n")
    try:
        if use =="y":
            man1.in_use()
        else:
            man1.not_in_use()
    except Exception as e:
        print(e)