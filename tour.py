"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'
import time
from toah_model import TOAHModel


def stools4(model, num_of_cheeses, origin, mid, dest):
    """
    A recursive helper function that helps calculate the number of moves that
    it takes to move the cheeses from origin to destination using 4 stools

    @type model: TOAHModel
    @type num_of_cheeses: int
    @type origin: int
    @type mid: tuple
    @type dest: int
    @rtype None
    """

    if num_of_cheeses == 1:
        model.move(origin, dest)
    else:
        optimal = int(((8 * num_of_cheeses + 1) ** (1 / 2) - 1) / 2)
        # http://math.stackexchange.com/questions/1451254/how-to-find-the-
        # optimal-solution-for-reves-puzzle
        # used int method to round to the lowest integer
        stools4(model, num_of_cheeses-optimal, origin, (mid[1], dest), mid[0])
        stools3(model, optimal, origin, dest, mid[1])
        stools4(model, num_of_cheeses-optimal, mid[0], (origin, mid[1]), dest)


def stools3(model, num_of_cheeses, origin, dest, mid):
    """
    A recursive helper function that helps calculate the moves to take number
    of cheese from origin to dest using only 3 stools

    @type model: TOAHModel
    @type num_of_cheeses: int
    @type origin: int
    @type dest: int
    @type mid: int
    @rtype: None
    """
    if num_of_cheeses > 0:
        stools3(model, num_of_cheeses - 1, origin, mid, dest)
        model.move(origin, dest)
        stools3(model, num_of_cheeses - 1, mid, dest, origin)


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """
    stools4(model, model.get_number_of_cheeses(), 0, (1, 2), 3)
    if animate:
        x = model.get_move_seq()
        y = model.get_number_of_cheeses()
        model = TOAHModel(4)
        i = 0
        model.fill_first_stool(y)
        time.sleep(delay_btw_moves)
        print(model)
        while i < x.length():
            time.sleep(delay_btw_moves)
            tuple_ = x.get_move(i)
            model.move(tuple_[0], tuple_[1])
            time.sleep(delay_btw_moves)
            print()
            print(model)
            time.sleep(delay_btw_moves)
            i += 1


if __name__ == '__main__':
    num_cheeses = 5
    delay_between_moves = 0.5
    console_animate = True

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    import python_ta
    python_ta.check_all(config="tour_pyta.txt")
