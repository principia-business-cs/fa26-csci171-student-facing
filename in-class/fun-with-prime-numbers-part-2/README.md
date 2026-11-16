# Fun with Prime Numbers — Part 2

## The Challenge

In [Part 1](../fun-with-prime-numbers/README.md), you tested individual numbers to decide whether they were prime. This time, find all the primes up to a limit by keeping track of a whole collection of numbers and crossing out numbers that cannot be prime.

Use the explanation below to develop your own Python implementation. There is no starter code: deciding how to turn the idea into functions, lists, loops, and conditionals is part of the challenge.

## Work From Your Own Thinking

- Write your own code. Do not copy a solution from a website, classmate, textbook, or AI tool, or ask AI to generate one.
- You may use Python documentation and class notes for syntax.
- Discuss the idea and ask the instructor for hints, but be ready to explain every line you write.
- Do not use a library that generates primes, hardcode the answers, or call your Part 1 prime checker on every number.

## The Idea: Cross Out Multiples

A prime number is an integer greater than 1 whose only positive factors are 1 and itself. A composite number has other factors. If you know that 3 is prime, you also know that 6, 9, 12, and every larger multiple of 3 cannot be prime: each has 3 as a factor.

Imagine writing all the integers from 2 through 30 on paper. At first, every number is a possible prime.

**Start with 2.** Keep 2, but cross out its larger multiples: 4, 6, 8, 10, and so on through 30. Do not cross out 2 itself.

**The next number still standing is 3.** Keep 3 and cross out its larger multiples. Some, such as 6 and 12, are already crossed out. That is fine. The newly crossed-out numbers are 9, 15, 21, and 27.

**Skip 4 because it is already crossed out.** It cannot give us a new prime factor; its multiples are also multiples of 2.

**The next number still standing is 5.** Keep 5 and cross out its larger multiples. The only newly crossed-out number is 25.

The numbers still standing are:

**2, 3, 5, 7, 11, 13, 17, 19, 23, 29**

Why can we trust the next number still standing? If it had a smaller prime factor, an earlier round would already have crossed it out. Why does crossing out a larger multiple make sense? That number has a factor other than 1 and itself.

## Try It On Paper

Write the integers from 2 through 50. Use a different color or symbol for each round.

- Which numbers get crossed out for the first time when you use 2? What about 3, 5, and 7?
- Why do you skip 4 and 6?
- Why must the number leading a round stay uncrossed?
- Why would stopping after the round for 5 incorrectly leave 49 standing?

Explain the method to a partner using your marked-up numbers before you code.

## Representing the Paper in Python

Use a list of Boolean values as your record of which numbers are still possible primes. Let a number's position in the list represent that number: position 17 records the status of 17. A true value means “still a possible prime”; a false value means “not prime.”

Think carefully about the length needed to include the limit itself. Positions 0 and 1 must be marked as not prime, since neither is prime.

Crossing out a number means changing its Boolean value. Keep the positions fixed rather than deleting list elements: deleting an element shifts later positions and breaks the connection between a number and its position.

The same composite number may be marked more than once. Marking it again should not change it back into a candidate.

## Your Program

Create `prime_numbers_part2.py` with a function named `primes_up_to(limit)`.

Assume the argument is an integer. Return a list containing every prime less than or equal to the limit, in increasing order. Return an empty list for any limit below 2. Keep printing and input prompts outside the function.

Your implementation must use the Boolean record and cross out multiples as described above. Use your own loops and conditionals. Keep your Part 1 program so you can compare the two approaches.

Begin with a version you understand, even if it visits more numbers than necessary.

## Check Your Work

Predict these results before running your function.

| Limit | Expected return |
| --- | --- |
| -5 | [] |
| 0 | [] |
| 1 | [] |
| 2 | [2] |
| 3 | [2, 3] |
| 4 | [2, 3] |
| 10 | [2, 3, 5, 7] |
| 11 | [2, 3, 5, 7, 11] |
| 30 | [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] |

Also check that:

- A limit of 49 produces 15 primes, ends with 47, and excludes 49.
- A limit of 100 produces 25 primes and ends with 97.
- Repeated calls with different limits work independently.

Compare your results with Part 1. Add at least three tests of your own, including a prime limit and a composite limit. If the two programs disagree, investigate rather than assuming either is correct.

## Improve It After It Works

When you reach 5, its multiples 10, 15, and 20 have already been crossed out by smaller primes. The first multiple that might need a new mark is 25. Similarly, for 7, it is 49.

Explain why a round led by a prime `p` can start crossing out at `p * p`.

You can also finish crossing-out rounds once the next candidate's square is greater than the limit. Every composite number has at least one prime factor no greater than its square root: if both factors in a factor pair were larger than that, their product would exceed the number.

For a limit of 30, the rounds for 2, 3, and 5 are enough. You still need to collect **all** the surviving numbers through 30, including those beyond the last round.

Improve your working program using these ideas, then rerun your checks. Pay attention to limits that are perfect squares, such as 25 and 49.

## Compare and Reflect

Keep your code and a short reflection answering:

- How does your list represent the numbers on paper?
- Why are all surviving numbers prime when the crossing-out rounds finish?
- How does this approach differ from calling your Part 1 checker on every number?
- What extra storage does this method use?
- Which test helped you find a mistake or confirm a boundary case?

Be ready to demonstrate your program and explain your reasoning in class.
