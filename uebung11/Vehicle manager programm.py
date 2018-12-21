class Vehicle:

    def __init__(self, brand, model, kilometer, service_date):
        self.brand = brand
        self.model = model
        self.kilometer = kilometer
        self.service_date = service_date

    def vehicle_info(self):
        return self.brand + " " + self.model


# aktuelle Fuhrparkliste
def list_of_vehicles(car_park):
    if not car_park:
        print("")
        print("You have no cars in your Car-park. Press 2 if you want to add a car\n")

    else:
        for index, vehicle in enumerate(car_park):
            print("ID:{} ".format(str(index)))
            print("Brand: {}".format(vehicle.brand))
            print("Model: {}".format(vehicle.model))
            print("kilometer: {}".format(vehicle.kilometer))
            print("Service date: {}".format(vehicle.service))
            print("")


#Fahrzeug hinzufuegen
def add_new_vehicle(car_park):
    brand = raw_input("Car Brand: ")
    model = raw_input("Car Model: ")
    kilometer = raw_input("kilometer: ")
    service_date = raw_input("Service date: ")

    new_car = Vehicle(brand=brand, model=model, kilometer=kilometer, service_date=service_date)
    car_park.append(new_car)
    print("")
    print("You added: " + new_car.vehicle_info())


# kilometer bearbeiten
def edit_kilometer(car_park):
    print("Select vehicle ID to update kilometer")

    for index, vehicle in enumerate(car_park):
        print(str(index) + "\n " + vehicle.vehicle_info())

    print("")
    id_num = raw_input("ID num: ... ")
    selected_id = car_park[int(id_num)]

    new_kilometer = raw_input("Enter kilometer value for {}: ".format(selected_id.vehicle_info()))
    selected_id.kilometer = new_kilometer

    print("")
    print("Kilometer updated for {}".format(selected_id.vehicle_info()))


# service bearbeiten
def edit_service(car_park):
    print("Select vehicle ID to update service date")

    for index, vehicle in enumerate(car_park):
        print(str(index) + "\n" + Vehicle.vehicle_info(vehicle))

    print("")
    id_num = raw_input("ID num: ... ")
    if id_num != car_park[int(id_num)]:
        print("That ID does not exist")

    selected_id = car_park[int(id_num)]

    new_service = input("Enter mileage value for {}: ".format(selected_id.vehicle_info()))
    selected_id.service = new_service

    print("")
    print("Service date updated for {}".format(selected_id.vehicle_info()))


def save(car_park):
    with open("vehicles.txt", "w+") as veh_file:
        for index, vehicle in enumerate(car_park):
            veh_file.write("ID: ()\n".format(str(index)))
            veh_file.write("%s\n%s\n%s\n%s\n\n" % (vehicle.brand, vehicle.model, vehicle.kilometer, vehicle.service_date))



def main():
    car_park = []
    print("Welcome to your car park program.")

    while True:
        print ""
        print"Select options"
        print"1) Show current car park"
        print"2) Add new vehicle"
        print"3) Edit vehicles kilometer"
        print"4) Edit vehicles service date"
        print"q) Save & Exit \n"


        selection = raw_input("Select action: ")

        if selection == "1":
            list_of_vehicles(car_park)
        elif selection == "2":
            add_new_vehicle(car_park)
        elif selection == "3":
            edit_kilometer(car_park)
        elif selection == "4":
            edit_service(car_park)
        elif selection == 'q'.lower():
            print("Thank you. Your selection is saved.")
            save(car_park)
            break
        else:
            print("Please try again.")
            continue


if __name__ == "__main__":
    main()




