import pydivert

with pydivert.WinDivert("tcp.SrcPort == 443 and tcp.PayloadLength == 0") as w:
    for packet in w:
        packet.tcp.rst = False
        w.send(packet)