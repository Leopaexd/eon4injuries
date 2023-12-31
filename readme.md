Python-modul för att räkna ut och slå fram skador till rollspelet Eon IV

## Användning

### Importera och skapa en instans av klassen InjuryRoller:
    from eon4injuries.injuries import InjuryRoller
    
    injuryroller = InjuryRoller()

###  Anropa metoden injury_effects:
Obligatoriska parametrar är (reducerad) skadeverkan och skadetabell. Skadetabellen anges exakt som den är döpt i
reglerna, t ex "Brännskada" eller "Slagsmålsskada mot torso". De skadetabeller som används är de mer utförliga som finns
i stridsboken.

Det finns två frivilliga parametrar: "table_modifier" och "verbose".

"table_modifier" (default = 0) är eventuell modifikation av skadetabellslaget (t ex pga
vapenegenskap) och kan vara positiv eller negativ.

"verbose" (default = True) anger om resultatet ska skrivas ut eller inte.

#### Exempelanrop:

    injuryroller.injury_effects(13, 'Slagsmålsskada mot huvud')
    injuryroller.injury_effects(25, 'Stickskada mot ben', 1, verbose=False)

#### Resultat:
Metoden returnerar en lista med längd 3 på formen
[utmattning, dödsslag, beskrivning], t ex:

    [4, 0, '7 Kopplat strypgrepp. [Omtöcknad, Greppad.]\n']

Om parametern "verbose" används skrivs en beskrivning ut, t ex:

    Utmattning: 4
    Slagsmålsskada mot huvud (mod: +1): 5 Ansikte: Upprepade käftsmällar spräcker läppen och en tand sväljs. [1 tand utslagen.] Skalle: Hårda slag mot skallen grumlar blicken. [Omtöcknad.] Hals: Ett fösande slag trycker offret bakåt. [Tillbakaknuffad.]
    (resultat: 5)