import pandas as pd

def load_swat_data(filepath: str):
    """Load SWAT output (water availability) from CSV."""
    return pd.read_csv(filepath)

def load_aquacrop_data(filepath: str):
    """Load AquaCrop output (ET demand, yield potential) from CSV."""
    return pd.read_csv(filepath)
