{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMjtOSM3zJeSktr0iePmKQh",
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
        "<a href=\"https://colab.research.google.com/github/Hamdanay/scientific-computing/blob/main/2802597450_Taufiqurrahman_Hamdan_Al_Ayubi.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7XVtel8iHIJU",
        "outputId": "eed3b2ac-fc89-43bd-9d8d-e13bc7049842"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Thu Feb  6 02:39:44 2025\n"
          ]
        }
      ],
      "source": [
        "import time\n",
        "print(time.ctime())"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "sesi 1"
      ],
      "metadata": {
        "id": "ML0xaSIqIpF2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = 1\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XNOKtxkkJEfQ",
        "outputId": "ee1c360c-d565-4511-dee7-00424a5f603d"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = x + 1\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VvpoB4nhJWeJ",
        "outputId": "bf0f8967-38f1-4ec5-f07d-88264b9a4def"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 1\n",
        "y = x + 1\n",
        "x = 2\n",
        "y"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "icsNZsiRKBSq",
        "outputId": "f05356f2-df54-4fb0-f62b-f1597fae1c88"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "HyEJNIYbKq0b"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x = np.array((1, 4, 3))\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u74hvWyuLQAi",
        "outputId": "0b2bd606-8218-4afa-de3c-2debcf6cf819"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 4, 3])"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = np.array([[1, 4, 3], [9, 2, 7]])\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yHkEQ2NnL9cA",
        "outputId": "61d02ab4-8125-483e-b168-8730e17d1df3"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 4, 3],\n",
              "       [9, 2, 7]])"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_adder(a, b, c):\n",
        "         \"\"\"\n",
        "         function to sum the 3 numbers\n",
        "         input: 3 numbers a, b, c\n",
        "         output: the sum of a, b, and c\n",
        "         author:\n",
        "         date:\n",
        "         \"\"\"\n",
        "\n",
        "         #this is simulation\n",
        "         out = a + b + c\n",
        "\n",
        "         return out"
      ],
      "metadata": {
        "id": "6sAnRKROOVz2"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "my_adder(1, 2, 3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c42eWTlcPoSV",
        "outputId": "ff5e35ba-d249-4437-91eb-f8d88547e21f"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_thermo_stat(temp, desired_temp):\n",
        "  if temp < desired_temp - 5:\n",
        "    status = 'heat'\n",
        "  elif temp > desired_temp + 5:\n",
        "    status = 'AC'\n",
        "  else:\n",
        "    status = 'off'\n",
        "  return status"
      ],
      "metadata": {
        "id": "WssVQx4RQelJ"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "status = my_thermo_stat(65,75)\n",
        "print(status)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4Pj7sYbJRb_3",
        "outputId": "469c97d1-105b-4855-a619-b05b27482125"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "heat\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "status = my_thermo_stat(75,65)\n",
        "print(status)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k9Wvzn53Xuvc",
        "outputId": "3ced560f-5734-4c41-97d7-68d59835bae1"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "AC\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 3\n",
        "if x > 1 and x < 2:\n",
        "  y = 2\n",
        "elif x> 2 and x < 4:\n",
        "  y = 4\n",
        "else:\n",
        "  y = 0\n",
        "print(y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Aa51VLhASxis",
        "outputId": "84b10efd-40f7-4d62-f876-1b9a341628d8"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "val = float(input(\"masukkan nama anda : \"))\n",
        "val"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a1K7TZZqT7wR",
        "outputId": "2302d575-e8ef-4a6a-9dc6-09a2d25f9eb9"
      },
      "execution_count": 30,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "masukkan nama anda : 9\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "9.0"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate(uas, uts, asg):\n",
        "    final_score = (0.5 * uas) + (0.3 * uts) + (0.2 * asg)\n",
        "    return final_score\n",
        "\n",
        "\n",
        "def get_grade(score):\n",
        "    if score >= 80:\n",
        "        return \"A\"\n",
        "    elif score >= 70:\n",
        "        return \"B\"\n",
        "    elif score >= 60:\n",
        "        return \"C\"\n",
        "    elif score >= 50:\n",
        "        return \"D\"\n",
        "    else:\n",
        "        return \"E\"\n",
        "\n",
        "username = input(\"Masukkan Username: \")\n",
        "password = \"\"\n",
        "\n",
        "while password != \"Bn123\":\n",
        "    password = input(\"Masukkan Password: \")\n",
        "    if password != \"Bn123\":\n",
        "        print(\"Password salah! Silakan coba lagi.\")\n",
        "\n",
        "print(\"Login Berhasil!, selamat datang Taufiq\\n\")\n",
        "\n",
        "nama_siswa = input(\"Masukkan Nama Mahasiswa: \")\n",
        "uas = float(input(\"Masukkan Nilai UAS: \"))\n",
        "uts = float(input(\"Masukkan Nilai UTS: \"))\n",
        "asg = float(input(\"Masukkan Nilai ASG: \"))\n",
        "\n",
        "\n",
        "final_score = calculate(uas, uts, asg)\n",
        "grade = get_grade(final_score)\n",
        "\n",
        "# hasil\n",
        "print(\"\\n=== HASIL PERHITUNGAN ===\")\n",
        "print(f\"Nama Mahasiswa: {nama_siswa}\")\n",
        "print(f\"Final Score: {final_score:.2f}\")\n",
        "print(f\"Grade: {grade}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fkyomUnABV7c",
        "outputId": "d97ba631-fcc8-41a9-e4d3-f15f36c1b5f8"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan Username: Taufiq\n",
            "Masukkan Password: Bn123\n",
            "Login Berhasil!, selamat datang Taufiq\n",
            "\n",
            "Masukkan Nama Mahasiswa: budi\n",
            "Masukkan Nilai UAS: 89\n",
            "Masukkan Nilai UTS: 70\n",
            "Masukkan Nilai ASG: 79\n",
            "\n",
            "=== HASIL PERHITUNGAN ===\n",
            "Nama Mahasiswa: budi\n",
            "Final Score: 81.30\n",
            "Grade: A\n"
          ]
        }
      ]
    }
  ]
}
