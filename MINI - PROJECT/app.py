from flask import Flask, render_template, request, jsonify
import json
from collections import deque
import heapq

app = Flask(__name__)

# Load JSON
with open("knowledge_base.json", encoding="utf-8") as f:
    kb = json.load(f)

# ---------------- SEARCH ALGORITHMS ----------------
def bfs_search(start, target):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        if node == target:
            return node
        visited.add(node)

        for option in kb[node]["options"].values():
            if option not in visited:
                queue.append(option)
    return None


def dfs_search(node, target, visited=None):
    if visited is None:
        visited = set()

    if node == target:
        return node

    visited.add(node)

    for option in kb[node]["options"].values():
        if option not in visited:
            result = dfs_search(option, target, visited)
            if result:
                return result
    return None


def heuristic(node):
    return len(node)


def best_first_search(start, target):
    pq = []
    heapq.heappush(pq, (heuristic(start), start))
    visited = set()

    while pq:
        _, node = heapq.heappop(pq)
        if node == target:
            return node

        visited.add(node)

        for option in kb[node]["options"].values():
            if option not in visited:
                heapq.heappush(pq, (heuristic(option), option))
    return None


# NLP matching
def find_match(user_input):
    user_input = user_input.lower()

    for key in kb.keys():
        clean_key = key.replace("_", " ")
        if clean_key in user_input:
            return key
    return None


# Route
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    algo = request.json["algorithm"]

    match = find_match(user_input)

    if not match:
        return jsonify({"response": "Sorry, I didn't understand."})

    if match in ["hi", "hello", "greetings"]:
        return jsonify({"response": kb[match]["message"]})

    if algo == "BFS":
        result = bfs_search("start", match)
    elif algo == "DFS":
        result = dfs_search("start", match)
    else:
        result = best_first_search("start", match)

    if result:
        return jsonify({"response": kb[result]["message"]})
    else:
        return jsonify({"response": "No result found."})


if __name__ == "__main__":
    app.run(debug=True)
