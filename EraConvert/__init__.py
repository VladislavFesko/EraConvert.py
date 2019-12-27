__all__ = [
    'convert_ATE',
    'convert_Infinities',
    'convert_Trids',
    'convert_Tetix',
    'convert_Petix',
    'convert_Ectix',
    'convert_Zettix',
    'convert_Yottix',
    'convert_Xenux',
    'convert_YOV',
    'convert_YOC',
    'convert_YOH',
    'convert_YOA',
    'convert_xATE',
    'convert_MATE',
    'convert_YOVp',
    'convert_EEE',
    'convert_DEE',
    'convert_CME',
    'convert_PME',
    'convert_EEEp',
    'convert_EEEp2',
    'convert_EEEp3',
    'convert_xthofx',
    ]
def convert_ATE(year):
    return "n+" + year
def convert_Infinities(year):
    return "2n+" + year
def convert_Trids(year):
    return "3n+" + year
def convert_Tetix(year):
    return "4n+" + year
def convert_Petix(year):
    return "5n+" + year
def convert_Ectix(year):
    return "6n+" + year
def convert_Zettix(year):
    return "7n+" + year
def convert_Yottix(year):
    return "8n+" + year
def convert_Xenux(year):
    return "9n+" + year
def convert_YOV(year):
    return "7000000000n+" + year
def convert_YOC(year):
    return "8000000008n+" + year
def convert_YOH(year):
    return "6.66e+666n+" + year
def convert_YOA(year):
    return "13.8e+3000000000000000006n+" + year
def convert_xATE(integer, year):
    return integer + "n+" + year
def convert_MATE(year):
    return "n^2+" + year
def convert_YOVp(year):
    return "7000000000n^2+" + year
def convert_EEE(year):
    return "n^3+" + year
def convert_DEE(year):
    return "2n^3+" + year
def convert_CME(year):
    return "3n^3+" + year
def convert_PME(year):
    return "4n^3+" + year
def convert_EEEp(year):
    return "n^4+" + year
def convert_EEEp2(year):
    return "n^5+" + year
def convert_EEEp3(year):
    return "n^6+" + year
def convert_xthofx(integer, year):
    return integer + "E" + year
