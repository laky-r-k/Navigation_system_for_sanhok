#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX 100
#define INF 99999

int find_index(char names[MAX][50], int count, char *name) {
    for (int i = 0; i < count; i++) {
        if (strcmp(names[i], name) == 0) return i;
    }
    return -1;
}

void dijkstra(int graph[MAX][MAX], int n, int start, int end, char names[MAX][50]) {
    int dist[MAX], visited[MAX], prev[MAX];
    for (int i = 0; i < n; i++) {
        dist[i] = INF;
        visited[i] = 0;
        prev[i] = -1;
    }
    dist[start] = 0;

    for (int i = 0; i < n; i++) {
        int u = -1;
        for (int j = 0; j < n; j++) {
            if (!visited[j] && (u == -1 || dist[j] < dist[u]))
                u = j;
        }

        if (dist[u] == INF) break;
        visited[u] = 1;

        for (int v = 0; v < n; v++) {
            if (graph[u][v] && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
                prev[v] = u;
            }
        }
    }

    // Print path
    int path[MAX], path_len = 0, temp = end;
    while (temp != -1) {
        path[path_len++] = temp;
        temp = prev[temp];
    }

    printf("Shortest path: ");
    for (int i = path_len - 1; i >= 0; i--) {
        printf("%s", names[path[i]]);
        if (i != 0) printf(" -> ");
    }
    printf("\nTotal distance: %d\n", dist[end]);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: dijkstra <start> <end>\n");
        return 1;
    }

    FILE *file = fopen("mapnav/graph_data/graph.txt", "r");
    if (!file) {
        perror("Cannot open file");
        return 1;
    }

    int edges;
    fscanf(file, "%d", &edges);

    char names[MAX][50];
    int graph[MAX][MAX] = {0}, node_count = 0;

    for (int i = 0; i < edges; i++) {
        char a[50], b[50];
        int cost;
        fscanf(file, "%s %s %d", a, b, &cost);

        int idx_a = find_index(names, node_count, a);
        if (idx_a == -1) {
            strcpy(names[node_count], a);
            idx_a = node_count++;
        }

        int idx_b = find_index(names, node_count, b);
        if (idx_b == -1) {
            strcpy(names[node_count], b);
            idx_b = node_count++;
        }

        graph[idx_a][idx_b] = cost;
        graph[idx_b][idx_a] = cost;
    }

    fclose(file);

    int start = find_index(names, node_count, argv[1]);
    int end = find_index(names, node_count, argv[2]);

    if (start == -1 || end == -1) {
        printf("Invalid node names.\n");
        return 1;
    }

    dijkstra(graph, node_count, start, end, names);
    return 0;
}
