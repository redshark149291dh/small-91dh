"""Small UI state helper demo."""

class UIState:
    """Simple UI state manager for command‑line apps."""
    def __init__(self, initial):
        self.stack = [initial]
    def current(self):
        return self.stack[-1]
    def push(self, state):
        self.stack.append(state)
    def pop(self):
        if len(self.stack) > 1:
            self.stack.pop()

def main():
    ui = UIState("main")
    menu = {
        "main": {"1": lambda: ui.push("settings"), "2": lambda: exit(), "q": lambda: exit()},
        "settings": {"b": lambda: ui.pop(), "q": lambda: exit()},
    }
    actions = {"1": "Open settings", "2": "Quit", "q": "Quit", "b": "Back"}
    while True:
        cur = ui.current()
        print(f"\n--- {cur} screen ---")
        for k, d in actions.items():
            if k in menu[cur]:
                print(f"[{k}] {d}")
        choice = input("Choose: ").strip()
        if choice in menu[cur]:
            menu[cur][choice]()
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()