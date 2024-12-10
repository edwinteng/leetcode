class BrowserHistory:

    def __init__(self, homepage: str):
        self.past = []
        self.forward_history = []
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.past.append(url)
        self.forward_history.clear()

    def back(self, steps: int) -> str:
        while steps >0 and len(self.past)>1:
            site = self.past.pop()
            self.forward_history.append(site)
            steps-=1
        return self.past[-1]

    def forward(self, steps: int) -> str:
        while steps >0 and len(self.forward_history):
            site = self.forward_history.pop()
            self.past.append(site)
            steps-=1
        return self.past[-1]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)