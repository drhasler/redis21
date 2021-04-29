import redis
from redisgraph import Node, Edge, Graph

r = redis.Redis(host='localhost', port=6379)

graph = Graph('graph', r)


def User(id):
    props = {'id': id}
    return Node(label='User', properties=props)


def Movie(id):
    props = {'id': id}
    return Node(label='Movie', properties=props)


"""
relations
User knows Movie (with some properties)
User follows User
"""

##############
# EDIT GRAPH #
##############


def upsert_node(n):
    id = n.properties['id']
    q = "MERGE (n:%s{id:'%s'}) " % (n.label, id)
    # SET properties
    graph.query(q)


def delete_node(n):
    id = n.properties['id']
    q = "MATCH (n:%s{id:'%s'}) " % (n.label, id)
    q += "DELETE n "
    graph.query(q)


def upsert_edge(e):
    s = e.src_node
    sid = s.properties['id']
    t = e.dest_node
    tid = t.properties['id']
    q = "MATCH (s:%s{id:'%s'}) " % (s.label, sid)
    q += "MATCH (t:%s{id:'%s'}) " % (t.label, tid)
    q += "MERGE (s)-[:%s]->(t) " % e.relation
    # SET properties
    graph.query(q)


def delete_edge(e):
    s = e.src_node
    sid = s.properties['id']
    t = e.dest_node
    tid = t.properties['id']
    q = "MATCH (s:%s{id:'%s'}) " % (s.label, sid)
    q += "MATCH (t:%s{id:'%s'}) " % (t.label, tid)
    q += "MATCH (s)-[r:%s]->(t) " % e.relation
    q += "DELETE r "
    graph.query(q)


###############
# QUERY GRAPH #
###############


def known_movies(user_id):
    q = "MATCH (u:User{id:'%s'}) " % user_id
    q += "MATCH (u)-[:knows]->(m:Movie) "
    q += "RETURN m.id"
    res = graph.query(q)
    return [record[0] for record in res.result_set]


def follows(user_id):
    q = "MATCH (u:User{id:'%s'}) " % user_id
    q = "MATCH (u)-[:follows]->(v:User) "
    q += "RETURN v.id"
    res = graph.query(q)
    return [record[0] for record in res.result_set]


def known_by(user_id, movie_id):
    q = "MATCH (u:User{id:'%s'}) " % user_id
    q += "MATCH (m:Movie{id:'%s'}) " % movie_id
    q += "MATCH (u)-[:follows]->(v:User)-[:knows]->(m) "
    q += "RETURN v.id"
    res = graph.query(q)
    return [record[0] for record in res.result_set]


if __name__ == '__main__':
    u1 = User('u1')
    u2 = User('u2')
    u3 = User('u3')
    m1 = Movie('m1')
    m2 = Movie('m2')
    e1 = Edge(u1, 'follows', u2)
    e2 = Edge(u2, 'knows', m1)
    e3 = Edge(u3, 'knows', m2)
    e4 = Edge(u1, 'follows', u3)

    for node in [u1,u2,u3,m1,m2]:
        upsert_node(node)
    for edge in [e1,e2,e3,e4]:
        upsert_edge(edge)

    print(known_movies('u3'))
    print(known_by('u1', 'm1'))
    print(follows('u1'))
    graph.delete()
