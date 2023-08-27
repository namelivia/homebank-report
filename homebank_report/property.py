class Property:
    def __init__(self, title, curr, auto_smode, auto_weekday):
        self.title = title
        self.curr = curr
        self.auto_smode = auto_smode
        self.auto_weekday = auto_weekday
    
    def __str__(self):
        return f"Property: title={self.title}, curr={self.curr}, auto_smode={self.auto_smode}, auto_weekday={self.auto_weekday}"
