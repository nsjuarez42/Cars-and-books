class Motor:

    def __init__(self,cilinders,cv,hp):
        self.cilinders = cilinders
        self.cv = cv
        self.hp = hp
        self.working = False

    def work(self):
        if not self.working:
            self.working = True
        else:
            
            
        
    def stop_working(self):
        if self.working:
            self.working = False
        else:
            print("")
