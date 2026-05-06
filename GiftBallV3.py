from abc import ABC, abstractmethod

# Interface de l'état de la machine.
# Chaque état doit implémenter les actions possibles.
class State(ABC):
    @abstractmethod
    def insert_token(self, machine):
        """Action quand on insère un jeton."""
        pass

    @abstractmethod
    def eject_token(self, machine):
        """Action quand on éjecte un jeton."""
        pass

    @abstractmethod
    def turn_crank(self, machine):
        """Action quand on tourne la manivelle."""
        pass

    def __str__(self):
        return self.__class__.__name__


# État lorsque la machine n'a pas de jeton.
class NoTokenState(State):
    def insert_token(self, machine):
        print("Jeton inséré.")
        machine.set_state(machine.one_token_state)

    def eject_token(self, machine):
        print("Aucun jeton à éjecter.")

    def turn_crank(self, machine):
        print("Un jeton doit d'abord être inséré.")


# État lorsque la machine a un jeton inséré.
class OneTokenState(State):
    def insert_token(self, machine):
        print("Un jeton est déjà inséré.")

    def eject_token(self, machine):
        print("Jeton éjecté.")
        machine.set_state(machine.no_token_state)

    def turn_crank(self, machine):
        # Si plus de boules, on passe à l'état rupture.
        if machine.ball_count <= 0:
            print("Plus de boules disponibles.")
            machine.set_state(machine.sold_out_state)
            return

        # Distribution d'une boule.
        machine.ball_count -= 1
        machine.set_state(machine.sold_state)
        print("Boule surprise délivrée!")

        # Passage à l'état suivant selon le stock.
        if machine.ball_count > 0:
            machine.set_state(machine.no_token_state)
        else:
            machine.set_state(machine.sold_out_state)


# État temporaire après la vente d'une boule.
class SoldState(State):
    def insert_token(self, machine):
        print("Veuillez attendre, une boule a déjà été vendue.")

    def eject_token(self, machine):
        print("Impossible d'éjecter un jeton après vente.")

    def turn_crank(self, machine):
        print("La manivelle a déjà été tournée.")


# État lorsque la machine est en rupture de stock.
class SoldOutState(State):
    def insert_token(self, machine):
        print("Impossible d'insérer un jeton : plus de boules.")

    def eject_token(self, machine):
        print("Aucun jeton à éjecter.")

    def turn_crank(self, machine):
        print("Plus de boules disponibles.")


# Machine à distribuer les balles surprise.
class GiftBall:
    def __init__(self, ball_count: int):
        self.ball_count = ball_count
        self.no_token_state = NoTokenState()
        self.one_token_state = OneTokenState()
        self.sold_state = SoldState()
        self.sold_out_state = SoldOutState()
        self.current_state = self.no_token_state if ball_count > 0 else self.sold_out_state

    def set_state(self, state):
        """Changer l'état courant de la machine."""
        self.current_state = state

    def status(self):
        return f"{self.current_state} ({self.ball_count} boules)"

    def insert_token(self):
        self.current_state.insert_token(self)

    def eject_token(self):
        self.current_state.eject_token(self)

    def turn_crank(self):
        self.current_state.turn_crank(self)


if __name__ == "__main__":
    machine = GiftBall(3)
    print(machine.status())
    machine.insert_token()
    print(machine.status())
    machine.turn_crank()
    print(machine.status())

    machine.insert_token()
    machine.eject_token()
    print(machine.status())

    machine.insert_token()
    machine.turn_crank()
    print(machine.status())

    machine = GiftBall(0)
    print(machine.status())
    machine.insert_token()
    machine.turn_crank()

    machine = GiftBall(1)
    machine.insert_token()
    machine.turn_crank()
    print(machine.status())
