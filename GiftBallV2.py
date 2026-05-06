from enum import Enum, auto

class State(Enum):
    NO_TOKEN = auto()    # pas de jeton
    ONE_TOKEN = auto()   # un jeton
    SOLD = auto()        # vendu
    SOLD_OUT = auto()    # plus de boules

# création de la classe GiftBall
class GiftBall:
    def __init__(self, ball_count: int):
        self.ball_count = ball_count
        self.current_state = State.NO_TOKEN if ball_count > 0 else State.SOLD_OUT

    # insertion d'un jeton
    def insert_token(self):
        if self.current_state == State.NO_TOKEN:
            self.current_state = State.ONE_TOKEN
        else:
            print("Impossible d'insérer un jeton maintenant.")
    
    # éjection d'un jeton
    def eject_token(self):
        if self.current_state == State.ONE_TOKEN:
            self.current_state = State.NO_TOKEN
        else:
            print("Aucun jeton à éjecter.")
    
    # action de tourner la manivelle
    def turn_crank(self):
        if self.current_state != State.ONE_TOKEN:
            print("Un jeton doit d'abord être inséré.")
            return
        
        self.ball_count -= 1
        self.current_state = State.SOLD
        print("Boule surprise délivrée!")

        if self.ball_count > 0:
            self.current_state = State.NO_TOKEN
        else:
            self.current_state = State.SOLD_OUT


# test de la classe GiftBall
if __name__ == "__main__":
    machine = GiftBall(3)
    machine.insert_token()
    machine.turn_crank()
    machine.insert_token()
    machine.eject_token()
    machine.insert_token()
    machine.turn_crank()
