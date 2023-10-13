# author: Oliver Glant
# email: oliver.glant@gmail.com
# Eon IV injuries roller

from eon4dice import roll
from Skadetabell import Skadetabell

# injuryroller.injury_effects(13, 'Huggskada mot huvud', +1, verbose=False)


class InjuryRoller:
    def __init__(self):
        self.skadetabell = Skadetabell()

    def injury_effects(self, damage, damagetable, table_modifier=0, verbose=True):
        # Funktionen tar skadeverkan och skadetyp och fastställer effekterna av skadan.
        # Parametern table_modifier är eventuella modifikationer på tabellslaget från t ex vapenegenskap
        # Returnerar en lista
        effects = [0, 0, '']  # utmattning, dödsslag, beskrivning

        # beräkna utmattning
        if damage > 0:
            if damage < 5:
                effects[0] = 1
            else:
                effects[0] = int((damage - damage % 5) / 2.5)
        if verbose:
            print('Utmattning:', effects[0])
        # Skadetabell
        if damage > 9:
            table_roll = roll('1T10') + (effects[0] - 4) + table_modifier
            result = table_roll  # används för att beräkna dödsslag om resultatet är över 20
            if table_roll > 20:
                table_roll = 20
            elif table_roll < 1:
                table_roll = 1
            effects[2] = self.skadetabell.table[damagetable][table_roll]
            if verbose:
                print(f'{damagetable}{f" (mod: {table_modifier:+})" if table_modifier != 0 else ""}: {effects[2]}(resultat: {result})')

        return effects