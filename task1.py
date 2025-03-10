from abc import abstractmethod, ABC
from typing import Optional
import logging


def run_task1() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger("task1")

    class Vehicle(ABC):
        @abstractmethod
        def start_engine(self) -> None:
            pass

    class VehicleFactory(ABC):
        @abstractmethod
        def create_car(self, make: str, model: str) -> "Car":
            pass

        @abstractmethod
        def create_motorcycle(self, make: str, model: str) -> "Motorcycle":
            pass

    class USVehicleFactory(VehicleFactory):
        def create_car(self, make: str, model: str) -> "Car":
            return Car(make, model, "US Spec")

        def create_motorcycle(self, make: str, model: str) -> "Motorcycle":
            return Motorcycle(make, model, "US Spec")

    class EUVehicleFactory(VehicleFactory):
        def create_car(self, make: str, model: str) -> "Car":
            return Car(make, model, "EU Spec")

        def create_motorcycle(self, make: str, model: str) -> "Motorcycle":
            return Motorcycle(make, model, "EU Spec")

    class Car(Vehicle):
        def __init__(self, make: str, model: str, region: Optional[str] = "") -> None:
            self.make = make
            self.model = model
            self.region = region

        def start_engine(self) -> None:
            logger.info(f"{self.make} {self.model} ({self.region}): Двигун запущено")

    class Motorcycle(Vehicle):
        def __init__(self, make: str, model: str, region: Optional[str] = "") -> None:
            self.make = make
            self.model = model
            self.region = region

        def start_engine(self) -> None:
            logger.info(f"{self.make} {self.model} ({self.region}): Мотор заведено")

    logger.info("Using factories to create vehicles:")
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    # Creating US vehicles
    us_car = us_factory.create_car("Ford", "Mustang")
    us_car.start_engine()

    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_motorcycle.start_engine()

    # Creating EU vehicles
    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_car.start_engine()

    eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Monster")
    eu_motorcycle.start_engine()


if __name__ == "__main__":
    run_task1()
