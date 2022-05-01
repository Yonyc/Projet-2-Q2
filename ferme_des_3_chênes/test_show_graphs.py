import unittest
from show_graph import lune, velages, show_races

class TestVelage(unittest.TestCase):

    def test_valid(self):
        debut = "20/03/2000"
        fin = "10/04/2020"
        data = [("10/02/2010", "1"), ("10/02/2010", "2"), ("10/02/2021", "3")]
        self.assertEqual(velages(data, debut, fin), {"10/02/2010":2})

    def test_empty(self):
        debut = "20/03/2000"
        fin = "10/04/2020"
        data2 = []
        self.assertEqual(velages(data2, debut, fin), {})

class TestLune(unittest.TestCase):

    def test_valid(self):
        debut = "20/03/2000"
        fin = "10/04/2020"
        data = [("21/03/2019", "1"), ("10/02/2010", "2"), ("10/02/2021", "3"), ("18/01/2022", "4")]
        #21/03/2019 et 18/01/2022 sont bien des jours de pleine lune mais le second est hors des dates admises
        self.assertEqual(lune(data, debut, fin), {'Pleine Lune':["1"], 'Lune incomplète':["2"]})

    def test_empty(self):
        debut = "20/03/2000"
        fin = "10/04/2020"
        data2 = []
        self.assertEqual(lune(data2, debut, fin), {'Lune incomplète': [], 'Pleine Lune': []})

class TestRaces(unittest.TestCase):

    def test_races_in(self):
        race = ('rouge', 'bleue')
        pourcentage = 0.1
        data = [(0.9, "bleue"), (0.3, "rouge"), (0.2, "rouge")]
        self.assertEqual(show_races(data, race, pourcentage), {'rouge':2, 'bleue':1})

    def test_out_of_pourcentage(self):
        race = ('rouge', 'bleue')
        pourcentage = 0.4
        data = [(0.1, "bleue"), (0.3, "rouge"), (0.2, "rouge")]
        self.assertEqual(show_races(data, race, pourcentage), {})


    def test_no_races_in(self):
        race = ('jaune', 'bleue')
        pourcentage = 0.1
        data = [(0.1, "rouge"), (0.3, "rouge"), (0.2, "rouge")]
        self.assertEqual(show_races(data, race, pourcentage), {})


if __name__ == '__main__':
    unittest.main()