from afem.structure.assembly import Assembly, AssemblyAPI
from afem.topology.fix import FixShape

__all__ = ["FixAssembly"]


class FixAssembly(object):
    """
    Attempt to fix the shapes of each part in an assembly. Sub-assemblies are
    included by default.

    :param assy: The assembly. If ``None`` then the active assembly is used.
    :type assy: str or afem.structure.assembly.Assembly or None
    :param float precision: Basic precision value.
    :param float min_tol: Minimum allowed tolerance.
    :param float max_tol: Maximum allowed tolerance.

    :raise TypeError: If an :class:`.Assembly` instance is not found.
    """

    def __init__(self, assy, precision=None, min_tol=None, max_tol=None):
        assy = AssemblyAPI.get_assy(assy)
        if not isinstance(assy, Assembly):
            raise TypeError('Could not find assembly.')

        parts = assy.get_parts()
        compound = assy.as_compound()

        fix = FixShape(compound, precision, min_tol, max_tol)

        for part in parts:
            new_shape = fix.apply(part)
            part.set_shape(new_shape)

    @staticmethod
    def limit_tolerance(assy, tol=1.0e-7):
        """
        Limit tolerances for the assembly shapes.

        :param assy: The assembly. If ``None`` then the active assembly is
            used.
        :type assy: str or afem.structure.assembly.Assembly or None
        :param float tol: Target tolerance.

        :return: *True* if at least one tolerance of a sub-shape was modified.
        :rtype: bool

        :raise TypeError: If an :class:`.Assembly` instance is not found.
        """
        assy = AssemblyAPI.get_assy(assy)
        if not isinstance(assy, Assembly):
            raise TypeError('Could not find assembly.')

        shape = assy.as_compound()
        return FixShape.limit_tolerance(shape, tol)

    @staticmethod
    def set_tolerance(assy, tol):
        """
        Enforce tolerance on the given assembly.

        :param assy: The assembly. If ``None`` then the active assembly is
            used.
        :type assy: str or afem.structure.assembly.Assembly or None
        :param float tol: The tolerance.

        :return: None.

        :raise TypeError: If an :class:`.Assembly` instance is not found.
        """
        assy = AssemblyAPI.get_assy(assy)
        if not isinstance(assy, Assembly):
            raise TypeError('Could not find assembly.')

        shape = assy.as_compound()
        return FixShape.set_tolerance(shape, tol)