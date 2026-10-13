# Run with: python3 test_hw3.py

import pathlib
import subprocess
import sys
import unittest

from problem3 import ArrayStack, SinglyLinkedStack, DoublyLinkedStack, reverse_stack

FOLDER = pathlib.Path(__file__).parent


class HomeworkTests(unittest.TestCase):
    def check_program(self, program, input_file, expected):
        text = (FOLDER / "tests" / input_file).read_text()
        result = subprocess.run(
            [sys.executable, str(FOLDER / program)],
            input=text, capture_output=True, text=True, check=True
        )
        self.assertEqual(result.stdout, expected)
        self.assertEqual(result.stderr, "")

    def test_palindrome_example(self):
        self.check_program("problem1.py", "problem1_basic.txt", "False\nTrue\nTrue\n2\n")

    def test_palindrome_spaces_case(self):
        self.check_program("problem1.py", "problem1_spaces_case.txt", "False\nTrue\nFalse\nTrue\nTrue\n3\n")

    def test_substring_example(self):
        expected = "a\nab\nabc\nabca\nabcab\nb\nbc\nbca\nbcab\nc\nca\ncab\n12\n"
        self.check_program("problem2.py", "problem2_basic.txt", expected)

    def test_substring_repeated(self):
        self.check_program("problem2.py", "problem2_repeated.txt", "a\naa\naaa\naaaa\n4\n")

    def test_substring_single(self):
        self.check_program("problem2.py", "problem2_single.txt", "x\n1\n")

    def test_stack_operations_and_reversal(self):
        for stack_class in [ArrayStack, SinglyLinkedStack, DoublyLinkedStack]:
            with self.subTest(stack=stack_class.__name__):
                stack = stack_class()
                self.assertTrue(stack.is_empty())
                with self.assertRaises(IndexError):
                    stack.pop()
                with self.assertRaises(IndexError):
                    stack.peek()
                reverse_stack(stack)
                self.assertTrue(stack.is_empty())

                stack.push(7)
                reverse_stack(stack)
                self.assertEqual(stack.peek(), 7)
                self.assertEqual(stack.pop(), 7)

                for value in range(1, 11):
                    stack.push(value)
                original_stack = stack
                reverse_stack(stack)
                self.assertIs(stack, original_stack)
                self.assertEqual(stack.values(), list(range(10, 0, -1)))
                self.assertEqual(stack.peek(), 1)

                if isinstance(stack, DoublyLinkedStack):
                    node = stack.top
                    previous = None
                    while node is not None:
                        self.assertIs(node.prev, previous)
                        previous = node
                        node = node.next

                self.assertEqual([stack.pop() for i in range(10)], list(range(1, 11)))
                self.assertTrue(stack.is_empty())

    def test_stack_output(self):
        result = subprocess.run(
            [sys.executable, str(FOLDER / "problem3.py")],
            capture_output=True, text=True, check=True
        )
        before = "Before: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n"
        after = "After: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1\n"
        self.assertEqual(result.stdout, (before + after) * 3)

    def test_ghostbusters(self):
        cases = [
            ("problem4_crossing.txt", False),
            ("problem4_parallel.txt", True),
            ("problem4_same_line.txt", False),
            ("problem4_vertical.txt", True),
            ("problem4_single.txt", True),
            ("problem4_horizontal.txt", True),
            ("problem4_vertical_same_line.txt", False),
            ("problem4_later_same_line.txt", False),
            ("problem4_crossing_outside_segments.txt", False)
        ]
        for filename, eliminated in cases:
            with self.subTest(input=filename):
                expected = "All Ghosts: were eliminated\n" if eliminated else "All Ghosts: were not eliminated\n"
                self.check_program("problem4.py", filename, expected)


if __name__ == "__main__":
    unittest.main()
