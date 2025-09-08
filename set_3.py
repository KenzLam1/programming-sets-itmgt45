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
    current_stop = first_stop

    # avoid infinite loop
    steps_taken = 0
    max_steps = len(route_map) + 5

    while current_stop != second_stop and steps_taken < max_steps:
        found_next = False

        # Look for a route that starts from the current_stop
        for start, end in route_map:
            if start == current_stop:
                minutes = route_map[(start, end)]["travel_time_mins"]
                time += minutes
                current_stop = end
                found_next = True
                break

        if not found_next:
            # stop adding time if no route found
            break

        steps_taken += 1

    return time