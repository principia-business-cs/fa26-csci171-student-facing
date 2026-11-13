# Fun with Prime Numbers

## The Challenge

Can you teach a computer to recognize a prime number using a rule you understand?

A **prime number** is an integer greater than 1 with exactly two positive factors: 1 and itself. For example, 7 is prime; 6 is not, because 2 and 3 also divide it evenly. The number 1 is not prime.

Practice functions, loops, conditionals, return values, and testing by developing your own solution in Python.

## Work From Your Own Thinking

Start individually and take a real stab at the problem before comparing ideas.

- Write your own code. Do not copy a prime-number solution from a website, classmate, textbook, or AI tool, or ask AI to generate the solution.
- You may look up what prime numbers are and consult Python documentation or class notes for syntax such as functions, loops, and the remainder operator (`%`).
- Do not use a library function that checks or generates primes, or hardcode a list of answers.
- You may discuss ideas and ask the instructor for a hint. Keep your implementation your own, and be ready to explain every line.
- An unfinished attempt with thoughtful notes is useful practice. Record what you tried and where you got stuck.

## 1. Explore Before Coding

On paper, classify the integers from 1 through 20 as prime or not prime. For each non-prime integer greater than 1, find a factor other than 1 and itself.

Then answer:

1. Why is 1 not prime? What about 0 and negative integers?
2. What makes 2 unusual among prime numbers?
3. Is every odd integer greater than 1 prime? Find a counterexample.
4. How would you decide whether a number you have never seen before is prime?

Write your proposed steps in plain English before opening your editor.

## 2. Write Your Prime Checker

Create a file named `prime_numbers.py` and write a function named `is_prime(n)`.

Assume `n` is an integer. Your function must **return** `True` if it is prime and `False` otherwise. Keep input prompts and printing outside this function.

Choose your own approach using loops, conditionals, and arithmetic. Begin with a method you can explain; you can improve it later.

Use these cases to check your work:

| Input | Expected return |
| --- | --- |
| -7 | False |
| 0 | False |
| 1 | False |
| 2 | True |
| 3 | True |
| 4 | False |
| 9 | False |
| 17 | True |
| 25 | False |
| 29 | True |
| 49 | False |

Add at least three test cases of your own. Predict each result before running your code. Include an even integer greater than 2, an odd non-prime integer, and a prime.

If a test fails, trace the values your function checks. Explain why your function cannot decide that a number is prime just because one possible divisor does not divide it evenly.

## 3. Find More Primes

Write a second function named `primes_up_to(limit)`. Assume `limit` is an integer.

Return a list of all prime numbers less than or equal to `limit`, in increasing order. Reuse your own `is_prime` function. For a limit below 2, return an empty list.

Examples:

- `primes_up_to(1)` returns `[]`.
- `primes_up_to(2)` returns `[2]`.
- `primes_up_to(10)` returns `[2, 3, 5, 7]`.
- `primes_up_to(11)` returns `[2, 3, 5, 7, 11]`.

Use your function to discover the primes up to 100. Compare the results with your paper predictions for 1 through 20.

## 4. Compare and Reflect

After making your own attempt, discuss your approach with a partner without copying code.

- What tells your function that a number is definitely not prime?
- When does it have enough information to return `True`?
- Which test exposed a mistake or gave you confidence in your approach?
- Did you and your partner use different methods? Explain one difference.
- What would you try next if you had more time?

Keep your code and a short reflection describing your approach, test results, and any remaining questions. Be ready to demonstrate your functions in class.

## Optional: Prime Playground

Choose one extension after your basic functions work:

- Find pairs of primes up to 100 that differ by 2. These are called **twin primes**.
- Find the first 20 primes instead of using a maximum value.
- Count how many possible divisors your checker tries. Can you reduce that count while keeping every result correct? Explain why your improvement works.
- Investigate perfect squares such as 49 and 121. Why are they useful tests for a prime checker?

The goal is to build and explain your own reasoning, even if your first solution is slow.
