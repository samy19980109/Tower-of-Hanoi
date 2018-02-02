"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
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


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply mov from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin, dest)


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.game = TOAHModel(number_of_stools)
        self.game.fill_first_stool(number_of_cheeses)

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        dest = str(self.game.number_of_stools - 1)
        dest1 = str(self.game.number_of_stools)
        print("Enter your move by first entering the origin and then the "
              "destination")
        print("The stools are called 0 - " + dest + ", please enter from 0 to "
              + dest + " instead of 1 to " + dest1)
        print("To exit, type END when prompted for an input")

        print(self.game)

        # o represents Origin and d represents Destination
        # just saying! people are smart enough to figure it out on their own
        # though

        o, d = "", ""

        while o != "END" or d != "END":
            try:
                print("Enter move " + str(self.game.number_of_moves() + 1))
                o = input("Origin:")
                while o == "":
                    print(self.game)
                    print("Please enter the origin stool.")
                    o = input("Origin:")
                if o == "END":
                    break
                d = input("Destination:")
                while d == "":
                    print(self.game)
                    print("Please enter the destination stool.")
                    d = input("Destination:")
                if d == "END":
                    break
                o, d = int(o), int(d)
                move(self.game, o, d)
                print(self.game)
            except IllegalMoveError:
                print("Illegal move!")
                print(self.game)
            except IndexError:
                print("Illegal move!")
                print(self.game)


if __name__ == '__main__':

    a = ConsoleController(5, 4)
    a.play_loop()

    # Leave lines below as they are, so you will know what python_ta checks.
    # You will need consolecontroller_pyta.txt in the same folder.
    import python_ta
    python_ta.check_all(config="consolecontroller_pyta.txt")
