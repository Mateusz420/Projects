def load_list():
    citizens = list()
    citizen = list()
    citizen_sort = 1

    with open("list.txt", "r") as citizens_initial:
        citizens_initial = citizens_initial.read()
        citizens_initial = citizens_initial.split(',')
        citizens_initial = [no_white.strip() for no_white in citizens_initial]

        for i in citizens_initial:
            if citizen_sort == 1:
                citizen.append(i)
            elif citizen_sort == 2:
                citizen.append(int(i))
            elif citizen_sort == 3:
                citizen.append(i)
                citizens.append(citizen)
                citizen = list()
                citizen_sort = 0
            citizen_sort += 1

    return citizens


def main():
    citizens = load_list()

    for i in sorted(citizens, key=lambda x: x[1]):
        print(i)


if __name__ == "__main__":
    main()
