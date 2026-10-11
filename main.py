"""
Simple UI state helper for command-line demos.
"""

class UIState:
    def __init__(self):
        self._state = {}

    def set(self, key, value):
        self._state[key] = value

    def get(self, key, default=None):
        return self._state.get(key, default)

    def toggle(self, key, true_val=True, false_val=False):
        current = self._state.get(key, None)
        self._state[key] = false_val if current == true_val else true_val

    def __repr__(self):
        return f"UIState({self._state})"

def demo():
    ui = UIState()
    ui.set('menu_visible', False)
    print("Initial:", ui)
    ui.toggle('menu_visible')
    print("Toggled:", ui)
    ui.set('theme', 'dark')
    print("Theme set:", ui.get('theme'))
    ui.toggle('theme', 'dark', 'light')
    print("Theme toggled:", ui.get('theme'))

if __name__ == "__main__":
    demo()