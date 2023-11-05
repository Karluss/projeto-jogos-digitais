class GameState:
    def __init__(self):
        self.state = "MENU"
    
    def update(self, state): 
        self.state = state