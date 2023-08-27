class Currency:
    def __init__(self, key, flags, iso, name, symb, syprf, dchar, gchar, frac, rate, mdate):
        self.key = key
        self.flags = flags
        self.iso = iso
        self.name = name
        self.symb = symb
        self.syprf = syprf
        self.dchar = dchar
        self.gchar = gchar
        self.frac = frac
        self.rate = rate
        self.mdate = mdate
    
    def __str__(self):
        return f"Currency: key={self.key}, flags={self.flags}, iso={self.iso}, name={self.name}, symb={self.symb}, syprf={self.syprf}, dchar={self.dchar}, gchar={self.gchar}, frac={self.frac}, rate={self.rate}, mdate={self.mdate}"
