import json
import os

q_table_path = "output/q_table.json"

class RLAgent:
    def __init__(self):
        self.q_table = {}
        os.makedirs("output", exist_ok=True)
        if os.path.exists(q_table_path):
            with open(q_table_path, "r") as f:
                self.q_table = json.load(f)
        else:
            self._save()

    def get_action(self, categories):
        # Choose category with highest Q-value (or random if none)
        max_reward = float("-inf")
        best_category = None
        for category in categories:
            reward = self.q_table.get(category, 0)
            if reward > max_reward:
                max_reward = reward
                best_category = category
        return best_category if best_category else categories[0]

    def update(self, category, reward):
        current = self.q_table.get(category, 0)
        self.q_table[category] = current + reward
        self._save()

    def _save(self):
        with open(q_table_path, "w") as f:
            json.dump(self.q_table, f, indent=2)
