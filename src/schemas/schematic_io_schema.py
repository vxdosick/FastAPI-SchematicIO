from pydantic import BaseModel
from typing import List


class TextRequest(BaseModel):
    text: str


class Node(BaseModel):
    id: str
    label: str


class Edge(BaseModel):
    id: str
    source: str
    target: str


class Elements(BaseModel):
    nodes: List[Node]
    edges: List[Edge]


class SchematicResponse(BaseModel):
    elements: Elements