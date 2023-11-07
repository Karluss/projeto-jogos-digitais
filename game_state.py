class GameState:
    def __init__(self):
        self.state = "MENU"
        self.sound = "ON"
    
    def update(self, state): 
        self.state = state
    
    def set_sound_state(self, sound):
        self.sound = sound
    
    def get_sound_state(self):
        return self.sound