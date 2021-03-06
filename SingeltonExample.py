import unittest
class Singleton:

    _instances = {}

    def __call__(cls, *a, **kw):
        if cls not in cls._instances:
            cls.__instances[cls] = super(Database, cls).__call__(cls, *a, **kw)
        return cls.__instances[cls]

class Database:
    def __init__(self):
        self.population = {}
        f = open("capitals.txt", 'r')
        lines = f.readlines()
        for i in range(1, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i+1].strip())
        f.close()

class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result

class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ["Seoul", 'Mexiko City']
        tp = rf.total_population(names)
        self.assertEqual(17500000+17400000, tp)


if __name__ == '__main__':
    unittest.main()