#take from unit, to unit, value

class ConversionNotPossible(Exception):
    print("Conversion error, Conversion not Possible")


def refactored(fromUnit, toUnit, value):

        formula = {('k', 'c'): lambda k: k - 273.15,
                   ('c', 'k'): lambda c: c + 273.15,
                   ('c', 'f'): lambda c: (c*1.8) + 32,
                   ('f', 'c'): lambda f: (f-32) / 1.8,
                   ('f', 'k'): lambda f: formula['f', 'c'](f) + 273.15, #reuses f->c conversion
                   ('k', 'f'): lambda k: formula['k', 'c'](k) * 1.8 + 32,    #reuses k->c confersion
                   ('m', 'y'): lambda m: m * 1.094,
                   ('y', 'm'): lambda y: y / 1.094,
                   ('y', 'mi'): lambda y: y / 1760,
                   ('m', 'mi'): lambda y: y / 1609.344,
                   ('mi', 'm'): lambda mi: mi * 1609.344,
                   ('mi', 'y'): lambda mi: mi * 1760,
                   ('y', 'y'): lambda y: y,
                   ('m', 'm'): lambda m: m,
                   ('mi', 'mi'): lambda mi: mi,
                   ('k', 'k'): lambda k: k,
                   ('f', 'f'): lambda f: f,
                   ('c', 'c'): lambda c: c}

        #try to do this, if doesnt work raise exception
        try:
            result = formula[fromUnit, toUnit](value)
            return result
        except KeyError:
            raise ConversionNotPossible
