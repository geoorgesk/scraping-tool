def collect_facts():
    print("Enter your facts (multi-line supported).")
    print("Separate each fact with an empty line.")
    print("Press Enter twice at the end to finish:\n")

    facts = []
    current_fact = []

    while True:
        line = input()
        if line.strip() == "":
            if current_fact:
                facts.append(" ".join(current_fact).strip())
                current_fact = []
            else:
                # Two consecutive blank lines means end
                break
        else:
            current_fact.append(line.strip())

    with open("numbered_facts.txt", "w", encoding="utf-8") as file:
        for i, fact in enumerate(facts, start=1):
            file.write(f"{i}. {fact}\n")

    print("\nSaved to 'numbered_facts.txt'")


if __name__ == "__main__":
    collect_facts()
