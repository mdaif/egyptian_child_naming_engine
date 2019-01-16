from random import choice
from namesearchengine import BizarreNameSearchEngine


class EgyptianChildNamingEngineBase:
    ALLOWED_MALE_NAMES = (
        'Mohamed', 'Muhammad', 'Mohammad' 'Ahmed', 'Ahmad', 'Mahmoud')

    @staticmethod
    def fight(people):
        winner = people.fight()
        return winner

    def get_deceased_grandparents(self, child):
        return [
            gp for gp in child.grandparents if
            gp.is_male and gp.is_recently_deceased
        ]

    def get_heuristics(self):
        raise NotImplementedError(
            "Has to be implemented by each family, should return an arbitrary"
            " family-enforced name, such as an uncle's name, an uncle's first"
            " born's name, and so forth. None if that's not an issue.")

    def name_child(self, child):
        if child.is_male:
            deceased_gps = self.get_deceased_grandparents(child)
            if deceased_gps:
                winner = self.fight(child.parents)
                return winner.parents.father

            heuristics = self.get_heuristics()
            if heuristics:
                return heuristics
            return choice(self.ALLOWED_MALE_NAMES)
        else:
            bnse = BizarreNameSearchEngine()
            # retrieve the female names that are least known to humankind
            # such as    لمار ، ليان ، رانسى and so forth.
            bizarre_name = bnse.select().order_by(
                BizarreNameSearchEngine.COMMONALITY, order='asc').first()
            child.family.explain(bizarre_name)
            child.family.friends.explain(bizarre_name)
            return bizarre_name
