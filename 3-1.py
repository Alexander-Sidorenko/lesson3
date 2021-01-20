def div_func() :
    try:
        var_1 = int(input("Укажите первое число: "))
        var_2 = int(input("Укажите второе число: "))
    except ZeroDivisionError:
        return
    var_3 = var_2/var_1
    return var_3
print(div_func)
