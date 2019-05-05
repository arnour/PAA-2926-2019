from paa191t1.dijkstra import datastructs


def dijkstra(graph, source_node, distance_struct=datastructs.DijkstraDistance()):
    """O algoritmo considera um conjunto de menores caminhos a partir de um nó inicial.

    A cada iteração busca-se nas adjacências de cada um dos nós, aquele com menor distância
    do nó inicial e o adiciona ao conjunto de menores caminhos. Esse passo é repetido para
    todos os nós alcançáveis a partir do nó inicial.

    As arestas que ligarem nós que já tenham
    sido adicionados ao conjunto de menores caminhos serão desconsideradas.

    Args:
        graph (struc.Graph): Grafo contendo os nós e arestas
        source_node (int): Vértice inicial a partir do qual os menores caminhos serão calculados.
        distance_struct (struc.DijkstraDistance): Uma das estruturas de dados no pacote struct que extendam DijkstraDistance.
    Returns:
        dict(), dict(): As distâncias e os predecessores de cada nó.
    """

    predecessors = {}

    # Cria a estrutura de dados responsável por armazenar as distâncias
    struct = distance_struct(graph.all_nodes())

    # Inicializa o nó inicial com o menor valor
    # Considere o nó inicial como s
    # Distância de s até s é zero, logo d(s) = 0
    struct.update(source_node, 0)

    # Itera sobre cada nó do grafo
    # n é o número de vértices do grafo G
    # m é o número de arestas do grafo G
    # O total de iterações será o número de nós do grafo, já que a cada rodada um nó é removido (pop).
    while struct.has_nodes_to_visit():

        # Encontra e retorna o nó de menor distância e sua respectiva distância.
        # Considere origin_node como v
        # Considere origin_node_distance d(v)
        origin_node, origin_node_distance = struct.pop()

        # Itera sobre cada aresta adjacente de v
        # O total de iterações será o número de arestas do grafo, pois a cada iteração as arestas de cada um dos nós é visitada.
        # Considere target_node como u
        for target_node in graph.successors(origin_node):

            # Recupera a distância atual que este nó vizinho está do nó inicial
            # Considere target_node_distance como d(u)
            target_node_distance = struct.value(target_node)

            # Recupara o peso dessa aresta
            # Considere esta aresta como e(v, u) e seu peso como w
            edge_weight = graph.edge_weight(origin_node, target_node)

            # Calcula a nova distância de u até o nó inicial, considerando que ele vá passar por v
            # Considere a nova distância como d' = d(v) + w
            new_target_node_distance = origin_node_distance + edge_weight

            # Se a distância d(u) > d' então um caminho mais curto partindo do nó inicial até u (passando por v) foi encontrado
            # Neste caso, atualiza-se a d(u) com o valor de d'
            # Armazena que nó v é o predecessor de u no caminho mais curto
            if target_node_distance > new_target_node_distance:
                struct.update(target_node, new_target_node_distance)
                predecessors[target_node] = origin_node

    # Retorna as distâncias mais curtas do nó inicial para todos os nós
    # Retorna também cada nó e seu predecessor, pois dessa maneira é possível determinar o caminho
    return struct.values, predecessors
