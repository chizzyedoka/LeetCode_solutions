class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curPosition = 0
        self.historySize = 1

    def visit(self, url: str) -> None: #[a, b, c, d, a]
        if len(self.history) < self.curPosition + 2:
            self.history.append(url)
        else:
            self.history[self.curPosition+1] = url
        self.curPosition += 1
        self.historySize = self.curPosition + 1
        

    def back(self, steps: int) -> str:
        self.curPosition = max(self.curPosition-steps, 0)
        return self.history[self.curPosition]

    def forward(self, steps: int) -> str:
        self.curPosition = min(self.curPosition + steps, self.historySize-1)
        return self.history[self.curPosition]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)