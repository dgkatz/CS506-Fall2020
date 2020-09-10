def draw_gym(weights=1):
    dumbbell = f"❚{'█'*weights}══{'█'*weights}❚"
    box_width = 8 + weights * 2
    gym = f"""
|{'-'*box_width}|
|  {dumbbell}  |
|{'-'*box_width}|
    """
    print(gym)
