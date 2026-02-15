from parser.pdf_parser import extract_pages
from parser.drg_nodes import build_nodes
from parser.drg_graph import DocumentReasoningGraph
from parser.reasoning_engine import GraphReasoner

pdf_path = "iNLP_A2.pdf"

pages = extract_pages(pdf_path)
nodes = build_nodes(pages)

drg = DocumentReasoningGraph()
graph = drg.build_graph(nodes)

reasoner = GraphReasoner(graph)

query = "When is the assignment deadline?"

# -------- helper function --------
def show_nodes(title, node_ids):
    print(f"\n{title}")
    print("=" * 50)
    for n in node_ids:
        text = graph.nodes[n]["text"]
        print(f"[{n}] {text}")


# -------- run methods --------
flat_nodes = reasoner.flat_retrieval(query)
struct_nodes = reasoner.structural_traversal(query)
emerg_nodes = reasoner.emergent_reasoning(query)

show_nodes("FLAT", flat_nodes)
show_nodes("STRUCTURAL", struct_nodes)
show_nodes("EMERGENT", emerg_nodes)