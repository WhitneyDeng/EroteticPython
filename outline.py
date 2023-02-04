class Atom:
    name: str
    verifier: bool

    def __init__(self, name: str, verifier: bool = True) -> None: 
        # ∈ Definition A1
        self.verifier = verifier
        self.name = name

    def __invert__(self):
        # Definition A1
        return Atom( self.name, not self.verifier)
    def __eq__(self, other):
        return (
            self.verifier == other.verifier
        ) and (
            self.name == other.name
        )

class State:
    atoms: set[Atom]

    def __init__(self, atoms: set[Atom]) -> None:
        # ∈ Definition A2 
        self.atoms = atoms

    def __init__(self, atoms: set[(str, bool)]) -> None:
        # ∈ Definition A2 
        self.atoms = atoms
        # for each atom, convert

# Come back to A3
class States:
    states: set[State]

    def __init__(self, states: set[State]) -> None:
        self.states = states
    def __mul__(self, other: "States"): 
        # Definition A6
        raise NotImplementedError
    def __invert__(self):
        # Definition A7
        raise NotImplementedError
    def atomic_answer_potential(self, states: "States") -> int: 
        # Definition A10
        raise NotImplementedError
    def is_falsum(view: "View"): 
        raise NotImplementedError

class View:
    stage: States
    supposition: States

    def __init__(self, stage: States, supposition: States) -> None:
        # ∈ Definition A4
        self.stage = stage
        self.supposition = supposition

    def __mul__(self, other: "View"): 
        # Definition A8
        raise NotImplementedError

    def __sum__(self, other: "View"): 
        # Definition A9
        raise NotImplementedError

    def answer(self, state: States) -> "View": 
        # Definition A11
        raise NotImplementedError

    def merge(self, other: "View") -> "View": 
        # Definition A12
        raise NotImplementedError

    def update(self, other: "View") -> "View": 
        # Definition A13
        raise NotImplementedError

    def __invert__(self):
        # Definition A14
        raise NotImplementedError

    def __truediv__(self, other: "View") -> "View": 
        # Definition A15
        raise NotImplementedError

    def factor(self, other: "View") -> "View": 
        # Definition A16
        if is_falsum(other):
            raise NotImplementedError 
        else:
            raise NotImplementedError

    def suppose(self, other: "View") -> "View": 
        # Definition A17
        raise NotImplementedError

    def depose(self, other: "View") -> "View": 
        # Definition A18
        raise NotImplementedError

    def inquire(self, other: "View") -> "View": 
        # Definition A19
        raise NotImplementedError

    def query(self, other: "View") -> "View": 
        # Definition A20
        raise NotImplementedError

# Definition A4
T = View(States({State(set())}), States({State(set())}))
# Definition A4
#⊥
falsum = View(States(set()), States({State(set())}))

class Commitment:
    archive: set[View]
    spotlight: View
    
    def __init__(self, archive: set[View], spotlight: View) -> None:
        # ∈ Definition A5
        self.archive = archive
        self.spotlight = spotlight
        
    def commit(self) -> None:
        # Definition A21 (modifies self.views) 
        raise NotImplementedError
    def reorient(self, view: View) -> "Commitment": 
        # Definition A22
        assert view in {*self.views, self.view}
        return Commitment(self.views, view)