{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP+l6jq96kZ2Djk3FMtZ1wC",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/FarahhhFatima/FarahhhFatima/blob/main/gc_counter.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8688f1e6"
      },
      "source": [
        "!mkdir -p data"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cae190c1",
        "outputId": "e539972a-d309-4029-9054-42f1dda8fe3d"
      },
      "source": [
        "%%writefile data/example_chr1.fasta\n",
        ">chr1\n",
        "ATGCGCGATATATCGCGCGATATATCGCGCGATATAT"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing data/example_chr1.fasta\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "801c0a86",
        "outputId": "0389813b-1840-494f-82ef-e81fffe69363"
      },
      "source": [
        "def calculate_gc(sequence):\n",
        "    g = sequence.count(\"G\")\n",
        "    c = sequence.count(\"C\")\n",
        "    return ((g + c) / len(sequence)) * 100\n",
        "\n",
        "def read_fasta(file_path):\n",
        "    with open(file_path) as f:\n",
        "        lines = f.readlines()\n",
        "        sequence = \"\".join(line.strip() for line in lines if not line.startswith(\">\"))\n",
        "        return sequence\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    fasta_file = \"data/example_chr1.fasta\"\n",
        "    seq = read_fasta(fasta_file)\n",
        "    gc = calculate_gc(seq)\n",
        "\n",
        "    print(\"Sequence length:\", len(seq))\n",
        "    print(\"GC content: {:.2f}%\".format(gc))"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sequence length: 37\n",
            "GC content: 45.95%\n"
          ]
        }
      ]
    }
  ]
}