from openai import OpenAI
import json

from core.config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


class SchematicIoService:
    @staticmethod
    def ai_request(input_text: str) -> dict:
        prompt = f"""
            Analyze the text and extract a logical structure suitable for visualization as a directed graph in Cytoscape.js.
            Instructions:
            1. Split the text into clear logical sections (main ideas or thematic blocks).
            2. For each section:
               - Create a short, meaningful label (2–6 words).
               - Preserve the core idea in the label.
            3. Create graph elements in Cytoscape.js format:
               - Nodes must contain: id and label.
               - Edges must contain: id, source, and target.
            4. The graph must represent logical relationships (hierarchy, cause-effect, dependency, thematic expansion).
            5. Do NOT mix node and edge fields.
               - Nodes must NOT contain source or target.
               - Edges must NOT contain label unless it describes the relationship.
            6. Do NOT include "source" or "target" fields in nodes.  
               - Edges must be separate elements with proper "source" and "target" fields.  
               - Each element in the "elements" array must be either a node or an edge, never mix the two.  
               - Ensure the graph is fully connected with edges representing logical relationships.

            Return a coherent, logically connected directed graph.

            Text:
            {input_text}
        """
        
        completion = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "cytoscape_nodes_edges_schema",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "elements": {
                                "type": "object",
                                "properties": {
                                    "nodes": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "string"},
                                                "label": {"type": "string"}
                                            },
                                            "required": ["id", "label"]
                                        }
                                    },
                                    "edges": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "string"},
                                                "source": {"type": "string"},
                                                "target": {"type": "string"}
                                            },
                                            "required": ["id", "source", "target"]
                                        }
                                    }
                                },
                                "required": ["nodes", "edges"]
                            }
                        },
                        "required": ["elements"]
                    }
                }
            }
        )
        
        return json.loads(completion.choices[0].message.content)
     
    @staticmethod
    def build_schema(elements_dict: dict) -> dict:
        nodes = [{"data": n} for n in elements_dict["elements"]["nodes"]]
        edges = [{"data": e} for e in elements_dict["elements"]["edges"]]
        cytoscape_elements = nodes + edges

        elements_js = json.dumps(cytoscape_elements, ensure_ascii=False)

        html_block = (
            f'<div id="schematic-graph" style="width: 100%; height: 400px; background-image: linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px); background-size: 40px 40px; background-color: #0A0A1F;"></div>'
            f'<script src="https://unpkg.com/cytoscape/dist/cytoscape.min.js"></script>'
            f'<script>'
            f'const cy = cytoscape({{'
            f'container: document.getElementById("schematic-graph"),'
            f'elements: {elements_js},'
            f'style: ['

            # ---- NODE STYLE ----
            f'{{selector: "node", style: {{'
            f'content: "data(label)",'
            f'"text-valign": "center",'
            f'"text-halign": "center",'
            f'color: "#000000",'
            f'"font-size": "25px",'
            f'"font-weight": "600",'
            f'"text-wrap": "ellipsis",'
            f'"text-max-width": "180px",'
            f'"background-color": "#F4A261",'
            f'"border-width": 2,'
            f'"border-color": "#ffffff",'
            f'shape: "round-rectangle",'
            f'width: "250px",'
            f'height: "80px",'
            f'padding: "12px"'
            f'}}}},'

            # ---- EDGE STYLE ----
            f'{{selector: "edge", style: {{'
            f'width: 5,'
            f'"line-color": "#ffffff",'
            f'"line-style": "dashed",'
            f'"target-arrow-color": "#ffffff",'
            f'"target-arrow-shape": "triangle",'
            f'"curve-style": "bezier"'
            f'}}}}'

            f'],'

            # ---- LAYOUT ----
            f'layout: {{'
            f'name: "breadthfirst",'
            f'directed: true,'
            f'padding: 20,'
            f'spacingFactor: 0.7'  # делает граф компактнее (ребра короче)
            f'}}'

            f'}});'
            f'</script>'

        )

        return html_block
