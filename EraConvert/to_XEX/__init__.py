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
    'convert_xATE',
    'convert_MATE',
    'convert_EEE',
    'convert_EEEp',
    'convert_EEEp2',
    'convert_EEEp3',
    ]
def convert_ATE(year):
    return "2E" + year
def convert_Infinities(year):
    return "3E" + year
def convert_Trids(year):
    return "4E" + year
def convert_Tetix(year):
    return "5E" + year
def convert_Petix(year):
    return "6E" + year
def convert_Ectix(year):
    return "7E" + year
def convert_Zettix(year):
    return "8E" + year
def convert_Yottix(year):
    return "9E" + year
def convert_Xenux(year):
    return "10E" + year
def convert_YOV(year):
    return "7000000000E" + year
def convert_YOC(year):
    return "8000000008E" + year
def convert_YOH(year):
    return "6.66e+666E" + year
def convert_xATE(integer, year):
    return integer + "E" + year
def convert_MATE(year):
    return "13.8e+3000000003E" + year
def convert_EEE(year):
    return "13.8e+2999999999999999997-1" + year
def convert_EEEp(year):
    return "13.8e+3000000000000000000-1E" + year
def convert_EEEp2(year):
    return "13.8e+3000000000000000003-1E" + year
def convert_EEEp3(year):
    return "13.8e+3000000000000000006-1E" + year
