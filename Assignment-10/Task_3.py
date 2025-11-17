class emp:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def inc(self,p):
        self.s=self.s+(self.s*p/100)
    def pr(self):
        print("emp:",self.n,"salary:",self.s)


# Example usage (still poorly formatted on purpose)
if __name__=="__main__":
    e=emp("bob",1000)
    e.inc(10)
    e.pr()
