from Engine import Chess

chess = Chess()
chess.Start()


while True:
    from_pos = input("from: ")
    to_pos = input("to: ")
    chess.MovePiece(from_pos, to_pos)