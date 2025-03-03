{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNgxsCyzK3hJzckO662gW0m"
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
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O6rnSo717R_H",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1721451396109,
          "user_tz": 420,
          "elapsed": 4,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "3cf7c558-ee0d-4bdd-b119-616f9775c867"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing tasks.py\n"
          ]
        }
      ],
      "source": [
        "%%file tasks.py\n",
        "import pytest\n",
        "\n",
        "tasks = []\n",
        "\n",
        "def add_task(task):\n",
        "    tasks.append(task)\n",
        "    return tasks\n",
        "\n",
        "def remove_task(task):\n",
        "    if task in tasks:\n",
        "        tasks.remove(task)\n",
        "        return tasks\n",
        "    else:\n",
        "        return \"Task not found.\"\n",
        "\n",
        "def list_tasks():\n",
        "    return tasks\n",
        "\n",
        "def clear_tasks():\n",
        "    tasks.clear()\n",
        "    return \"Tasks cleared.\"\n",
        "\n",
        "# Tests\n",
        "def test_add_task():\n",
        "    # Clear the tasks list before testing\n",
        "    clear_tasks()\n",
        "    assert add_task(\"Task 1\") == [\"Task 1\"]\n",
        "    assert add_task(\"Task 2\") == [\"Task 1\", \"Task 2\"]\n",
        "    assert add_task(\"Task 3\") == [\"Task 1\", \"Task 2\", \"Task 3\"]\n",
        "\n",
        "def test_remove_task():\n",
        "    # Clear the tasks list and add tasks for testing\n",
        "    clear_tasks()\n",
        "    add_task(\"Task 1\")\n",
        "    add_task(\"Task 2\")\n",
        "    add_task(\"Task 3\")\n",
        "\n",
        "    # Test removing existing tasks\n",
        "    assert remove_task(\"Task 2\") == [\"Task 1\", \"Task 3\"]\n",
        "    assert remove_task(\"Task 1\") == [\"Task 3\"]\n",
        "\n",
        "    # Test removing non-existent task\n",
        "    assert remove_task(\"Task 4\") == \"Task not found.\"\n",
        "    assert remove_task(\"Task 3\") == []\n",
        "\n",
        "def test_list_tasks():\n",
        "    # Clear the tasks list before testing\n",
        "    clear_tasks()\n",
        "\n",
        "    # Test listing tasks when list is empty\n",
        "    assert list_tasks() == []\n",
        "\n",
        "    # Add tasks and test listing\n",
        "    add_task(\"Task 1\")\n",
        "    add_task(\"Task 2\")\n",
        "    assert list_tasks() == [\"Task 1\", \"Task 2\"]\n",
        "\n",
        "def test_clear_tasks():\n",
        "    # Clear the tasks list before testing\n",
        "    clear_tasks()\n",
        "\n",
        "    # Add tasks for testing\n",
        "    add_task(\"Task 1\")\n",
        "    add_task(\"Task 2\")\n",
        "\n",
        "    # Test clearing tasks\n",
        "    assert clear_tasks() == \"Tasks cleared.\"\n",
        "    assert list_tasks() == []\n",
        "\n",
        "# Additional edge case tests\n",
        "def test_add_empty_task():\n",
        "    # Clear the tasks list before testing\n",
        "    clear_tasks()\n",
        "    assert add_task(\"\") == [\"\"]\n",
        "\n",
        "def test_remove_from_empty_list():\n",
        "    # Clear the tasks list before testing\n",
        "    clear_tasks()\n",
        "    assert remove_task(\"Non-existent task\") == \"Task not found.\"\n",
        "\n",
        "def test_add_duplicate_tasks():\n",
        "    # Clear the tasks list before testing\n",
        "    clear_tasks()\n",
        "    assert add_task(\"Task 1\") == [\"Task 1\"]\n",
        "    assert add_task(\"Task 1\") == [\"Task 1\", \"Task 1\"]\n",
        "    assert add_task(\"Task 2\") == [\"Task 1\", \"Task 1\", \"Task 2\"]\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pytest tasks.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vbidqLTR7a1T",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1721451416884,
          "user_tz": 420,
          "elapsed": 751,
          "user": {
            "displayName": "Laurence Moroney",
            "userId": "17858265307580721507"
          }
        },
        "outputId": "25344ef7-a069-4e3c-ccdc-33082b78e003"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001B[1m======================================= test session starts ========================================\u001B[0m\n",
            "platform linux -- Python 3.10.12, pytest-7.4.4, pluggy-1.5.0\n",
            "rootdir: /content\n",
            "plugins: anyio-3.7.1\n",
            "\u001B[1mcollecting ... \u001B[0m\u001B[1m\rcollected 7 items                                                                                  \u001B[0m\n",
            "\n",
            "tasks.py \u001B[32m.\u001B[0m\u001B[32m.\u001B[0m\u001B[32m.\u001B[0m\u001B[32m.\u001B[0m\u001B[32m.\u001B[0m\u001B[32m.\u001B[0m\u001B[32m.\u001B[0m\u001B[32m                                                                             [100%]\u001B[0m\n",
            "\n",
            "\u001B[32m======================================== \u001B[32m\u001B[1m7 passed\u001B[0m\u001B[32m in 0.03s\u001B[0m\u001B[32m =========================================\u001B[0m\n"
          ]
        }
      ]
    }
  ]
}