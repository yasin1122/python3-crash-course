def saiyan(super=False):

    def super_saiyan():
        return "I am a SUPER Saiyan!!"
    
    if super:
        return super_saiyan
    else:
        return "I am a normal Saiyan!"
    
goku = saiyan(True)
print(goku())