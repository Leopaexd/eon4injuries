from unittest import TestCase

from injuries import InjuryRoller


class TestInjuryRoller(TestCase):
    def test_injury_effects(self):
        injuryroller = InjuryRoller()
        roll1 = injuryroller.injury_effects(13, 'Slagsmålsskada mot huvud', 1, verbose=True)
        print(roll1)
        self.assertEqual(len(roll1), 3, msg='Injury result is not a list of length 3')
