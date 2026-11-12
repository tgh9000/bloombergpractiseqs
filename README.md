# Bloomberg Practice Questions

Code review and debugging exercises based on common Bloomberg interview problems.

These are not "write the solution from scratch" problems. Each exercise is set up like a pull request someone else wrote. You get a spec, an implementation and a test suite, and your job is to review them: find what is wrong in the code **and** in the tests, fix both, and convince yourself the result is correct.

## What is in each exercise

```
NN-problem-name/
├── excercise.txt   # The PR description: what the code must do (the spec)
├── <topic>.py      # The proposed implementation, with unittest tests at the bottom
└── AGENTS.md       # Rules for an AI helper, if you use one
```

- **`excercise.txt`** is the source of truth. It lists every requirement, including edge cases, input limits, required time complexity and whether inputs may be modified. If the code or a test disagrees with it, the spec wins.
- **`<topic>.py`** contains the implementation and its tests in one file. The implementation contains deliberate logic errors.
- **`AGENTS.md`** tells an AI assistant to act as a hint-giver rather than solving the exercise for you (see below).

## What to expect from the tests

The test suites are deliberately imperfect. Every exercise has all three of these:

1. **Wrong tests that pass.** Some tests assert the buggy behaviour instead of what the spec requires. They pass, but they shouldn't.
2. **Correct tests that fail.** Some tests are right and fail because the implementation is wrong.
3. **Missing tests.** At least one requirement in the spec is not tested at all, and the implementation gets it wrong. You need to write the test that catches it.

You may also find weak tests that pass no matter what (for example, only checking a length or a type).

A green test run is therefore **not** proof that you are done. Passing tests only tell you something if the tests themselves are correct and complete.

## How to work through an exercise

1. **Read `excercise.txt` first**, before looking at the code. Note each requirement and edge case.
2. **Run the tests** to see where you are starting from:
   ```
   cd 02-sum-of-mutated-array-closest-to-target
   python mutated_array.py -v
   ```
3. **Review every test against the spec.** For each one, ask whether the expected value is actually correct and whether it checks anything meaningful. Fix or delete wrong tests.
4. **Write tests for the missing requirements.** Go through your list from step 1 and add a test for anything that is not covered.
5. **Fix the implementation** until all of your corrected tests pass.
6. **Explain your result.** Say which tests give you confidence and why, and which bugs you found in the code and in the original tests.

Python 3.8+ is enough. There are no dependencies beyond the standard library.

## Using an AI assistant

Each folder has an `AGENTS.md` that tells the AI to act as a limited debugging helper: give progressive hints, explain tracebacks and concepts, ask diagnostic questions, and **not** write the fix for you.

To get the most out of it:

- Open **only the exercise folder** you are working on in your editor or AI tool, not the whole repo.
- The AI is told it does not know the assignment, so paste in the relevant part of `excercise.txt` when you need it to reason about a requirement.
- `AGENTS.md` contains instructions, not access controls. Check what your AI tool can read on disk.

## Exercises

| # | Exercise | File |
|---|----------|------|
| 01 | Code validator (warm-up) | `validator.py` |
| 02 | Sum of Mutated Array Closest to Target | `mutated_array.py` |
| 03 | Number of Dice Rolls With Target Sum | `dice_rolls.py` |
| 04 | Sort Characters By Frequency | `frequency_sort.py` |
| 05 | Add Two Numbers II | `add_two_numbers_ii.py` |
| 06 | Shuffle an Array | `shuffler.py` |
| 07 | Range Sum Query 2D - Immutable | `num_matrix.py` |
| 08 | Find Minimum in Rotated Sorted Array | `rotated_min.py` |
| 09 | Word Ladder | `word_ladder.py` |
| 10 | Design Browser History | `browser_history.py` |
| 11 | Vertical Order Traversal of a Binary Tree | `vertical_order.py` |
| 12 | Minesweeper | `minesweeper.py` |
| 13 | Number of Islands | `islands.py` |
| 14 | Find Peak Element | `peak_element.py` |
| 15 | Binary Tree Level Order Traversal | `level_order.py` |
| 16 | Unique Paths | `unique_paths.py` |
| 17 | Coin Change | `coin_change.py` |
| 18 | Two City Scheduling | `two_city.py` |
| 19 | Subsets | `subsets.py` |
| 20 | Binary Tree Right Side View | `right_side_view.py` |
| 21 | Insert Delete GetRandom O(1) | `randomized_set.py` |
| 22 | Minimum Remove to Make Valid Parentheses | `valid_parentheses.py` |
| 23 | LRU Cache | `lru.py` |
| 24 | Decode String | `decode_string.py` |
| 25 | Flatten a Multilevel Doubly Linked List | `flatten_list.py` |
| 26 | Word Search | `word_search.py` |
| 27 | Word Break II | `word_break.py` |
| 28 | Longest Substring Without Repeating Characters | `longest_substring.py` |
| 29 | Merge Intervals | `merge_intervals.py` |
| 30 | Add Two Numbers | `add_two_numbers.py` |
| 31 | 3Sum | `three_sum.py` |
| 32 | Validate Binary Search Tree | `validate_bst.py` |
| 33 | Valid Triangle Number | `triangle_number.py` |
| 34 | Invalid Transactions | `transactions.py` |
| 35 | Design Underground System | `underground.py` |
| 36 | Copy List with Random Pointer | `copy_random_list.py` |
| 37 | Remove All Adjacent Duplicates in String II | `remove_duplicates.py` |
| 38 | Reconstruct Itinerary | `itinerary.py` |

## Keeping your work separate

If you want to retry an exercise later, do your fixes on a branch so `main` keeps the original broken version:

```
git checkout -b my-solutions
```

To reset a single exercise back to its original state:

```
git checkout main -- 02-sum-of-mutated-array-closest-to-target
```
