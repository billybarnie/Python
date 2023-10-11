

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"Reversed list: {fruit_list}")

    fruit_list.append("oranges")
    print(f"Oranges added: {fruit_list}")

    fruit_list.insert(1, "cherry")
    print(f"Cherry inserted: {fruit_list}")

    fruit_list.remove("banana")
    print(f"Removed banana: {fruit_list}")

    fruit_list.pop()
    print(f"last element removed: {fruit_list}")

    fruit_list.sort()
    print(f"Sorted: {fruit_list}")

    fruit_list.clear()
    print(f"Cleared: {fruit_list}")


if __name__ == "__main__":
    main()