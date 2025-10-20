from abc import ABC, abstractmethod

class IEngine(ABC):
    @abstractmethod
    def release(self):
        raise NotImplementedError


class ICar(ABC):
    @abstractmethod
    def release_car(self, engine: IEngine):
        raise NotImplementedError


class IAbstractFactory(ABC):
    @abstractmethod
    def release_engine(self) -> IEngine:
        raise NotImplementedError

    @abstractmethod
    def release_car(self) -> ICar:
        raise NotImplementedError


class BYDEngine(IEngine):
    def release(self):
        print("BYDEngine release")


class KIAEngine(IEngine):
    def release(self):
        print("KIAEngine release")


class BYDCar(ICar):
    def release_car(self, engine: IEngine):
        engine.release()
        print("BYDCar release")


class KIACar(ICar):
    def release_car(self, engine: IEngine):
        engine.release()
        print("KIACar release")


class BYDAbstractFactory(IAbstractFactory):
    def release_engine(self) -> IEngine:
        return BYDEngine()

    def release_car(self) -> ICar:
        return BYDCar()


class KIAAbstractFactory(IAbstractFactory):
    def release_engine(self) -> IEngine:
        return KIAEngine()

    def release_car(self) -> ICar:
        return KIACar()


if __name__ == "__main__":
    byd_factory = BYDAbstractFactory()
    byd_engine_object = byd_factory.release_engine()
    byd_car_object = byd_factory.release_car()
    byd_car_object.release_car(engine=byd_engine_object)
    
    
    kia_factory = KIAAbstractFactory()
    kia_engine_object = kia_factory.release_engine()
    kia_car_object = kia_factory.release_car()
    kia_car_object.release_car(engine=kia_engine_object)
