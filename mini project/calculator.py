"""
╔══════════════════════════════════════════════════════╗
║           🧮 Advanced Python Calculator              ║
║   Basic Ops | Statistics | Mean | Median | Mode      ║
╚══════════════════════════════════════════════════════╝
"""

from collections import Counter


# ─────────────────────────────────────────────
#  Helper: get a valid float from the user
# ─────────────────────────────────────────────
def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️  Invalid input – please enter a number.\n")


# ─────────────────────────────────────────────
#  Helper: get a list of numbers from the user
# ─────────────────────────────────────────────
def get_number_list() -> list[float]:
    while True:
        raw = input("  Enter numbers separated by spaces: ").strip()
        try:
            numbers = [float(x) for x in raw.split()]
            if len(numbers) < 1:
                raise ValueError
            return numbers
        except ValueError:
            print("  ⚠️  Please enter at least one valid number.\n")


# ─────────────────────────────────────────────
#  Basic Operations  (two operands)
# ─────────────────────────────────────────────
def basic_operations():
    print("\n  ── Basic Calculator ──")
    a = get_number("  Enter first number  : ")
    b = get_number("  Enter second number : ")

    print(f"\n  {'─'*30}")
    print(f"  ➕  {a} + {b}  =  {a + b}")
    print(f"  ➖  {a} - {b}  =  {a - b}")
    print(f"  ✖️   {a} × {b}  =  {a * b}")

    if b != 0:
        print(f"  ➗  {a} ÷ {b}  =  {a / b:.6g}")
        print(f"  💯  {a} % {b}   =  {a % b:.6g}")  # modulo
    else:
        print("  ➗  Division by zero – undefined.")
        print("  💯  Modulo by zero  – undefined.")

    # Percentage helper: what % is a of b?
    if b != 0:
        print(f"  📊  {a} is {(a / b) * 100:.4g}% of {b}")
    print(f"  {'─'*30}")


# ─────────────────────────────────────────────
#  Percentage standalone
# ─────────────────────────────────────────────
def percentage():
    print("\n  ── Percentage Calculator ──")
    print("  1. What is X% of Y?")
    print("  2. X is what % of Y?")
    print("  3. % change from X to Y?")
    ch = input("  Choose (1/2/3): ").strip()

    if ch == "1":
        x = get_number("  Enter percentage (X): ")
        y = get_number("  Enter value (Y)     : ")
        print(f"\n  ✅  {x}% of {y}  =  {(x / 100) * y:.6g}")

    elif ch == "2":
        x = get_number("  Enter X: ")
        y = get_number("  Enter Y: ")
        if y == 0:
            print("  ⚠️  Y cannot be zero.")
        else:
            print(f"\n  ✅  {x} is {(x / y) * 100:.4g}% of {y}")

    elif ch == "3":
        x = get_number("  Enter original value (X): ")
        y = get_number("  Enter new value (Y)      : ")
        if x == 0:
            print("  ⚠️  Original value cannot be zero.")
        else:
            change = ((y - x) / abs(x)) * 100
            direction = "increase" if change >= 0 else "decrease"
            print(f"\n  ✅  % {direction}: {abs(change):.4g}%")

    else:
        print("  ⚠️  Invalid choice.")


# ─────────────────────────────────────────────
#  Statistics
# ─────────────────────────────────────────────
def compute_mean(nums: list[float]) -> float:
    return sum(nums) / len(nums)


def compute_median(nums: list[float]) -> float:
    s = sorted(nums)
    n = len(s)
    mid = n // 2
    return (s[mid - 1] + s[mid]) / 2 if n % 2 == 0 else s[mid]


def compute_mode(nums: list[float]) -> list[float]:
    counts = Counter(nums)
    max_count = max(counts.values())
    if max_count == 1:
        return []   # no repeating value
    return sorted(k for k, v in counts.items() if v == max_count)


def statistics_menu():
    print("\n  ── Statistics Calculator ──")
    nums = get_number_list()
    n    = len(nums)

    mean   = compute_mean(nums)
    median = compute_median(nums)
    mode   = compute_mode(nums)
    total  = sum(nums)

    print(f"\n  {'─'*38}")
    print(f"  📋  Numbers : {nums}")
    print(f"  🔢  Count   : {n}")
    print(f"  ➕  Sum     : {total:.6g}")
    print(f"  📊  Average (Mean)  : {mean:.6g}")
    print(f"  📍  Median          : {median:.6g}")
    if mode:
        print(f"  🏆  Mode            : {mode}")
    else:
        print(f"  🏆  Mode            : No repeating values")

    # Bonus: range & variance
    data_range = max(nums) - min(nums)
    variance   = sum((x - mean) ** 2 for x in nums) / n
    std_dev    = variance ** 0.5
    print(f"  📐  Range           : {data_range:.6g}")
    print(f"  📉  Variance        : {variance:.6g}")
    print(f"  📉  Std Deviation   : {std_dev:.6g}")
    print(f"  {'─'*38}")


# ─────────────────────────────────────────────
#  Main Menu
# ─────────────────────────────────────────────
MENU = """
╔══════════════════════════════════════╗
║          🧮  CALCULATOR MENU         ║
╠══════════════════════════════════════╣
║  1. Basic Operations  (+  -  ×  ÷)  ║
║  2. Percentage        (%, X% of Y)  ║
║  3. Statistics        (Mean/Med/Mod) ║
║  0. Exit                            ║
╚══════════════════════════════════════╝
"""

def main():
    print(__doc__)
    while True:
        print(MENU)
        choice = input("  👉  Enter your choice: ").strip()

        if choice == "1":
            basic_operations()
        elif choice == "2":
            percentage()
        elif choice == "3":
            statistics_menu()
        elif choice == "0":
            print("\n  👋  Goodbye! Thanks for using the calculator.\n")
            break
        else:
            print("\n  ⚠️  Invalid choice. Please enter 0, 1, 2, or 3.")

        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()
