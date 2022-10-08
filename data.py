# check worlds, skills

# professions
# 1 : None
# 2 : Knights
# 3 : Paladins
# 4 : Sorcerers
# 5 : Druids

# category - can be picked any to scrap whole highscores of selected category
# 1 : Achievements
# 2 : Axe Fighting
# 15 : Boss Points
# 3 : Charm Points
# 4 : Club Fighting
# 5 : Distance Fighting
# 14 : Drome Score
# 6 : Experience Points
# 7 : Fishing
# 8 : Fist Fighting
# 9 : Goshnar's Taint
# 10 : Loyalty Points
# 11 : Magic Level
# 12 : Shielding
# 13 : Sword Fighting


def world():
    worlds = ['Adra', 'Alumbra', 'Antica', 'Ardera', 'Astera', 'Axera',
              'Bastia', 'Batabra', 'Belobra', 'Bombra', 'Bona', 'Cadebra',
              'Calmera', 'Castela', 'Celebra', 'Celesta', 'Collabra',
              'Damora', 'Descubra', 'Dibra', 'Epoca', 'Esmera', 'Famosa',
              'Fera', 'Ferobra', 'Firmera', 'Gentebra', 'Gladera', 'Harmonia',
              'Havera', 'Honbra', 'Illusera', 'Impulsa', 'Inabra', 'Issobra',
              'Kalibra', 'Kardera', 'Karna', 'Libertabra', 'Lobera', 'Luminera',
              'Lutabra', 'Marbera', 'Marcia', 'Menera', 'Monza', 'Mudabra',
              'Mykera', 'Nadora', 'Nefera', 'Nossobra', 'Ocebra', 'Olima',
              'Ombra', 'Optera', 'Ousabra', 'Pacera', 'Peloria', 'Premia',
              'Quelibra', 'Quintera', 'Refugia', 'Reinobra', 'Seanera', 'Secura',
              'Serdebra', 'Solidera', 'Suna', 'Syrena', 'Talera', 'Tembra',
              'Thyria', 'Trona', 'Utobra', 'Venebra', 'Versa', 'Visabra', 'Vunira',
              'Wintera', 'Wizera', 'Xandebra', 'Yonabra', 'Zenobra', 'Zuna', 'Zunera']
    return worlds


def profession():
    prof = [2, 3, 4, 5]
    return prof


def category():
    # skill = [1, 2, 15, 3, 4, 5, 14, 6, 7, 8, 9, 10, 11, 12, 13]
    skill = 6
    return skill
