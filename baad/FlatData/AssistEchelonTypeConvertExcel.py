# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AssistEchelonTypeConvertExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AssistEchelonTypeConvertExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAssistEchelonTypeConvertExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AssistEchelonTypeConvertExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AssistEchelonTypeConvertExcel
    def Contents(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AssistEchelonTypeConvertExcel
    def ConvertTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(2)
def AssistEchelonTypeConvertExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddContents(builder, Contents): builder.PrependInt32Slot(0, Contents, 0)
def AssistEchelonTypeConvertExcelAddContents(builder, Contents):
    """This method is deprecated. Please switch to AddContents."""
    return AddContents(builder, Contents)
def AddConvertTo(builder, ConvertTo): builder.PrependInt32Slot(1, ConvertTo, 0)
def AssistEchelonTypeConvertExcelAddConvertTo(builder, ConvertTo):
    """This method is deprecated. Please switch to AddConvertTo."""
    return AddConvertTo(builder, ConvertTo)
def End(builder): return builder.EndObject()
def AssistEchelonTypeConvertExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)