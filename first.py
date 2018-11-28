def print_star(size):
    for rounds in range(size):
        for space in range(size-rounds):
            print("*", end='')
        print()


print_star(5)
