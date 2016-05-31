"""Other packages of interest:

- parapy.io: read from or write to common data files (.csv, .json, .xlsx)
- parapy.geom: library with curve, surface and solid classes and routines.
- parapy.geom.exchange: import from or export to standard geometry formats
    (.iges, .step, .stl, .brep).
- parapy.mesh: library with mesh control and algorithms classes and routines.
- parapy.cae: solutions specific to Computer-Aided Engineering tools
    (NASTRAN, VSAERO).
- parapy.api: communicating with ParaPy (HTTP, TCP, etc.).
- parapy.gui: the graphical user interface and its components.
"""

from parapy.core import *
from parapy.gui import *
from MainFolder.Components.Aircraft.Parameters import MaCruise

class exParapy(Base):

    MachCruise = Input(0.8)

    @Attribute
    def Maaach(self):
        return MaCruise.MaCruise.Mach()


obj=exParapy()
display(obj)


