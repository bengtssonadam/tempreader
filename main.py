import requests


def get_temp_data():

    t = requests.get('http://localhost:9080/temp')
    room = t.json()
    temps = room['room_temp']
    temps = list(filter(None,temps))

    return temps

def print_all_temps(temps):
    for temp in temps:
        print('Temperature = ' + temp)


def print_last_temp(temps):
    latest_read = temps[len(temps)-1]
    print('Senast uppmäta temperatur = ' + latest_read)


def meny():
    readings = get_temp_data()
    menu = """
       Välj ett alternativ
       1. Visa alla uppmäta temperaturer:
       2. Visa senast uppmäta temperatur
       3. Avsluta
       """

    loop = True
    while loop:
        print(menu)
        choice = int(input("Val: "))

        if choice == 1:
            print_all_temps(readings)
        elif choice == 2:
            print_last_temp(readings)
        elif choice == 3:
            loop = False
        else:
            print("Fel välj igen")


if __name__ == '__main__':
    meny()

