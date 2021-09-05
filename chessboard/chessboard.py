from flask import Flask, render_template

chessboard = Flask(__name__)

@chessboard.route("/")
def create_board():
    dimension = 8
    row = [[(x+1)%2 for x in range(dimension)], [x%2 for x in range(dimension)]]
    board = [row[x%2] for x in range(dimension)]

    value = {'board': board, 'row':row}
    
    return render_template('chess.html', key=value )

if __name__ == "__main__":
    chessboard.run(debug=True)