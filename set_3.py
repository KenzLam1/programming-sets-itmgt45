'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    from_data = set(social_graph.get(from_member, {}).get("following", []))
    to_data = set(social_graph.get(to_member, {}).get("following", []))

    afollows_b = to_member in from_data
    bfollows_a = from_member in to_data

    if afollows_b and bfollows_a:
        return "friends"
    if afollows_b:
        return "follower"
    if bfollows_a:
        return "followed by"
    return "no relationship"


def tic_tac_toe(board):
    # Size of the board (num of rows and columns)
    n = len(board)

    def winner(line):
        first = line[0] # takes note of first cell in the line
        # Cant be winning line if first cell is empty
        if first == "":
            return None
        # Check if all cells in the line are the same as the first cell
        for character in line[1:]:
            if character != first:
                return None
        # Return x or o if all cells are the same
        return first

    # row
    for r in range(n):
        w = winner(board[r])
        if w:
            return w

    # column
    for c in range(n):
        col = [board[r][c] for r in range(n)]
        w = winner(col)
        if w:
            return w

    # diagonal
    main_diag = [board[i][i] for i in range(n)]
    w = winner(main_diag)
    if w:
        return w

    anti_diag = [board[i][n - 1 - i] for i in range(n)]
    w = winner(anti_diag)
    if w:
        return w

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    if first_stop == second_stop:
        return 0

    time = 0
    current = first_stop
    visited = set()  # safety against malformed input

    while current != second_stop:
        if current in visited:
            break  # safety; route is expected to be fully enclosed
        visited.add(current)

        # find unique outgoing leg from current
        next_leg = None
        for (start, end), data in route_map.items():
            if start == current:
                next_leg = (end, data["travel_time_mins"])
                break

        if next_leg is None:
            break  # malformed map (shouldn't happen with valid input)

        nxt, minutes = next_leg
        time += minutes
        current = nxt

    return time