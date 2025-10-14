class Counter:
        
        def __init__(self, name: str, description: str):
                self.count = 0
                self.name = name
                self.description = description

        def increment(self):
                self.count += 1

        def reset(self):
                self.count = 0

        def __str__(self):
                return f"{self.name},{self.count}"
