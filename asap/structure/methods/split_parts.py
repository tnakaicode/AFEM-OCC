from OCC.GEOMAlgo import GEOMAlgo_Splitter

from .reshape_parts import reshape_parts


def split_part(part, splitter, split_both=True):
    """
    Split a part with another part or shape. 
    """
    if part.IsNull() or splitter.IsNull():
        return False

    # Split the parts.
    geom_split = GEOMAlgo_Splitter()
    geom_split.AddArgument(part)
    if split_both:
        geom_split.AddArgument(splitter)
    else:
        geom_split.AddTool(splitter)
    geom_split.Perform()
    if geom_split.ErrorStatus() != 0:
        return False

    # Replace modified shapes.
    if split_both:
        return reshape_parts(geom_split, [part, splitter])
    return reshape_parts(geom_split, [part])
