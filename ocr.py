from paddleocr import PaddleOCR
from PIL import Image

def inpt():
    ocr = PaddleOCR(use_doc_orientation_classify=False,use_doc_unwarping=False,use_textline_orientation=False)
    grid = ocr.predict(input="assets/grid.png")
    for res in grid:
        res.print()
        res.save_to_json(save_path="assets/grid.json") 
    grid = ocr.predict(input="assets/words.png")
    for res in grid:
        res.print()
        res.save_to_json(save_path="assets/words.json") 
            