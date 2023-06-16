import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('input/test.png')