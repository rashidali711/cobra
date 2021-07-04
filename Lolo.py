import platform

bit=platform.architecture()[0]

if bit=="64bit":
    import Jutt
    Jutt.reg()
elif bit=="32bit":
    import brand
    brand.reg()
