class Category:
    def __init__(self, key, name):
        self.key = key
        self.name = name
    
    def __str__(self):
        return f"Category: key={self.key}, name={self.name}"
