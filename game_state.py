class GameState:
    def __init__(self):
        self.state = "MENU"
        self.sound = "ON"
        self.restart_level = False
        self.user_name = "Player1"
        self.user_score = 0
        self.run_id = 1
    
    def update(self, state): 
        self.state = state
        if state == "LEVEL":
            self.restart_level = True
    
    def set_sound_state(self, sound):
        self.sound = sound
    
    def get_sound_state(self):
        return self.sound