{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNkrT5Jl+R5OS7nYZnRYW5j"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "import timeit\n",
        "import cProfile\n",
        "def is_prime(n):\n",
        "    if n \u003C= 1:\n",
        "        return False\n",
        "    for i in range(2, n):\n",
        "        if n % i == 0:\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "def sum_of_primes_naive(numbers):\n",
        "    total = 0\n",
        "    for number in numbers:\n",
        "        if is_prime(number):\n",
        "            total += number\n",
        "    return total\n"
      ],
      "metadata": {
        "id": "62kqP_1Gylfo",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717883839717,
          "user_tz": 420,
          "elapsed": 188,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        }
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Generate a list of numbers\n",
        "numbers = list(range(1, 100000))\n",
        "sum_of_primes_naive(numbers)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iMLK38E_1oxU",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717884269856,
          "user_tz": 420,
          "elapsed": 41199,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "b803f404-401a-4488-faf2-9f6160ef64d4"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "454396537"
            ]
          },
          "metadata": {

          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Measure time using timeit\n",
        "execution_time = timeit.timeit('sum_of_primes_naive(numbers)', globals=globals(), number=1)\n",
        "print(f\"Execution time: {execution_time} seconds\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8gRZnb8G4P7O",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717884310085,
          "user_tz": 420,
          "elapsed": 40231,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "a07f24d3-6576-4dd1-b8d8-50759ba48a6e"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Execution time: 40.20760166499997 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "get_user_time = timeit.timeit(lambda: sum_of_primes_naive(numbers), number=1)\n",
        "print(f\"Execution time for sum_of_primes: {get_user_time} seconds\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GTcItCtD0u3y",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717884017573,
          "user_tz": 420,
          "elapsed": 11051,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "c4cb77c8-3ba8-4707-f944-f9ac21f8699c"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Execution time for sum_of_primes: 10.844169482000012 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cProfile.run('sum_of_primes_naive(numbers)')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ANFvfM1iywwr",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717884599707,
          "user_tz": 420,
          "elapsed": 52418,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "3fa5ccd1-ec51-4a37-cbde-660d09058f3b"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "         100003 function calls in 52.203 seconds\n",
            "\n",
            "   Ordered by: standard name\n",
            "\n",
            "   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n",
            "        1    0.046    0.046   52.203   52.203 \u003Cipython-input-3-ecbf73245c3a\u003E:12(sum_of_primes_naive)\n",
            "    99999   52.156    0.001   52.156    0.001 \u003Cipython-input-3-ecbf73245c3a\u003E:4(is_prime)\n",
            "        1    0.000    0.000   52.203   52.203 \u003Cstring\u003E:1(\u003Cmodule\u003E)\n",
            "        1    0.000    0.000   52.203   52.203 {built-in method builtins.exec}\n",
            "        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "def is_prime_optimized(n):\n",
        "    if n \u003C= 1:\n",
        "        return False\n",
        "    if n \u003C= 3:\n",
        "        return True\n",
        "    if n % 2 == 0 or n % 3 == 0:\n",
        "        return False\n",
        "    i = 5\n",
        "    while i * i \u003C= n:\n",
        "        if n % i == 0 or n % (i + 2) == 0:\n",
        "            return False\n",
        "        i += 6\n",
        "    return True\n",
        "\n",
        "def sum_of_primes_optimized(numbers):\n",
        "    total = 0\n",
        "    for number in numbers:\n",
        "        if is_prime_optimized(number):\n",
        "            total += number\n",
        "    return total\n",
        "\n",
        "# Measure the time taken by the optimized implementation\n",
        "start_time = time.time()\n",
        "total_optimized = sum_of_primes_optimized(numbers)\n",
        "print(f\"Optimized Implementation: Sum of primes = {total_optimized}, Time taken = {time.time() - start_time} seconds\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5mt_SJ74ymKS",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717885644131,
          "user_tz": 420,
          "elapsed": 205,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "57794678-538e-414a-89ce-d8f408a789ac"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Optimized Implementation: Sum of primes = 454396537, Time taken = 0.11378026008605957 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "get_user_time = timeit.timeit(lambda: sum_of_primes_optimized(numbers), number=1)\n",
        "print(f\"Execution time for sum_of_primes: {get_user_time} seconds\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hInww94b6IEU",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717885646713,
          "user_tz": 420,
          "elapsed": 205,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "2d0c27b9-0ee7-4d61-ed1e-7bb0cb4e69b8"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Execution time for sum_of_primes: 0.13188440499993703 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cProfile.run('sum_of_primes_optimized(numbers)')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9nJGMgs-y-YN",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717885650015,
          "user_tz": 420,
          "elapsed": 477,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "6f947452-01b8-4f4b-852e-6e8329ed6b44"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "         100003 function calls in 0.184 seconds\n",
            "\n",
            "   Ordered by: standard name\n",
            "\n",
            "   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n",
            "        1    0.022    0.022    0.184    0.184 \u003Cipython-input-16-79341f60958d\u003E:17(sum_of_primes_optimized)\n",
            "    99999    0.162    0.000    0.162    0.000 \u003Cipython-input-16-79341f60958d\u003E:3(is_prime_optimized)\n",
            "        1    0.000    0.000    0.184    0.184 \u003Cstring\u003E:1(\u003Cmodule\u003E)\n",
            "        1    0.000    0.000    0.184    0.184 {built-in method builtins.exec}\n",
            "        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "import math\n",
        "\n",
        "# Naive primality check\n",
        "def is_prime(n):\n",
        "    if n \u003C= 1:\n",
        "        return False\n",
        "    for i in range(2, n):\n",
        "        if n % i == 0:\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "# Optimized primality check\n",
        "def is_prime_optimized(n):\n",
        "    if n \u003C= 1:\n",
        "        return False\n",
        "    if n \u003C= 3:\n",
        "        return True\n",
        "    if n % 2 == 0 or n % 3 == 0:\n",
        "        return False\n",
        "    i = 5\n",
        "    while i * i \u003C= n:\n",
        "        if n % i == 0 or n % (i + 2) == 0:\n",
        "            return False\n",
        "        i += 6\n",
        "    return True\n",
        "\n",
        "# Naive sum of primes\n",
        "def sum_of_primes_naive(numbers):\n",
        "    total = 0\n",
        "    for number in numbers:\n",
        "        if is_prime(number):\n",
        "            total += number\n",
        "    return total\n",
        "\n",
        "# Optimized sum of primes\n",
        "def sum_of_primes_optimized(numbers):\n",
        "    total = 0\n",
        "    for number in numbers:\n",
        "        if is_prime_optimized(number):\n",
        "            total += number\n",
        "    return total\n",
        "\n",
        "# Generate a list of numbers\n",
        "numbers = list(range(1, 10000))\n",
        "\n",
        "# Measure the time taken by the naive implementation\n",
        "start_time = time.time()\n",
        "total_naive = sum_of_primes_naive(numbers)\n",
        "print(f\"Naive Implementation: Sum of primes = {total_naive}, Time taken = {time.time() - start_time} seconds\")\n",
        "\n",
        "# Measure the time taken by the optimized implementation\n",
        "start_time = time.time()\n",
        "total_optimized = sum_of_primes_optimized(numbers)\n",
        "print(f\"Optimized Implementation: Sum of primes = {total_optimized}, Time taken = {time.time() - start_time} seconds\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wsyxgdMYyoEZ",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882774096,
          "user_tz": 420,
          "elapsed": 1068,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "cde1f184-602d-4b5d-e83a-d39de6ea6718"
      },
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Naive Implementation: Sum of primes = 5736396, Time taken = 0.8963015079498291 seconds\n",
            "Optimized Implementation: Sum of primes = 5736396, Time taken = 0.012197732925415039 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "import numpy as np\n",
        "\n",
        "# Naive matrix multiplication\n",
        "def naive_matrix_multiply(A, B):\n",
        "    n = len(A)\n",
        "    C = [[0] * n for _ in range(n)]\n",
        "    for i in range(n):\n",
        "        for j in range(n):\n",
        "            for k in range(n):\n",
        "                C[i][j] += A[i][k] * B[k][j]\n",
        "    return C\n",
        "\n",
        "# Generate random matrices\n",
        "n = 200\n",
        "A = np.random.rand(n, n).tolist()\n",
        "B = np.random.rand(n, n).tolist()\n",
        "\n",
        "start_time = time.time()\n",
        "C_naive = naive_matrix_multiply(A, B)\n",
        "print(f\"Naive Matrix Multiplication Time: {time.time() - start_time} seconds\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lu3mWMkex-Jw",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882583699,
          "user_tz": 420,
          "elapsed": 2063,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "a94b3d35-21a7-4bde-97a0-7a5a15d5aeb6"
      },
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Naive Matrix Multiplication Time: 1.7987112998962402 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cProfile.run('naive_matrix_multiply(A, B)')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iOhXSknWyOyf",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882668756,
          "user_tz": 420,
          "elapsed": 3582,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "78946b0f-a1aa-4a0b-c8f6-5f6761950a76"
      },
      "execution_count": 86,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "         6 function calls in 3.342 seconds\n",
            "\n",
            "   Ordered by: standard name\n",
            "\n",
            "   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n",
            "        1    3.341    3.341    3.341    3.341 \u003Cipython-input-84-e4215f1013a5\u003E:5(naive_matrix_multiply)\n",
            "        1    0.000    0.000    0.000    0.000 \u003Cipython-input-84-e4215f1013a5\u003E:7(\u003Clistcomp\u003E)\n",
            "        1    0.001    0.001    3.342    3.342 \u003Cstring\u003E:1(\u003Cmodule\u003E)\n",
            "        1    0.000    0.000    3.342    3.342 {built-in method builtins.exec}\n",
            "        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}\n",
            "        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Optimized matrix multiplication using NumPy\n",
        "start_time = time.time()\n",
        "C_optimized = np.dot(A, B)\n",
        "print(f\"Optimized Matrix Multiplication Time: {time.time() - start_time} seconds\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4uANWZQKyDAP",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882600535,
          "user_tz": 420,
          "elapsed": 200,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "25e71d94-6d87-4473-90b0-f61ab3d2edbf"
      },
      "execution_count": 85,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Optimized Matrix Multiplication Time: 0.019355297088623047 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Import necessary libraries\n",
        "import random\n",
        "import heapq\n",
        "import timeit\n",
        "import cProfile\n",
        "\n",
        "# Generate a large, sparse directed graph\n",
        "def generate_graph(num_nodes, max_edges_per_node):\n",
        "    graph = {i: [] for i in range(num_nodes)}\n",
        "    for i in range(num_nodes):\n",
        "        num_edges = min_edges_per_node + random.randint(1, (max_edges_per_node-min_edges_per_node))\n",
        "        for _ in range(num_edges):\n",
        "            target = random.randint(0, num_nodes - 1)\n",
        "            weight = int(random.uniform(1, 10))\n",
        "            graph[i].append((target, weight))\n",
        "    return graph\n",
        "\n",
        "# Create a graph with 1000 nodes and up to 10 edges per node\n",
        "num_nodes = 1000\n",
        "min_edges_per_node = 100\n",
        "max_edges_per_node = 900\n",
        "graph = generate_graph(num_nodes, max_edges_per_node)\n",
        "\n",
        "print(\"Graph generation complete.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nhPutqv_s1c7",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882264238,
          "user_tz": 420,
          "elapsed": 1056,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "e99800f2-d9ee-40de-dc85-6c9b1b0b5d7c"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Graph generation complete.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(graph)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Unoce-OEtD3Z",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882266396,
          "user_tz": 420,
          "elapsed": 210,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "730cff43-c7b5-4c3c-dc88-6065fc30b57b"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "IOPub data rate exceeded.\n",
            "The notebook server will temporarily stop sending output\n",
            "to the client in order to avoid crashing it.\n",
            "To change this limit, set the config variable\n",
            "`--NotebookApp.iopub_data_rate_limit`.\n",
            "\n",
            "Current values:\n",
            "NotebookApp.iopub_data_rate_limit=1000000.0 (bytes/sec)\n",
            "NotebookApp.rate_limit_window=3.0 (secs)\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Import necessary libraries\n",
        "import random\n",
        "import heapq\n",
        "import timeit\n",
        "import cProfile\n",
        "\n",
        "# Implement Dijkstra's algorithm\n",
        "def dijkstra(graph, start, goal):\n",
        "    queue = [(0, start)]\n",
        "    distances = {node: float('inf') for node in graph}\n",
        "    distances[start] = 0\n",
        "    previous_nodes = {node: None for node in graph}\n",
        "\n",
        "    while queue:\n",
        "        current_distance, current_node = heapq.heappop(queue)\n",
        "\n",
        "        if current_node == goal:\n",
        "            break\n",
        "\n",
        "        if current_distance \u003E distances[current_node]:\n",
        "            continue\n",
        "\n",
        "        for neighbor, weight in graph[current_node]:\n",
        "            distance = current_distance + weight\n",
        "            if distance \u003C distances[neighbor]:\n",
        "                distances[neighbor] = distance\n",
        "                previous_nodes[neighbor] = current_node\n",
        "                heapq.heappush(queue, (distance, neighbor))\n",
        "\n",
        "    path = []\n",
        "    current = goal\n",
        "    while current is not None:\n",
        "        path.append(current)\n",
        "        current = previous_nodes[current]\n",
        "    path.reverse()\n",
        "\n",
        "    if distances[goal] == float('inf'):\n",
        "        return [], float('inf')  # If there's no path to the goal\n",
        "\n",
        "    return path, distances[goal]\n",
        "\n",
        "# Test Dijkstra's algorithm with different start and goal nodes\n",
        "start_node = 0\n",
        "goal_node = 500  # Test with a different goal node\n",
        "\n",
        "print(\"Testing Dijkstra's algorithm...\")\n",
        "path, distance = dijkstra(graph, start_node, goal_node)\n",
        "print(f\"Shortest path from {start_node} to {goal_node}: {path}\")\n",
        "print(f\"Total distance: {distance}\")\n",
        "\n",
        "start_node = 100\n",
        "goal_node = 200  # Test with another different goal node\n",
        "\n",
        "print(\"Testing Dijkstra's algorithm with different start and goal...\")\n",
        "path, distance = dijkstra(graph, start_node, goal_node)\n",
        "print(f\"Shortest path from {start_node} to {goal_node}: {path}\")\n",
        "print(f\"Total distance: {distance}\")\n",
        "\n",
        "start_node = 999\n",
        "goal_node = 0  # Test with goal node at the start\n",
        "\n",
        "print(\"Testing Dijkstra's algorithm with reversed start and goal...\")\n",
        "path, distance = dijkstra(graph, start_node, goal_node)\n",
        "print(f\"Shortest path from {start_node} to {goal_node}: {path}\")\n",
        "print(f\"Total distance: {distance}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ydub6Lfos4G5",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882272164,
          "user_tz": 420,
          "elapsed": 198,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "75b7f6ba-a8c8-4748-ad2c-9510bfee923e"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Testing Dijkstra's algorithm...\n",
            "Shortest path from 0 to 500: [0, 191, 500]\n",
            "Total distance: 2\n",
            "Testing Dijkstra's algorithm with different start and goal...\n",
            "Shortest path from 100 to 200: [100, 236, 200]\n",
            "Total distance: 2\n",
            "Testing Dijkstra's algorithm with reversed start and goal...\n",
            "Shortest path from 999 to 0: [999, 381, 0]\n",
            "Total distance: 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Measure execution time of Dijkstra's algorithm\n",
        "dijkstra_time = timeit.timeit(lambda: dijkstra(graph, start_node, goal_node), number=1)\n",
        "print(f\"Execution time for Dijkstra's algorithm: {dijkstra_time} seconds\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gxbRU_GTs7YV",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882287132,
          "user_tz": 420,
          "elapsed": 206,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "d7b8c188-17f6-4e8d-db59-874f76c5b748"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Execution time for Dijkstra's algorithm: 0.004786953000120775 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Do 100 examples\n",
        "for i in range(100):\n",
        "    start_node = random.randint(0, num_nodes - 1)\n",
        "    goal_node = random.randint(0, num_nodes - 1)\n",
        "\n",
        "    # Measure the execution time of the Dijkstra's algorithm\n",
        "    start_time = timeit.default_timer()\n",
        "    path, distance = dijkstra(graph, start_node, goal_node)\n",
        "    end_time = timeit.default_timer()\n",
        "\n",
        "    dijkstra_time = end_time - start_time\n",
        "\n",
        "    print(f\"Execution time for Dijkstra's algorithm: {dijkstra_time:.6f} seconds\")\n",
        "    #print(f\"Shortest path from {start_node} to {goal_node}: {path}\")\n",
        "    #print(f\"Total distance: {distance}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e8o8ko2wtJwp",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882316542,
          "user_tz": 420,
          "elapsed": 4232,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "14ca63f7-eac8-4ad1-e15a-82a4fb7cc7be"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Execution time for Dijkstra's algorithm: 0.032082 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.076031 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.024136 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.034602 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.051995 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.043277 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.046637 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.008110 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.005897 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.179297 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.064515 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.009826 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.049530 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.013921 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.023917 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.052418 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.054499 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.043868 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.058755 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.042882 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.064934 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.036909 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.070205 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.000315 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.067737 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.059687 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.017864 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.058255 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.057375 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.026033 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.007123 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.038729 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.034440 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.049431 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.065315 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.033744 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.024527 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.062597 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.055393 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.010616 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.018812 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.013155 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.004476 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.002093 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.011835 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.021365 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.016756 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.063925 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.051120 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.026479 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.057961 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.009411 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.049937 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.030055 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.057456 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.008659 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.010188 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.025225 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.032741 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.021732 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.008730 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.016466 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.073247 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.062306 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.009704 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.035620 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.034416 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.035457 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.016915 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.025112 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.026302 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.046810 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.052238 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.014031 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.027880 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.009784 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.061780 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.060901 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.034982 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.046379 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.004030 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.033151 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.062739 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.041678 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.094453 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.085745 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.010236 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.048837 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.077085 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.094503 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.097649 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.089452 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.046869 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.028740 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.034474 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.023220 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.022318 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.007502 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.017202 seconds\n",
            "Execution time for Dijkstra's algorithm: 0.088599 seconds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#start_node = random.randint(0, num_nodes - 1)\n",
        "#goal_node = random.randint(0, num_nodes - 1)\n",
        "start_node = 1\n",
        "end_node = 20\n",
        "cProfile.run('dijkstra(graph, start_node, goal_node)')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2f1GQffpv-Kk",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882510013,
          "user_tz": 420,
          "elapsed": 3,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "d46fe44b-a089-4276-c2cd-4fb7d04f5b5d"
      },
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "         2865 function calls in 0.034 seconds\n",
            "\n",
            "   Ordered by: standard name\n",
            "\n",
            "   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n",
            "        1    0.001    0.001    0.001    0.001 \u003Cipython-input-53-0edeba46f173\u003E:10(\u003Cdictcomp\u003E)\n",
            "        1    0.000    0.000    0.000    0.000 \u003Cipython-input-53-0edeba46f173\u003E:12(\u003Cdictcomp\u003E)\n",
            "        1    0.031    0.031    0.033    0.033 \u003Cipython-input-53-0edeba46f173\u003E:8(dijkstra)\n",
            "        1    0.000    0.000    0.034    0.034 \u003Cstring\u003E:1(\u003Cmodule\u003E)\n",
            "      252    0.001    0.000    0.001    0.000 {built-in method _heapq.heappop}\n",
            "     2603    0.001    0.000    0.001    0.000 {built-in method _heapq.heappush}\n",
            "        1    0.000    0.000    0.034    0.034 {built-in method builtins.exec}\n",
            "        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}\n",
            "        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n",
            "        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Implement Dijkstra's algorithm\n",
        "def faster_dijkstra(graph, start, goal):\n",
        "    queue = [(0, start)]\n",
        "    distances = {node: float('inf') for node in graph}\n",
        "    distances[start] = 0\n",
        "    previous_nodes = {node: None for node in graph}\n",
        "    visited = set()\n",
        "\n",
        "    while queue:\n",
        "        current_distance, current_node = heapq.heappop(queue)\n",
        "\n",
        "        if current_node in visited:\n",
        "            continue\n",
        "        visited.add(current_node)\n",
        "\n",
        "        if current_node == goal:\n",
        "            break\n",
        "\n",
        "        for neighbor, weight in graph[current_node]:\n",
        "            if neighbor in visited:\n",
        "                continue\n",
        "            distance = current_distance + weight\n",
        "            if distance \u003C distances[neighbor]:\n",
        "                distances[neighbor] = distance\n",
        "                previous_nodes[neighbor] = current_node\n",
        "                heapq.heappush(queue, (distance, neighbor))\n",
        "\n",
        "    path = []\n",
        "    current = goal\n",
        "    while current is not None:\n",
        "        path.append(current)\n",
        "        current = previous_nodes[current]\n",
        "    path.reverse()\n",
        "\n",
        "    if distances[goal] == float('inf'):\n",
        "        return [], float('inf')  # If there's no path to the goal\n",
        "\n",
        "    return path, distances[goal]"
      ],
      "metadata": {
        "id": "ZSXnk80ZwDjn",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882430206,
          "user_tz": 420,
          "elapsed": 205,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        }
      },
      "execution_count": 65,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "start_node = 1\n",
        "goal_node = 200\n",
        "cProfile.run('dijkstra(graph, start_node, goal_node)')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aUMrBpEAxb_c",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1717882514583,
          "user_tz": 420,
          "elapsed": 218,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "8e8d0356-01fd-4c2a-a06e-b5e322059361"
      },
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "         2865 function calls in 0.046 seconds\n",
            "\n",
            "   Ordered by: standard name\n",
            "\n",
            "   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n",
            "        1    0.000    0.000    0.000    0.000 \u003Cipython-input-53-0edeba46f173\u003E:10(\u003Cdictcomp\u003E)\n",
            "        1    0.000    0.000    0.000    0.000 \u003Cipython-input-53-0edeba46f173\u003E:12(\u003Cdictcomp\u003E)\n",
            "        1    0.044    0.044    0.046    0.046 \u003Cipython-input-53-0edeba46f173\u003E:8(dijkstra)\n",
            "        1    0.000    0.000    0.046    0.046 \u003Cstring\u003E:1(\u003Cmodule\u003E)\n",
            "      252    0.001    0.000    0.001    0.000 {built-in method _heapq.heappop}\n",
            "     2603    0.001    0.000    0.001    0.000 {built-in method _heapq.heappush}\n",
            "        1    0.000    0.000    0.046    0.046 {built-in method builtins.exec}\n",
            "        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}\n",
            "        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n",
            "        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}\n",
            "\n",
            "\n"
          ]
        }
      ]
    }
  ]
}