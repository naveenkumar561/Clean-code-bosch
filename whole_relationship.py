class BoschTPMS:
    def __init__(self):
        print("BoschTPMS Constructed")

    def __del__(self):
        print("BoschTPMS Destructed")


class Engine:
    def __init__(self):
        print("Engine Constructed")

    def __del__(self):
        print("Engine Destructed")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.tpms = BoschTPMS()
        print("Car Constructed")

    def __del__(self):
        print("Car Destructed")


def build_car():
    alto = Car()


if __name__ == "__main__":
    build_car()
