from game import *
from utils import clamp


class Weapon:
	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name
	@classmethod
	def make_unarmed(cls):
		return cls('Unarmed',cls.UNARMED_POWER,1)

class Character:
	def __init__(self,name,max_hp,attack,defense,level,weapon,hp):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp
	@property
	def name (self):
		return self.name
	@property
	def weapon(self):
		return self.weapon
	# TODO: Affecter ce qui est passé comme valeur. Si la valeur est None, je lui met une arme vide (le Unarmed)
	@weapon.setter
	def weapon(self,val):
		if self.weapon == None:
			val = Weapon.make_unarmed()
	#si l arme est trop avancer on lance un valueerror
		if val.min_level > self.level:
			raise ValueError(Weapon)
		self.weapon = val

	# TODO: Définir getter/setter pour `hp`, qui doit être borné entre 0 et `max_hp`
	@property
	def hp(self):
		return self.hp
	@hp.setter
	def hp(self,val):
		# if 0 <= self.hp <= self.max_hp:
		# 	val = self.hp
		# else:
		# 	raise ValueError(Character)
		self.hp = clamp(val,0,self.max_hp)

	def compute_damage(self, other: "Character"):
		level_factor = (2 * self.level) / 5 + 2
		weapon_factor = self.weapon.power
		atk_def_factor = self.attack / other.defense
		critical = random.random() <= 1 / 16
		modifier = (2 if critical else 1) * random.uniform(0.85, 1.0)
		damage = ((level_factor * weapon_factor * atk_def_factor) / 50 + 2) * modifier

		return int(round(damage)), critical

	def deal_damage(attacker, defender):
		# TODO: Calculer dégâts
		damage, crit = attacker.compute_damage(defender)
		defender.hp -= damage
		print(f"{attacker.name} used {attacker.weapon.name}")
		if crit:
			print("  Critical hit!")
		print(f"  {defender.name} took {damage} dmg")

	def run_battle(c1: Character, c2: Character):
		# TODO: Initialiser attaquant/défendeur, tour, etc.
		attacker = c1
		defender = c2
		turns = 1
		print(f"{attacker.name} starts a battle with {defender.name}!")
		while True:
			# TODO: Appliquer l'attaque
			deal_damage(attacker, defender)
			# TODO: Si le défendeur est mort
			if defender.hp == 0:
				print(f"{defender.name} is sleeping with the fishes.")
				break
			turns += 1
			# Échanger attaquant/défendeur
			attacker, defender = defender, attacker
		# TODO: Retourner nombre de tours effectués
		return turns






def main():




if __name__ == "__main__":
	main()

