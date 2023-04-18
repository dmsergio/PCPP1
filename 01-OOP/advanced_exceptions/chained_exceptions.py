a_list = ["First error", "Second error"]

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print
        # progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        # another exception
        try:
            int("a")
        except ValueError as z:
            print("Inner exception (z):", z)
            print("Inner exception (f):", f)
            print("Outer exception (e):", e)
            print("Outer exception referenced (z):", z.__context__)
            print("Outer exception referenced (f):", f.__context__)
            print("Is it the same object:", z.__context__ is f)
            print("Is it the same object:", f.__context__ is e)
