def saiyan(super=False):

    def super_saiyan():
        return "I am a SUPER Saiyan!!"
    
    if super:
        return super_saiyan
    else:
        return "I am a normal Saiyan!"
    
goku = saiyan(True)
print(goku())

def new_decorator(original_func):
    def wrap_func():
        print("Code before the OG function")

        original_func()

        print("Code after the OG function")

    return wrap_func

@ new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")

func_needs_decorator()