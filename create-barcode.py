import barcode

ean = barcode.get('ean13', '523423789202')

ean.get_fullcode()
filename = ean.save('ean13')

options = dict(compress=True)

from barcode.writer import ImageWriter

ean = barcode.get('ean13', '523423789202', writer=ImageWriter())
filename = ean.save('ean13_')
