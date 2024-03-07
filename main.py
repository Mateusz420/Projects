import pygame
import pieces_class
import pandas
import datetime

pygame.init()
clock = pygame.time.Clock()

# Setting up the screen
screen = pygame.display.set_mode((840, 840))
chess_board = pygame.image.load("chess_board.png")

# Splitting the chess board into squares
board_x = 0
board_y = 735
all_tiles = []
tiles = []
x_coords = []

for i in range(9):
    for j in range(8):
        if j != 7:
            rect = pygame.Rect(board_x, board_y, 105, 105)
            board_x += 105
            all_tiles.append(rect)
        else:
            rect = pygame.Rect(board_x, board_y, 105, 105)
            board_x = 0
            board_y -= 105
            all_tiles.append(rect)

for i in range(len(all_tiles)):
    if i % 8 == 0 and i != 0:
        tiles.append(x_coords)
        x_coords = [all_tiles[i]]
    else:
        x_coords.append(all_tiles[i])

icon = pygame.image.load("pieces\\black_pawn.png")
pygame.display.set_caption("Chess")
pygame.display.set_icon(icon)

pieces = pieces_class.Pieces()

global MOVE
MOVE ="SELECT_PIECE"
global TURN
TURN = "white"
notation_list = []



def chess_notation(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord, piece=""):
    x = [8,7,6,5,4,3,2,1]
    x_piece = x[piece_x_coord]
    y_piece = chr(97+piece_y_coord)
    x_field = x[field_x_coord]
    y_field= chr(97+field_y_coord)
    
    notation_list.append(f"{piece}{y_piece}{x_piece}-{y_field}{x_field}")
    print(notation_list)




def piece_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    
    selected_piece = df.at[piece_x_coord, piece_y_coord]
    
    if (selected_piece == pieces_class.Pieces().white_pawn):
        white_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
    elif (selected_piece == pieces_class.Pieces().black_pawn):
        black_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
    elif (selected_piece == pieces_class.Pieces().white_knight or selected_piece == pieces_class.Pieces().black_knight):
        knight_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
    elif (selected_piece == pieces_class.Pieces().white_rook or selected_piece == pieces_class.Pieces().black_rook):
        rook_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
    
    elif (selected_piece == pieces_class.Pieces().white_bishop or selected_piece == pieces_class.Pieces().black_bishop):
        bishop_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
    
    elif (selected_piece == pieces_class.Pieces().white_queen or selected_piece == pieces_class.Pieces().black_queen):
        queen_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
    elif (selected_piece == pieces_class.Pieces().white_king or selected_piece == pieces_class.Pieces().black_king):
        king_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
    
    else:
        MOVE = "SELECT_PIECE"


def white_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    ### BRAK EN PASSANT
    
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    pawn_color = TURN+"_pawn"
    
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"
        
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), pawn_color):
        if (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]:
            #bicie
            if piece_x_coord - field_x_coord == 1 and df.at[field_x_coord, field_y_coord] != "0" and piece_y_coord - field_y_coord == 1 or piece_y_coord - field_y_coord == -1:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"

                #promotion (working, visual not so much tho)
                #if field_x_coord == 0 and df.at[field_x_coord, field_y_coord] == pieces_class.Pieces().white_pawn:
                    #df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_queen
                    #pieces.promoted_white.append((field_y_coord * 105, field_x_coord * 105))
                    #for i in range(2):
                        #for j in range(8):
                            #if (piece_y_coord * 105, piece_x_coord * 105) == pieces.white[i][j]:
                                #pieces.white[i][j] = (1000, 1000)
                MOVE="SELECT_PIECE"
                TURN="black"
            #ruch o 2 pola
            elif piece_y_coord == field_y_coord and piece_x_coord == 6 and field_x_coord == 4:
                if df.at[piece_x_coord - 1, piece_y_coord] == "0":
                    df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                    df.at[piece_x_coord, piece_y_coord] = "0"                 
                    MOVE="SELECT_PIECE"
                    TURN="black"

            #ruch o 1 pole
            elif piece_y_coord == field_y_coord and piece_x_coord - field_x_coord == 1:
                if(df.at[field_x_coord, field_y_coord]) == "0":
                    df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                    df.at[piece_x_coord, piece_y_coord] = "0"
                    
                    #promotion (working, visual not so much tho)
                    #if field_x_coord == 0 and df.at[field_x_coord, field_y_coord] == pieces_class.Pieces().white_pawn:
                        #df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_queen
                        #pieces.promoted_white.append((field_y_coord * 105, field_x_coord * 105))
                        #print(pieces.promoted_white)
                        #for i in range(2):
                            #for j in range(8):
                                #if (piece_y_coord * 105, piece_x_coord * 105) == pieces.white[i][j]:
                                    #pieces.white[i][j] = (1000, 1000)
                    MOVE="SELECT_PIECE"
                    TURN="black"
                else:
                    MOVE="SELECT_PIECE"
        else:
            MOVE="SELECT_PIECE"
            
        if TURN == next_turn:
            chess_notation(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
            

def black_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    ### BRAK EN PASSANT
    
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    pawn_color = TURN+"_pawn"
    
    if TURN == "black":
        next_turn = "white"
    elif TURN == "white":
        next_turn = "black"
    
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), pawn_color):
        if (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]:
            #bicie
            if piece_x_coord - field_x_coord == -1 and df.at[field_x_coord, field_y_coord] != "0" and piece_y_coord - field_y_coord == 1 or piece_y_coord - field_y_coord == -1:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN=next_turn
                
            #ruch o 2 pola
            elif piece_y_coord == field_y_coord and piece_x_coord == 1 and field_x_coord == 3:
                if df.at[piece_x_coord + 1, piece_y_coord] == "0":
                    df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                    df.at[piece_x_coord, piece_y_coord] = "0"
                    MOVE="SELECT_PIECE"
                    TURN=next_turn
                
            #ruch o 1 pole
            elif piece_y_coord == field_y_coord and piece_x_coord - field_x_coord == -1:
                if(df.at[field_x_coord, field_y_coord]) == "0":
                    df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                    df.at[piece_x_coord, piece_y_coord] = "0"
                    MOVE="SELECT_PIECE"
                    TURN=next_turn
                else:
                    MOVE="SELECT_PIECE"
        else:
            MOVE="SELECT_PIECE"
        
        if TURN == next_turn:
            chess_notation(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)


def knight_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    knight_color = TURN+"_knight"
    
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"
    
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), knight_color):
        if (TURN == "white" and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]) or (
            TURN == "black" and  (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]):
            #ruchy do przodu 2y+1x
            if piece_x_coord - 2 == field_x_coord and piece_y_coord - 1 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
            elif piece_x_coord - 2 == field_x_coord and piece_y_coord + 1 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
            #ruchy do tyłu -2y-1x
            elif piece_x_coord + 2 == field_x_coord and piece_y_coord + 1 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
            elif piece_x_coord + 2 == field_x_coord and piece_y_coord - 1 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
                
            #ruchy do przodu 1y+1x
            elif piece_x_coord + 1 == field_x_coord and piece_y_coord + 2 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
            elif piece_x_coord + 1 == field_x_coord and piece_y_coord - 2 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn

                #ruchy do tyłu -1y-1x
            elif piece_x_coord - 1 == field_x_coord and piece_y_coord - 2 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
    
            elif piece_x_coord - 1 == field_x_coord and piece_y_coord + 2 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
    
    else:
        MOVE="SELECT_PIECE"
        
    if TURN == next_turn:
        chess_notation(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord, "N")

def rook_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    rook_color = TURN+"_rook"
    
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"

    taking_x_plus = None
    taking_x_minus = None
    taking_y_plus = None
    taking_y_minus = None
    
    for i in range(4):
        if i == 0:
            for j in range(1, 8):
                if 0 <= piece_x_coord + j <= 7 and df.at[piece_x_coord + j, piece_y_coord] == "0":
                    df.at[piece_x_coord + j, piece_y_coord] = "1"
                    taking_x_plus = [piece_y_coord, piece_x_coord + j]
                elif 0 <= piece_x_coord + j <= 7 and df.at[piece_x_coord + j, piece_y_coord] != "0":
                    taking_x_plus = [piece_y_coord, piece_x_coord + j]
                    break
                else:
                    break
        elif i == 1:
            for j in range(1, 8):
                if 0 <= piece_x_coord - j <= 7 and df.at[piece_x_coord - j, piece_y_coord] == "0":
                    df.at[piece_x_coord - j, piece_y_coord] = "1"
                    taking_x_minus = [piece_y_coord, piece_x_coord - j]
                elif 0 <= piece_x_coord - j <= 7 and df.at[piece_x_coord - j, piece_y_coord] != "0":
                    taking_x_minus = [piece_y_coord, piece_x_coord - j]
                    break
                else:
                    break
        elif i == 2:
            for j in range(1, 8):
                if 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord, piece_y_coord + j] == "0":
                    df.at[piece_x_coord, piece_y_coord + j] = "1"
                    taking_y_plus = [piece_y_coord + j, piece_x_coord]
                elif 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord, piece_y_coord + j] != "0":
                    taking_y_plus = [piece_y_coord + j, piece_x_coord]
                    break
                else:
                    break
        elif i == 3:
            for j in range(1, 8):
                if 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord, piece_y_coord - j] == "0":
                    df.at[piece_x_coord, piece_y_coord - j] = "1"
                    taking_y_minus = [piece_y_coord - j, piece_x_coord]
                elif 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord, piece_y_coord - j] != "0":
                    taking_y_minus = [piece_y_coord - j, piece_x_coord]
                    break
                else:
                    break
                
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), rook_color):
        if (TURN == "white" and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]) or (
            TURN == "black" and  (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]):  
            if df.at[field_x_coord, field_y_coord] == "1" or [field_y_coord, field_x_coord] == taking_x_plus or [field_y_coord, field_x_coord] == taking_x_minus or [field_y_coord, field_x_coord] == taking_y_plus or [field_y_coord, field_x_coord] == taking_y_minus:  
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
                            
    for i in range(8):
        for j in range(8):
            if df.at[i, j] == "1":
                df.at[i, j] = "0"
                
    if TURN == next_turn:
            chess_notation(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord, "R")
        
def bishop_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    bishop_color = TURN+"_bishop"
    
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"

    taking_x_plus = None
    taking_x_minus = None
    taking_y_plus = None
    taking_y_minus = None
    
    for i in range(4):
        if i == 0:
            for j in range(1, 8):
                if 0 <= piece_x_coord + j <= 7 and 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord + j, piece_y_coord + j] == "0":
                    df.at[piece_x_coord + j, piece_y_coord + j] = "1"
                    taking_x_plus = [piece_y_coord + j, piece_x_coord + j]
                elif 0 <= piece_x_coord + j <= 7 and 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord + j, piece_y_coord + j] != "0":
                    taking_x_plus = [piece_y_coord + j, piece_x_coord + j]
                    break
                else:
                    break
        elif i == 1:
            for j in range(1, 8):
                if 0 <= piece_x_coord + j <= 7 and 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord + j, piece_y_coord - j] == "0":
                    df.at[piece_x_coord + j, piece_y_coord - j] = "1"
                    taking_x_minus = [piece_y_coord - j, piece_x_coord + j]
                elif 0 <= piece_x_coord + j <= 7 and 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord + j, piece_y_coord - j] != "0":
                    taking_x_minus = [piece_y_coord - j, piece_x_coord + j]
                    break
                else:
                    break
        elif i == 2:
            for j in range(1, 8):
                if 0 <= piece_x_coord - j <= 7 and 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord - j, piece_y_coord + j] == "0":
                    df.at[piece_x_coord - j, piece_y_coord + j] = "1"
                    taking_y_plus = [piece_y_coord + j, piece_x_coord - j]
                elif 0 <= piece_x_coord - j <= 7 and 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord - j, piece_y_coord + j] != "0":
                    taking_y_plus = [piece_y_coord + j, piece_x_coord - j]
                    break
                else:
                    break
        elif i == 3:
            for j in range(1, 8):
                if 0 <= piece_x_coord - j <= 7 and 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord - j, piece_y_coord - j] == "0":
                    df.at[piece_x_coord - j, piece_y_coord - j] = "1"
                    taking_y_minus = [piece_y_coord - j, piece_x_coord - j]
                elif 0 <= piece_x_coord - j <= 7 and 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord - j, piece_y_coord - j] != "0":
                    taking_y_minus = [piece_y_coord - j, piece_x_coord - j]
                    break
                else:
                    break
    
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), bishop_color):
        if (TURN == "white" and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]) or (
            TURN == "black" and  (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]):  
            if df.at[field_x_coord, field_y_coord] == "1" or [field_y_coord, field_x_coord] == taking_x_plus or [field_y_coord, field_x_coord] == taking_x_minus or [field_y_coord, field_x_coord] == taking_y_plus or [field_y_coord, field_x_coord] == taking_y_minus:  
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
                            
    for i in range(8):
        for j in range(8):
            if df.at[i, j] == "1":
                df.at[i, j] = "0"
                
    if TURN == next_turn:
        chess_notation(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord, "B")
                
def queen_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    queen_color = TURN+"_queen"
    
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"

    taking_x_plus_stright = None
    taking_x_minus_stright = None
    taking_y_plus_stright = None
    taking_y_minus_stright = None
    
    taking_x_plus_diagonally = None
    taking_x_minus_diagonally = None
    taking_y_plus_diagonally = None
    taking_y_minus_diagonally = None
    
    for i in range(4):
        if i == 0:
            for j in range(1, 8):
                if 0 <= piece_x_coord + j <= 7 and df.at[piece_x_coord + j, piece_y_coord] == "0":
                    df.at[piece_x_coord + j, piece_y_coord] = "1"
                    taking_x_plus_stright = [piece_y_coord, piece_x_coord + j]
                elif 0 <= piece_x_coord + j <= 7 and df.at[piece_x_coord + j, piece_y_coord] != "0":
                    taking_x_plus_stright = [piece_y_coord, piece_x_coord + j]
                    break
                else:
                    break
        elif i == 1:
            for j in range(1, 8):
                if 0 <= piece_x_coord - j <= 7 and df.at[piece_x_coord - j, piece_y_coord] == "0":
                    df.at[piece_x_coord - j, piece_y_coord] = "1"
                    taking_x_minus_stright = [piece_y_coord, piece_x_coord - j]
                elif 0 <= piece_x_coord - j <= 7 and df.at[piece_x_coord - j, piece_y_coord] != "0":
                    taking_x_minus_stright = [piece_y_coord, piece_x_coord - j]
                    break
                else:
                    break
        elif i == 2:
            for j in range(1, 8):
                if 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord, piece_y_coord + j] == "0":
                    df.at[piece_x_coord, piece_y_coord + j] = "1"
                    taking_y_plus_stright = [piece_y_coord + j, piece_x_coord]
                elif 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord, piece_y_coord + j] != "0":
                    taking_y_plus_stright = [piece_y_coord + j, piece_x_coord]
                    break
                else:
                    break
        elif i == 3:
            for j in range(1, 8):
                if 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord, piece_y_coord - j] == "0":
                    df.at[piece_x_coord, piece_y_coord - j] = "1"
                    taking_y_minus_stright = [piece_y_coord - j, piece_x_coord]
                elif 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord, piece_y_coord - j] != "0":
                    taking_y_minus_stright = [piece_y_coord - j, piece_x_coord]
                    break
                else:
                    break
    
    
    for i in range(4):
        if i == 0:
            for j in range(1, 8):
                if 0 <= piece_x_coord + j <= 7 and 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord + j, piece_y_coord + j] == "0":
                    df.at[piece_x_coord + j, piece_y_coord + j] = "1"
                    taking_x_plus_diagonally = [piece_y_coord + j, piece_x_coord + j]
                elif 0 <= piece_x_coord + j <= 7 and 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord + j, piece_y_coord + j] != "0":
                    taking_x_plus_diagonally = [piece_y_coord + j, piece_x_coord + j]
                    break
                else:
                    break
        elif i == 1:
            for j in range(1, 8):
                if 0 <= piece_x_coord + j <= 7 and 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord + j, piece_y_coord - j] == "0":
                    df.at[piece_x_coord + j, piece_y_coord - j] = "1"
                    taking_x_minus_diagonally = [piece_y_coord - j, piece_x_coord + j]
                elif 0 <= piece_x_coord + j <= 7 and 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord + j, piece_y_coord - j] != "0":
                    taking_x_minus_diagonally = [piece_y_coord - j, piece_x_coord + j]
                    break
                else:
                    break
        elif i == 2:
            for j in range(1, 8):
                if 0 <= piece_x_coord - j <= 7 and 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord - j, piece_y_coord + j] == "0":
                    df.at[piece_x_coord - j, piece_y_coord + j] = "1"
                    taking_y_plus_diagonally = [piece_y_coord + j, piece_x_coord - j]
                elif 0 <= piece_x_coord - j <= 7 and 0 <= piece_y_coord + j <= 7 and df.at[piece_x_coord - j, piece_y_coord + j] != "0":
                    taking_y_plus_diagonally = [piece_y_coord + j, piece_x_coord - j]
                    break
                else:
                    break
        elif i == 3:
            for j in range(1, 8):
                if 0 <= piece_x_coord - j <= 7 and 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord - j, piece_y_coord - j] == "0":
                    df.at[piece_x_coord - j, piece_y_coord - j] = "1"
                    taking_y_minus_diagonally = [piece_y_coord - j, piece_x_coord - j]
                elif 0 <= piece_x_coord - j <= 7 and 0 <= piece_y_coord - j <= 7 and df.at[piece_x_coord - j, piece_y_coord - j] != "0":
                    taking_y_minus_diagonally = [piece_y_coord - j, piece_x_coord - j]
                    break
                else:
                    break

    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), queen_color):
        if (TURN == "white" and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]) or (
            TURN == "black" and  (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]):  
            if df.at[field_x_coord, field_y_coord] == "1":  
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
            elif [field_y_coord, field_x_coord] == taking_x_plus_stright or [field_y_coord, field_x_coord] == taking_x_minus_stright or [field_y_coord, field_x_coord] == taking_y_plus_stright or [field_y_coord, field_x_coord] == taking_y_minus_stright:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
            elif [field_y_coord, field_x_coord] == taking_x_plus_diagonally or [field_y_coord, field_x_coord] == taking_x_minus_diagonally or [field_y_coord, field_x_coord] == taking_y_plus_diagonally or [field_y_coord, field_x_coord] == taking_y_minus_diagonally:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
                    
    for i in range(8):
        for j in range(8):
            if df.at[i, j] == "1":
                df.at[i, j] = "0"  
                
    if TURN == next_turn:
        chess_notation(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord, "Q")              

def winner_check(white, black):
    running = True
    
    if white[1][4] == (1000, 1000):
        print("Black Wins!")
        running = False
    elif black[1][4] == (1000, 1000):
        print("White Wins!")
        running = False
        
    return running

def king_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    king_color = TURN+"_king"
    rook_color = TURN+"_rook"
    CASTLE = False
    
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"

    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), king_color):
        if (TURN == "white" and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]) or (
            TURN == "black" and  (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]):
            if (piece_x_coord - field_x_coord == 1 or piece_x_coord - field_x_coord == -1 or piece_y_coord - field_y_coord == 1 or piece_y_coord - field_y_coord == -1) and (-1 <= piece_x_coord - field_x_coord <= 1 and -1 <= piece_y_coord - field_y_coord <= 1):
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                MOVE="SELECT_PIECE"
                TURN = next_turn
                
            #short castle
            elif field_x_coord == piece_x_coord and field_y_coord == 6 and df.at[piece_x_coord,5] == "0" and df.at[piece_x_coord,6] == "0" and df.at[piece_x_coord,7] == getattr(pieces_class.Pieces(), rook_color):
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                df.at[piece_x_coord,5] = df.at[piece_x_coord,7]
                df.at[piece_x_coord,7] = "0"
                if king_color == "white_king":
                    pieces.white[1][7] = (525, 735)
                if king_color == "black_king":
                    pieces.black[1][7] = (525, 0)
                MOVE="SELECT_PIECE"
                TURN = next_turn
                CASTLE = True
                notation_list.append("O-O")
                print(notation_list)
                
                
            #long castle
            elif field_x_coord == piece_x_coord and field_y_coord == 2 and df.at[piece_x_coord,3] == "0" and df.at[piece_x_coord,2] == "0" and df.at[piece_x_coord,1] == "0" and df.at[piece_x_coord,0] == getattr(pieces_class.Pieces(), rook_color):
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                df.at[piece_x_coord,3] = df.at[piece_x_coord,0]
                df.at[piece_x_coord,0] = "0"
                if king_color == "white_king":
                    pieces.white[1][0] = (315, 735)
                if king_color == "black_king":
                    pieces.black[1][0] = (315, 0)
                MOVE="SELECT_PIECE"
                TURN = next_turn
                CASTLE = True
                notation_list.append("O-O-O")
                print(notation_list)

# Ongoing progress (the idea sucks rn)               
def checkmate():
    result = 0
    
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"
    
    for i in range(8):
        for j in range(8):
            if df.at[i, j] != "0":
                if  df.at[i, j] == getattr(pieces_class.Pieces(), TURN + "_pawn"):
                    pass
    return result            
    if TURN == next_turn and CASTLE == False:
        chess_notation(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord, "K")     

df = pandas.DataFrame(pieces_class.Pieces().starting_chess_board_data)

print("Select Piece")
# game loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_day = datetime.datetime.now()
            notation_df = pandas.DataFrame(notation_list)
            notation_df.to_csv(f"chess//chess_game_{str(current_day.strftime('%d.%m.%G_%H;%M'))}.csv", index = False)
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if(MOVE == "SELECT_PIECE"):
                piece_x_coord = event.pos[1] // 105
                piece_y_coord = event.pos[0] // 105
                piece_coords = [piece_x_coord, piece_y_coord]
                print("Select field to move to")
                MOVE = "SELECT_FIELD"
                
            elif(MOVE == "SELECT_FIELD"):
                field_x_coord = event.pos[1] // 105
                field_y_coord = event.pos[0] // 105
                field_coords = [field_x_coord, field_y_coord]
                piece_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
                pieces.pieces_location(df, TURN, piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
                running = winner_check(pieces.white, pieces.black)
                print("Select Piece")
        
    screen.blit(chess_board, (0, 0))
    pieces.pieces_draw(screen)
    pygame.display.update()