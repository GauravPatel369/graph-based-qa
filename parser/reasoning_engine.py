import numpy as np
from sentence_transformers import SentenceTransformer


class GraphReasoner:
    def __init__(self, graph, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.graph = graph
        self.model = SentenceTransformer(model_name)

    # -----------------------------------
    # embed query
    # -----------------------------------
    def embed_query(self, query):
        return self.model.encode([query])[0]

    # -----------------------------------
    # cosine similarity
    # -----------------------------------
    def cosine(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # -----------------------------------
    # get top seed nodes
    # -----------------------------------
    def get_seed_nodes(self, query, k=5):
        q_emb = self.embed_query(query)

        scores = []
        for node_id in self.graph.nodes:
            emb = self.graph.nodes[node_id]["embedding"]
            sim = self.cosine(q_emb, emb)
            scores.append((node_id, sim))

        scores.sort(key=lambda x: x[1], reverse=True)
        return [n for n, _ in scores[:k]]

    # ===================================
    # 1️⃣ FLAT RETRIEVAL
    # ===================================
    def flat_retrieval(self, query, k=5):
        seeds = self.get_seed_nodes(query, k)
        return seeds

    # ===================================
    # 2️⃣ STRUCTURAL TRAVERSAL
    # ===================================
    def structural_traversal(self, query, depth=2):
        seeds = self.get_seed_nodes(query, k=5)
        visited = set(seeds)
        frontier = list(seeds)

        for _ in range(depth):
            new_frontier = []

            for node in frontier:
                for neighbor in self.graph.neighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        new_frontier.append(neighbor)

            frontier = new_frontier

        return list(visited)

    # ===================================
    # 3️⃣ EMERGENT GRAPH REASONING
    # ===================================
    def emergent_reasoning(self, query, depth=3):
        q_emb = self.embed_query(query)
        seeds = self.get_seed_nodes(query, k=5)

        visited = set(seeds)
        frontier = list(seeds)

        for _ in range(depth):
            new_frontier = []

            for node in frontier:
                for nb in self.graph.neighbors(node):
                    if nb not in visited:
                        visited.add(nb)
                        new_frontier.append(nb)

            frontier = new_frontier

        # scoring
        scored = []
        for node in visited:
            emb = self.graph.nodes[node]["embedding"]
            sim = self.cosine(q_emb, emb)

            text = self.graph.nodes[node]["text"].lower()

            # exception bonus
            bonus = 0
            if any(x in text for x in ["except", "unless", "only if", "not allowed"]):
                bonus += 0.1

            score = sim + bonus
            scored.append((node, score))

        scored.sort(key=lambda x: x[1], reverse=True)

        return [n for n, _ in scored[:8]]
