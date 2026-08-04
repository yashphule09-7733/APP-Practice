from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Worker):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")


class RobotWorker(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise NotImplementedError("Robot doesn't eat")


human = HumanWorker()
human.work()
human.eat()

robot = RobotWorker()
robot.work()
robot.eat()   # Error
