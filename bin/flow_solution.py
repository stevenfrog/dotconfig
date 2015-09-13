#!/usr/bin/env python3
"""
This class used to solve the 'Flow Free' question.

┏━━━━━┓
┃A B D┃
┃  C E┃
┃     ┃
┃ B D ┃
┃ ACE ┃
┗━━━━━┛
>>>>>>>
┏━━━━━┓
┃A┌B┌D┃
┃││C│E┃
┃│││││┃
┃│B│D│┃
┃└ACE┘┃
┗━━━━━┛

======================

┏━━━━━━━┓
┃A    B▒┃
┃B  C   ┃
┃   D D ┃
┃ ┼   ▒ ┃
┃ ┼ C   ┃
┃    E  ┃
┃E     A┃
┗━━━━━━━┛
>>>>>>>
┏━━━━━━━┓
┃A┐┌──B▒┃
┃B││C──┐┃
┃│││D┌D│┃
┃└┼┘└┘▒│┃
┃┌┼┐C─┐│┃
┃││└─E└┘┃
┃E└────A┃
┗━━━━━━━┛

Version: 0.4
Author: stevenfrog
Date: 2015-07-28
"""


import copy
import time
import math

# TABLE_LINE_1='┌ └ ┐ ┘ ─ │ ├ ┤ ┬ ┴ ┼'
# TABLE_LINE_2='┏ ┗ ┓ ┛ ━ ┃ ┣ ┫ ┳ ┻ ╋'
# TABLE_LINE_3='╔ ╚ ╗ ╝ ═ ║ ╠ ╣ ╦ ╩ ╬'
# ARROWS_1 = '← ↑ → ↓ ↰ ↱ ↲ ↳'
# ARROWS_2 = '⇐ ⇑ ⇒ ⇓ ※ ▒'


TABLE_LINE_THIN = ['│', '─', '┌', '┐', '└', '┘', '├', '┤', '┬', '┴', '┼']
TABLE_LINE_THICK = ['┃', '━', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋']
TABLE_LINE_DOUBLE = ['║', '═', '╔', '╗', '╚', '╝', '╠', '╣', '╦', '╩', '╬']

BLOCK = '▒'
BRIDGE = '┼'

COLOR_CONSOLE = '\033[0m'
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_PURPLE = '\033[35m'
COLOR_CYAN = '\033[36m'
COLOR_WHITE = '\033[37m'

COLOR_BG_RED = '\033[41m'
COLOR_BG_GREEN = '\033[42m'
COLOR_BG_YELLOW = '\033[43m'
COLOR_BG_BLUE = '\033[44m'
COLOR_BG_PURPLE = '\033[45m'
COLOR_BG_CYAN = '\033[46m'
COLOR_BG_WHITE = '\033[30;47m'


COLORS = [COLOR_CONSOLE, COLOR_RED, COLOR_GREEN, COLOR_YELLOW, COLOR_BLUE, COLOR_PURPLE, COLOR_CYAN, COLOR_WHITE,
          COLOR_BG_RED, COLOR_BG_GREEN, COLOR_BG_YELLOW, COLOR_BG_BLUE, COLOR_BG_PURPLE, COLOR_BG_CYAN, COLOR_BG_WHITE]

ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

# Only fisrt result?
ONLY_FIRST_RESULT = True

# The searching order
# 0 -> center, 1 -> up, 2 -> down, 3 -> left, 4 -> right
MOVE_WAYS = [2, 4, 1, 3]


'''
┏━━━┓
┃   ┃
┃ A ┃
┃  A┃
┗━━━┛
'''
#QUESTION = {
#    'Size': (3, 3),
#    'Fixed': {
#        'A': [(1, 1), (2, 2)]
#    }
#}

'''
┏━━━━┓
┃  BC┃
┃ A  ┃
┃ ABC┃
┗━━━━┛
'''
#QUESTION = {
#    'Size': (4, 3),
#    'Fixed': {
#        'A': [(1, 1), (1, 2)],
#        'B': [(2, 0), (2, 2)],
#        'C': [(3, 0), (3, 2)]
#    }
#}

'''
┏━━━━━┓
┃A B D┃
┃  C E┃
┃     ┃
┃ B D ┃
┃ ACE ┃
┗━━━━━┛
'''
#QUESTION = {
#    'Size': (5, 5),
#    'Fixed': {
#        'A': [(0, 0), (1, 4)],
#        'B': [(2, 0), (1, 3)],
#        'C': [(2, 1), (2, 4)],
#        'D': [(4, 0), (3, 3)],
#        'E': [(4, 1), (3, 4)]
#    }
#}

'''
┏━━━━━┓
┃A    ┃
┃     ┃
┃  A  ┃
┃     ┃
┃     ┃
┗━━━━━┛
'''
#QUESTION = {
#    'Size': (5, 5),
#    'Fixed': {
#        'A': [(0, 0), (2, 2)]
#    }
#}

'''
┏━━━━┓
┃A  ▒┃
┃    ┃
┃    ┃
┃   A┃
┗━━━━┛
'''
#QUESTION = {
#    'Size': (4, 4),
#    'Fixed': {
#        'A': [(0, 0), (3, 3)],
#        'X': [(3, 0)]
#    }
#}

'''
┏━━━━━━━┓
┃    B A┃
┃ A    C┃
┃       ┃
┃  DE  E┃
┃   F  F┃
┃ CDG   ┃
┃     BG┃
┗━━━━━━━┛
'''
#QUESTION = {
#    'Size': (7, 7),
#    'Fixed': {
#        'A': [(6, 0), (1, 1)],
#        'B': [(4, 0), (5, 6)],
#        'C': [(6, 1), (1, 5)],
#        'D': [(2, 3), (2, 5)],
#        'E': [(3, 3), (6, 3)],
#        'F': [(3, 4), (6, 4)],
#        'G': [(6, 6), (3, 5)]
#    }
#}

'''
┏━━━━━┓
┃A▒   ┃
┃ ▒ ▒ ┃
┃ ▒ ▒ ┃
┃ ▒ ▒ ┃
┃   ▒A┃
┗━━━━━┛
'''
#QUESTION = {
#    'Size': (5, 5),
#    'Block': [(1, 0), (1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (3, 3), (3, 4)],
#    'Fixed': {
#        'A': [(0, 0), (4, 4)]
#    }
#}


'''
┏━━━━━━━━┓
┃A     GA┃
┃    B   ┃
┃    E   ┃
┃  D F   ┃
┃B   C   ┃
┃C D     ┃
┃  EF  G ┃
┃        ┃
┗━━━━━━━━┛
'''
#QUESTION = {
#    'Size': (8, 8),
#    'Fixed': {
#        'A': [(0, 0), (7, 0)],
#        'B': [(0, 4), (4, 1)],
#        'C': [(0, 5), (4, 4)],
#        'D': [(2, 3), (2, 5)],
#        'E': [(2, 6), (4, 2)],
#        'F': [(3, 6), (4, 3)],
#        'G': [(6, 0), (6, 6)]
#    }
#}

'''
┏━━━━━━━━┓
┃E     GE┃
┃    F   ┃
┃    D   ┃
┃  A B   ┃
┃F   C   ┃
┃C A     ┃
┃  DB  G ┃
┃        ┃
┗━━━━━━━━┛
'''
#QUESTION = {
#    'Size': (8, 8),
#    'Fixed': {
#        'E': [(0, 0), (7, 0)],
#        'F': [(0, 4), (4, 1)],
#        'C': [(0, 5), (4, 4)],
#        'A': [(2, 3), (2, 5)],
#        'D': [(2, 6), (4, 2)],
#        'B': [(3, 6), (4, 3)],
#        'G': [(6, 0), (6, 6)]
#    }
#}

'''
┏━━━━━━━┓
┃ BE    ┃
┃     A ┃
┃  C    ┃
┃       ┃
┃ B   A ┃
┃D  C D ┃
┃E      ┃
┗━━━━━━━┛
'''
#QUESTION = {
#    'Size': (7, 7),
#    'Fixed': {
#        'A': [(5, 1), (5, 4)],
#        'B': [(1, 0), (1, 4)],
#        'C': [(2, 2), (3, 5)],
#        'D': [(0, 5), (5, 5)],
#        'E': [(2, 0), (0, 6)]
#    }
#}

'''
┏━━━━━━━┓
┃ DA    ┃
┃     E ┃
┃  C    ┃
┃       ┃
┃ D   E ┃
┃B  C B ┃
┃A      ┃
┗━━━━━━━┛
'''
#QUESTION = {
#    'Size': (7, 7),
#    'Fixed': {
#        'E': [(5, 1), (5, 4)],
#        'D': [(1, 0), (1, 4)],
#        'C': [(2, 2), (3, 5)],
#        'B': [(0, 5), (5, 5)],
#        'A': [(2, 0), (0, 6)]
#    }
#}

'''
┏━━━━━┓
┃AB CD┃
┃  ┼  ┃
┃  B  ┃
┃ CD E┃
┃AE   ┃
┗━━━━━┛
'''
#QUESTION = {
#    'Size': (5, 5),
#    'Bridge': [(2, 1)],
#    'Fixed': {
#        'A': [(0, 0), (0, 4)],
#        'B': [(1, 0), (2, 2)],
#        'C': [(3, 0), (1, 3)],
#        'D': [(4, 0), (2, 3)],
#        'E': [(1, 4), (4, 3)]
#    }
#}

'''
┏━━━━━┓
┃A   C┃
┃B┼┼  ┃
┃A  ▒B┃
┃D    ┃
┃▒  DC┃
┗━━━━━┛
'''
#QUESTION = {
#    'Size': (5, 5),
#    'Block': [(3, 2), (0, 4)],
#    'Bridge': [(1, 1), (2, 1)],
#    'Fixed': {
#        'A': [(0, 0), (0, 2)],
#        'B': [(0, 1), (4, 2)],
#        'C': [(4, 0), (4, 4)],
#        'D': [(3, 4), (0, 3)]
#    }
#}

'''
┏━━━━━┓
┃AB CD┃
┃  ┼  ┃
┃  B  ┃
┃ CD E┃
┃A▒▒▒▒┃
┗━━━━━┛
'''
#QUESTION = {
#    'Size': (5, 5),
#    'Block': [(4, 3), (1, 4), (2, 4), (3, 4), (4, 4)],
#    'Bridge': [(2, 1)],
#    'Fixed': {
#        'A': [(0, 0), (0, 4)],
#        'B': [(1, 0), (2, 2)],
#        'C': [(3, 0), (1, 3)],
#        'D': [(4, 0), (2, 3)]
#    }
#}

'''
┏━━━━━━━┓
┃A    B▒┃
┃B  C   ┃
┃   D D ┃
┃ ┼   ▒ ┃
┃ ┼ C   ┃
┃    E  ┃
┃E     A┃
┗━━━━━━━┛
'''
#QUESTION = {
#    'Size': (7, 7),
#    'Block': [(6, 0), (5, 3)],
#    'Bridge': [(1, 3), (1, 4)],
#    'Fixed': {
#        'A': [(0, 0), (6, 6)],
#        'B': [(0, 1), (5, 0)],
#        'C': [(3, 1), (3, 4)],
#        'D': [(3, 2), (5, 2)],
#        'E': [(0, 6), (4, 5)]
#    }
#}


'''
I was blocked here so much time
┏━━━━━━━┓
┃A     B┃
┃    A  ┃
┃ B     ┃
┃  ┼    ┃
┃   D C ┃
┃       ┃
┃C     D┃
┗━━━━━━━┛
'''
#QUESTION = {
#    'Size': (7, 7),
#    'Bridge': [(2, 3)],
#    'Fixed': {
#        'A': [(0, 0), (4, 1)],
#        'B': [(6, 0), (1, 2)],
#        'C': [(5, 4), (0, 6)],
#        'D': [(3, 4), (6, 6)]
#    }
#}


'''
I was block here a little
┏━━━━━━━┓
┃▒A B   ┃
┃     B ┃
┃   D C ┃
┃       ┃
┃  A C  ┃
┃D      ┃
┃▒      ┃
┗━━━━━━━┛
'''
#QUESTION = {
#    'Size': (7, 7),
#    'Block': [(0, 0), (0, 6)],
#    'Fixed': {
#        'A': [(1, 0), (2, 4)],
#        'B': [(3, 0), (5, 1)],
#        'C': [(5, 2), (4, 4)],
#        'D': [(3, 2), (0, 5)]
#    }
#}

'''
┏━━━━━━━┓
┃▒A B   ┃
┃     B ┃
┃   D C ┃
┃       ┃
┃  A C  ┃
┃D      ┃
┃▒      ┃
┗━━━━━━━┛
'''
#QUESTION = {
#    'Size': (9, 9),
#    'Bridge': [(3, 4)],
#    'Fixed': {
#        'A': [(4, 0), (5, 8)],
#        'B': [(2, 1), (1, 2)],
#        'C': [(3, 1), (1, 3)],
#        'D': [(3, 3), (4, 7)],
#        'E': [(5, 5), (1, 7)],
#        'F': [(4, 2), (5, 7)],
#        'G': [(5, 2), (4, 3)],
#        'H': [(4, 5), (3, 6)],
#        'I': [(6, 1), (5, 6)],
#        'J': [(7, 1), (7, 7)]
#    }
#}


'''
┏━━━━━━━┓
┃▒A B   ┃
┃     B ┃
┃   D C ┃
┃       ┃
┃  A C  ┃
┃D      ┃
┃▒      ┃
┗━━━━━━━┛
'''
QUESTION = {
    'Size': (11, 13),
    'Bridge': [(3, 3), (7, 6)],
    'Block':  [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
               (6, 1), (0, 2), (1, 2), (2, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 11), (0, 12),
               (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9)],
    'Fixed': {
        'A': [(0, 10), (5, 8)],
        'B': [(1, 3),  (6, 12)],
        'C': [(8, 1),  (9, 11)],
        'D': [(2, 11), (7, 7)],
        'E': [(6, 7),  (8, 9)]
    }
}

# Create some constants
TABLE_WIDTH = QUESTION['Size'][0]
TABLE_HEIGHT = QUESTION['Size'][1]
HAS_BRIDGE = 'Bridge' in QUESTION

TABLE_FIXED_BLOCK = [([0] * TABLE_WIDTH) for i in range(TABLE_HEIGHT)]
if 'Block' in QUESTION:
    for pos in QUESTION['Block']:
        TABLE_FIXED_BLOCK[pos[1]][pos[0]] = 1
if 'Bridge' in QUESTION:
    for pos in QUESTION['Bridge']:
        TABLE_FIXED_BLOCK[pos[1]][pos[0]] = 2
for ele in QUESTION['Fixed']:
    for pos in QUESTION['Fixed'][ele]:
        TABLE_FIXED_BLOCK[pos[1]][pos[0]] = 1

FIXED_ELES = QUESTION['Fixed']
TABLE_BRIDGE = []
if HAS_BRIDGE:
    TABLE_BRIDGE = QUESTION['Bridge']


def generateFixTable(question_data):
    """
    Generate the start table with elements.
    EX:
    ┏━━━┓
    ┃000┃
    ┃0A0┃
    ┃00A┃
    ┗━━━┛
    """

    tmp_table = [(['0'] * TABLE_WIDTH) for i in range(TABLE_HEIGHT)]
    fixed_data = question_data['Fixed']
    for key in fixed_data:
        start_pos = fixed_data[key][0]
        end_pos = fixed_data[key][1]
        tmp_table[start_pos[1]][start_pos[0]] = key
        tmp_table[end_pos[1]][end_pos[0]] = key

    if 'Block' in question_data:
        for key in question_data['Block']:
            tmp_table[key[1]][key[0]] = BLOCK

    if 'Bridge' in question_data:
        for key in question_data['Bridge']:
            tmp_table[key[1]][key[0]] = BRIDGE

    return tmp_table


def checkCellStatus(solution_data, cell, finish_pos):
    """
    Check cell to move in table.
    If cell is expect position, return 'OK'
    If cell is empty, return True, otherwise return False
    """

    pos_x = cell[0]
    pos_y = cell[1]
    if cell == finish_pos:
        return 'OK'
    elif pos_x < 0 or pos_y < 0 or pos_x >= TABLE_WIDTH or pos_y >= TABLE_HEIGHT:
        return False
    # the cell is in bridge?
    elif TABLE_FIXED_BLOCK[pos_y][pos_x] == 2:
        return True
    elif TABLE_FIXED_BLOCK[pos_y][pos_x] == 1:
        return False

    for ele in solution_data:
        if cell in solution_data[ele]:
            return False

    return True


def checkTableFullStatus(solution_data):
    """
    Check table whether full with elements.
    """

    for i in range(TABLE_WIDTH):
        for j in range(TABLE_HEIGHT):
            cell = (i, j)
            cell_blocked = False
            # if cell in TABLE_FIXED_BLOCK:
            if TABLE_FIXED_BLOCK[j][i] > 0:
                cell_blocked = True

            if not cell_blocked:
                for ele in solution_data:
                    if cell in solution_data[ele]:
                        cell_blocked = True
                        continue

            if not cell_blocked:
                return False

    return True


def copySolution(solution_data):
    """
    Shallow copy solution array.
    Not deep copy, can save time
    """

    tmp_solution = {}
    for key in solution_data:
        tmp_solution[key] = copy.copy(solution_data[key])
    return tmp_solution


recursion_num = 0
found_solution_result = False


def findWayHome(solution_data, current_elem, cell_pos, come_from):

    global recursion_num, found_solution_result
    recursion_num += 1

    if ONLY_FIRST_RESULT and found_solution_result:
        return

    cell_up = (cell_pos[0], cell_pos[1] - 1)
    cell_down = (cell_pos[0], cell_pos[1] + 1)
    cell_left = (cell_pos[0] - 1, cell_pos[1])
    cell_right = (cell_pos[0] + 1, cell_pos[1])

    # If current position is not bridge, check three position whether has
    # bridge, expect from way
    next_bridges = 0
    bridge_direction = 0
    cell_is_bridge = False

    if HAS_BRIDGE:
        cell_is_bridge = cell_pos in TABLE_BRIDGE

        if not cell_is_bridge:
            if come_from != 2 and cell_up in TABLE_BRIDGE:
                next_bridges += 1
                bridge_direction = 1
            elif come_from != 1 and cell_down in TABLE_BRIDGE:
                next_bridges += 1
                bridge_direction = 2
            elif come_from != 4 and cell_left in TABLE_BRIDGE:
                next_bridges += 1
                bridge_direction = 3
            elif come_from != 3 and cell_right in TABLE_BRIDGE:
                next_bridges += 1
                bridge_direction = 4

    for i in MOVE_WAYS:
        if HAS_BRIDGE:
            # Check current cell whether is bridge
            # If current cell is bridge, only one way
            if cell_is_bridge and i != come_from:
                continue

            # If there only one bridge in three ways, expect from way, that's
            # only way
            if next_bridges == 1 and i != bridge_direction:
                continue

        # Normally the start position is in left top, end position is in right bottom
        # So move down, right, left, up is better

        # Ro_move_cell
        if i == 1 and come_from != 2:
            # move up
            to_move_cell = cell_up
        elif i == 2 and come_from != 1:
            # move down
            to_move_cell = cell_down
        elif i == 3 and come_from != 4:
            # move left
            to_move_cell = cell_left
        elif i == 4 and come_from != 3:
            # move right
            to_move_cell = cell_right
        else:
            continue

        move_res = checkCellStatus(
            solution_data, to_move_cell, FIXED_ELES[current_elem][1])

        if move_res == 'OK':
            ele_order_idx = 0
            for ele in running_order:
                if ele == current_elem:
                    break
                ele_order_idx += 1

            # If there is next element to search, go on finding way
            if ele_order_idx + 1 < len(running_order):
                next_ele = running_order[ele_order_idx + 1]
                findWayHome(solution_data, next_ele, FIXED_ELES[next_ele][0], 0)
            # Else check whether table is full, store result
            elif checkTableFullStatus(solution_data):
                solution_result.append(solution_data)
                found_solution_result = True
            # Fisish linking but not fill all table, ignore result

        elif move_res:
            # IMPORTANT! If use deep copy it will cost about 5 times
            tmp_solution = {}
            for key in solution_data:
                tmp_solution[key] = copy.copy(solution_data[key])
            tmp_solution[current_elem].append(to_move_cell)
            findWayHome(tmp_solution, current_elem, to_move_cell, i)
    return


def drawAnswer_table(table_data, ele, start_pos, end_pos, solution_data):
    """
    Transfer moves to lines
    EX:
    {'A': [(1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1)]}

    =>

    [['┌', '─', '┐'], ['│', 'A', '│'], ['└', '┘', 'A']]
    """

    steps = solution_data[ele]
    step_len = len(steps)
    last_step = (0, 0)
    next_step = (0, 0)
    for i in range(step_len):
        current_x = steps[i][0]
        current_y = steps[i][1]
        if(i == 0):
            last_step = start_pos
        else:
            last_step = steps[i - 1]

        if(i == step_len - 1):
            next_step = end_pos
        else:
            next_step = steps[i + 1]

        direction = (
            current_x - last_step[0], current_y - last_step[1], next_step[0] - current_x, next_step[1] - current_y)

        if (direction == (0, 1, 0, 1) or direction == (0, -1, 0, -1)):
            table_data[current_y][current_x] = TABLE_LINE_THIN[0]
        elif (direction == (1, 0, 1, 0) or direction == (-1, 0, -1, 0)):
            table_data[current_y][current_x] = TABLE_LINE_THIN[1]
        elif (direction == (0, -1, 1, 0) or direction == (-1, 0, 0, 1)):
            table_data[current_y][current_x] = TABLE_LINE_THIN[2]
        elif (direction == (1, 0, 0, 1) or direction == (0, -1, -1, 0)):
            table_data[current_y][current_x] = TABLE_LINE_THIN[3]
        elif (direction == (-1, 0, 0, -1) or direction == (0, 1, 1, 0)):
            table_data[current_y][current_x] = TABLE_LINE_THIN[4]
        elif (direction == (0, 1, -1, 0) or direction == (1, 0, 0, -1)):
            table_data[current_y][current_x] = TABLE_LINE_THIN[5]

    return table_data


def cellInElement(pos, solution_data):
    for key in solution_data:
        if pos in solution_data[key]:
            return key
    return


def printTable(table_data, solution_data=None):
    """
    Print table in scrren.
    EX:
    ┏━━━┓
    ┃┌─┐┃
    ┃│A│┃
    ┃└┘A┃
    ┗━━━┛
    """

    left_space = '   '

    print(left_space, end='')
    print(TABLE_LINE_THICK[2], end='')
    for x in range(TABLE_WIDTH):
        print(TABLE_LINE_THICK[1], end='')
    print(TABLE_LINE_THICK[3])

    for y in range(TABLE_HEIGHT):
        print(left_space, end='')
        print(TABLE_LINE_THICK[0], end='')
        for x in range(TABLE_WIDTH):
            element = table_data[y][x]

            if TABLE_BRIDGE and (x, y) in TABLE_BRIDGE:
                print(BRIDGE, end='')
                continue
            elif element == '0':
                print(' ', end='')
                continue

            # print the color
            color_idx = None
            if solution_data and element in TABLE_LINE_THIN:
                tmp = cellInElement((x, y), solution_data)
                if tmp:
                    color_idx = ord(tmp) - 64
            elif element in ELEMENTS:
                color_idx = ord(element) - 64

            if color_idx:
                print(COLORS[color_idx] + element + COLORS[0], end='')
            else:
                print(element, end='')

        print(TABLE_LINE_THICK[0])

    print(left_space, end='')
    print(TABLE_LINE_THICK[4], end='')
    for x in range(TABLE_WIDTH):
        print(TABLE_LINE_THICK[1], end='')
    print(TABLE_LINE_THICK[5])


def printAnswer(answer_data):
    # print answer tables
    print("#######  Answers  #######")
    if ONLY_FIRST_RESULT and len(answer_data['moves']) > 0:
        print("!!!!! First Result !!!!!!")
    print()

    num = 0
    for moves in answer_data['moves']:
        num += 1
        print(str(num) + '.')
        answer_table = copy.deepcopy(fixTable)
        for ele in moves:
            answer_table = drawAnswer_table(
                answer_table, ele, answer_data['Fixed'][ele][0], answer_data['Fixed'][ele][1], moves)

        printTable(answer_table, moves)
        print()


def countDistance(pos1, pos2):
    return math.pow(math.fabs(pos1[0] - pos2[0]), 2) + math.pow(math.fabs(pos1[1] - pos2[1]), 2)


'''
I find run with the longest distance element first is better effective

#######   Table   #######
   ┏━━━━━━━┓
   ┃ DA    ┃
   ┃     E ┃
   ┃  C    ┃
   ┃       ┃
   ┃ D   E ┃
   ┃B  C B ┃
   ┃A      ┃
   ┗━━━━━━━┛

##########################
recursion_num: 290424
Used time: 2.207577 real seconds
#######  Answers  #######

1.
   ┏━━━━━━━┓
   ┃┌DA───┐┃
   ┃│┌──┐E│┃
   ┃││C┐│││┃
   ┃│└┐││││┃
   ┃└D│││E│┃
   ┃B─┘C└B│┃
   ┃A─────┘┃
   ┗━━━━━━━┛
======================================================


#######   Table   #######
   ┏━━━━━━━┓
   ┃ BE    ┃
   ┃     A ┃
   ┃  C    ┃
   ┃       ┃
   ┃ B   A ┃
   ┃D  C D ┃
   ┃E      ┃
   ┗━━━━━━━┛

##########################
recursion_num: 14057653
Used time: 109.406567 real seconds
#######  Answers  #######

1.
   ┏━━━━━━━┓
   ┃┌BE───┐┃
   ┃│┌──┐A│┃
   ┃││C┐│││┃
   ┃│└┐││││┃
   ┃└B│││A│┃
   ┃D─┘C└D│┃
   ┃E─────┘┃
   ┗━━━━━━━┛
'''


# Record start time
start_time = time.time()

fixTable = generateFixTable(QUESTION)

solution = {}
for key in FIXED_ELES:
    solution[key] = []


solution_result = []

# print start Table
print("#######   Table   #######")
printTable(fixTable)
print()


# change the element order
eles_distance = {}
for ele in FIXED_ELES:
    eles_distance[ele] = countDistance(FIXED_ELES[ele][0], FIXED_ELES[ele][1])

sorted_eles = sorted(eles_distance.items(), key=lambda d: d[1], reverse=True)

running_order = []
for item in sorted_eles:
    running_order.append(item[0])

# Starting find ways from first element
findWayHome(solution, running_order[0], FIXED_ELES[running_order[0]][0], 0)

# Create answer
answer = copy.deepcopy(QUESTION)
answer['moves'] = solution_result

print("##########################")
#print(running_order)
print("recursion_num:", recursion_num)
# print(solution_result)
# print("##########################")
end_time = time.time()
print("Used time: %f real seconds" % (end_time - start_time))

printAnswer(answer)


'''
今天还发现了一种算法， 就是贴边。
如果有起点，终点都在最边上， 且没有东西阻挡，就应该尝试先连， 一般都对。
但是如果如要扭一下，绕路，这个算法就会有点问题， 所有线连完后有空。
但是这个方法肯定是个快速解决的办法。

有空的情况再想办法用周围的线弯曲？
好像算法有点复杂了， 如果Table很大，估计能节省些时间。

不过， 应该先测试贴边算法是否先有解， 然后再有解的情况下，再调整弯曲， 这样应该才是最佳
还要考虑桥的问题， 有些直连后会影响有关桥的另一个

如果要进一步提高效率，估计只有用有关图论的东西了。
'''


'''
# This is a test for array searhing and table searching
testPos = (3, 1)
arrayTest = [(1, 2), (3,3), (3,1), (2, 3), (0, 0)]
testTable = [([0] * 4) for i in range(4)]
testTable[1][2] = 1
testTable[3][3] = 1
testTable[3][1] = 1
testTable[2][3] = 1
testTable[0][0] = 1

time1 = time.time()
for i in range(10000000):
    if (3, 1) in arrayTest:
        continue
time2 = time.time()
print("array Used time: %f real seconds" % (time2 - time1))

time1 = time.time()
for i in range(10000000):
    #xp = testPos[0]
    #yp = testPos[1]
    if testTable[3][1] == 1:
        continue
time2 = time.time()
print("table Used time: %f real seconds" % (time2 - time1))

'''
