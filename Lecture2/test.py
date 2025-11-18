class InvalidRadiusException(Exception):
    pass

def compute_circle_area(r):
    # Stel: negatieve radius is niet toegelaten
    if r < 0:
        # We gooien een zelfgekozen exception met een boodschap
        raise InvalidRadiusException("Radius moet >= 0 zijn.")

    from math import pi
    return pi * r * r


def demo_raise_custom_exception():
    try:
        print("Oppervlakte met r=2:", compute_circle_area(2))
        print("Oppervlakte met r=-5:", compute_circle_area(-5))
    except InvalidRadiusException as ex:
        print("Ongeldige radius:", ex)

demo_raise_custom_exception()