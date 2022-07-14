class Trainer():
    MAX_TEAM_SIZE=3

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.pokemon =[]
        self.crit_chance = .125
        self.crit_bonus = 100

    def catch(self, poke):
        if len(self.pokemon) == Trainer.MAX_TEAM_SIZE:
            return "You have too many Pokemon"
        if poke.id in {p.id for p in self.pokemon}:
            return "You've already caught this pokemon!"
        poke.trainer = self    
        self.pokemon.append(poke)
        return f'You caught {poke.name}'


    def release(self, name):
        if name in {p.name for p in self.pokemon}:
           self.pokemon=list(filter(lambda poke: poke.name.lower() !=name.lower(),self.pokemon))
           return True
        else:
            return False
     
    def show_team(self):
        for poke in self.pokemon:
            poke.display(30)

            




#all trainers have the same max team size
# each master has a unique name, id ,pokemon list , crit chance, critical bounus
