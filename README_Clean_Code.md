# Gilded Rose Refactoring — Clean Code Edition (Python)

## Introduction

This project is a clean-code refactor of the well-known **Gilded Rose Kata**. The goal of this refactoring effort was to apply Python best practices, reduce cyclomatic complexity, and improve the maintainability and testability of the code. 

Key software design principles such as the Open/Closed Principle (OCP), encapsulation, polymorphism, and modular architecture were applied to restructure the core logic while ensuring backward compatibility with the original interface.


## Refactored update_quality using the Open/Closed Principle

Originally, the update_quality() method in the GildedRose class contained a large, fragile chain of 'if-elif' statements handling all item types in a monolithic block. This violated the **Open/Closed Principle** — every time a new item behavior needed to be introduced, the function had to be modified.

## Added a Factory Function: item_factory()

The 'item_factory()' function is responsible for returning the item wrapper based on the item’s name. This approach ensures that the core 'GildedRose' logic remains agnostic to item-specific rules.

## Created Dedicated Classes per Item Type

Each item behavior is now encapsulated in a dedicated class that extends a common base wrapper. These classes implement their own 'update_quality()' logic, respecting each item's unique behavior.

Classes include:

- AgedBrieItem
- BackstagePassItem
- SulfurasItem
- ConjuredItem
- DefaultItem

This design follows the Single Responsibility Principle and leverages polymorphism to avoid nested conditionals, making the rules modular, isolated, and testable.

## Maintained Interface Compatibility

As required by the kata, the original Item class and the items property were left untouched. The new logic wraps the original Item instances without modifying them directly. This ensures full backward compatibility with existing external code while giving us internal flexibility.

## GitHub Actions CI/CD Pipeline

A GitHub Actions workflow was created to enforce code quality and automate tests on every push and pull request to main:

- Code formatting (`black`)
- Import sorting (`isort`)
- Style linting (`flake8`)
- Static analysis (`pylint`)
- Type checking (`mypy`)
- Unit + Approval tests (`pytest`, `approvaltests`)

This ensures any future contributions adhere to clean code standards and don’t break existing behavior.

---

## Tests Refactored

The test suite was fully restructured to improve readability, maintainability, and separation of concerns. Tests are now grouped by item type and reflect each rule in a clear, expressive way. 

**Approval testing** was retained to guarantee no regressions in expected outputs during refactoring.

---
