#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

## This is a class to test the falsiness of __nonzero__()
class FalseClass:
  def __nonzero__(self):
    return False
## This is a class to test the falsiness of __len__()
class EmptyClass:
  def __len__(self):
    return 0
## This is a class to provide a constant of false-y things
class Falseyness:
  FALSE_THINGS = [ 0, 0L, 0.0, 0j, None, False, '', (), [], {}, FalseClass(), EmptyClass() ]

class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        false_things = Falseyness.FALSE_THINGS # [ 0, 0L, 0.0, 0j, None, False, '', (), [], {}, FalseClass(), EmptyClass() ]
        for thing in false_things:
          self.assertFalse(thing)  # These things should be false

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        for thing in Falseyness.FALSE_THINGS:
          self.assertFalse(thing, "This should be false -- Please fix this")

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(__, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against
        reality.
        """
        expected_value = __
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = __
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.
        """

        # This throws an AssertionError exception
        assert False

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "naval". What is it's class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "naval".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        self.assertEqual(__, "naval".__class__) # It's str, not <type 'str'>

        # Need an illustration? More reading can be found here:
        #
        #   http://bit.ly/__class__
