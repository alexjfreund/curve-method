def validate_k(k_max):
    if not isinstance(k_max, int):
        raise ValueError("Maximum k value must be an integer")
    if k_max < 3 or k_max > 24:
        raise ValueError("Maximum k value must be within [3, 24]")
        
def validate_deg(deg):
    if not isinstance(deg, int):
        raise ValueError("Polynomial degree must be an integer")
    if deg < 1 or deg > 6:
        raise ValueError("Polynomial degree must be within the range [1,6]")
