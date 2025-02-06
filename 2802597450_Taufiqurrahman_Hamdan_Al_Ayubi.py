{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOGL8DjoI209B6ku5gpeHjX",
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
        "<a href=\"https://colab.research.google.com/github/Hamdanay/scientific-computing/blob/main/2802597450_Taufiqurrahman_Hamdan_Al_Ayubi.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
      "execution_count": null,
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