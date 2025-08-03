from ocr import inpt
from solve import solve
from highlight import highlight

def main():
    try:
        inpt()
    except:
        print("Missing input image files detected")
        return

    try:
        answers = solve()
        highlight(answers)
        print("Puzzle solved successfully!")
    except:
        print("An error occurred while processing the puzzle")
        return
    
main()



