from random import choice
from namesearchengine import BizzarNameSearchEngine

class EgyptianChildNamingEngine:
  ALLOWED_MALE_NAMES = ('Mohamed', 'Muhammad', 'Mohammad' 'Ahmed', 'Ahmad', 'Mahmoud')

  def fight(self, people):
    winner = people.fight()
    return winner
  
  def get_deceased_grandparents(self, child):
    return [gp for gp in child.grandparents if gp.is_male and gp.is_recently_deceased]

  def get_heruistics():
    raise NotImplementedError(
      "Has to be subclassed by each family, should return an arbitrary family-enforced name, such as an uncle's name, uncle's first born's name, and so forth. None otherwise")

  def name_child(self, child):
    if child.is_male:
      deceased_gps = self.get_deceased_grandparents(child)
      if deceased_gps:
        winner = self.fight(child.parents)
        return winner.parents.father
        
      heuristics = self.get_heruistics()
      if heuristics:
        return heuristics
      return choice(self.ALLOWED_MALE_NAMES)
    else:
      bnse = BizzarNameSearchEngine()
      bizzar_name = bnse.select().order_by(
        BizzarNameSearchEngine.COMMONALITY, order='asc').first()
      child.family.explain(bizzar_name)
      child.family.friends.explain(bizzar_name)
      return bizzar_name

