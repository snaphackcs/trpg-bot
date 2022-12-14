

class Player:
    """
    Player
    ================================
    """

    def __init__(self, player_id: str):
        self.id = player_id
        self.role = None
        self.ready = False

    def get_id(self):
        return self.id

    def set_ready(self):
        self.ready = True

    def is_ready(self):
        return self.ready
