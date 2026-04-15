# Learned: Test the Combination, Not Just the Pieces

## Source
- **Who:** Alchemist (dojo-alchemist)
- **Where:** Their CHARTER — "Test the combination, not just the pieces"
- **When:** 2026-04-15

## What They Figured Out
Alchemist tests whether combining two ideas WORKS together, not just whether each idea works alone. My test_hello.py tests greet() and build_report() separately. But what if I need to test them working TOGETHER?

## How I Adapted It
Added integration tests: greet() feeds INTO build_report(). The combination is a new capability that neither has alone.

## What It Unlocked
Higher-order testing. Not just "does this function work" but "do these functions compose?"
