# Step 1: Install and import the required library for ontology management
!pip -q install rdflib

from rdflib import Graph, RDF, URIRef
from rdflib.namespace import RDFS, OWL


# Step 2: Initialize a graph for the ontology
g = Graph()

# Define namespace
ontology = "http://example.org/ontology#"

animal = URIRef(ontology + "Animal")
mammal = URIRef(ontology + "Mammal")
bird = URIRef(ontology + "Bird")
dog = URIRef(ontology + "Dog")
eagle = URIRef(ontology + "Eagle")


# Step 3: Add entities and relationships

# Adding classes
g.add((animal, RDF.type, OWL.Class))
g.add((mammal, RDF.type, OWL.Class))
g.add((bird, RDF.type, OWL.Class))

# Adding relationships
g.add((mammal, RDFS.subClassOf, animal))
g.add((bird, RDFS.subClassOf, animal))

g.add((dog, RDF.type, mammal))
g.add((eagle, RDF.type, bird))


# Step 4: Query the ontology
# Query for entities whose type is a subclass of Animal
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?entity WHERE {
    ?entity rdf:type ?type .
    ?type rdfs:subClassOf <http://example.org/ontology#Animal> .
}
"""

results = g.query(query)

# Print results
for result in results:
    print(f"Entity: {result['entity']}")


# Step 5: Save the ontology to a file
g.serialize(
    destination="ontology.ttl",
    format="turtle"
)
