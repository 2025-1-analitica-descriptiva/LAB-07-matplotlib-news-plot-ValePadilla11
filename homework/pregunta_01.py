"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('files/input/news.csv', index_col=0)

    os.makedirs('files/plots', exist_ok=True)

    plt.figure(figsize=(10, 6))

    for column in df.columns:
        plt.plot(df.index, df[column], marker='o', label=column, linewidth=2)

    plt.title('News Media Usage Over Time', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Usage (%)', fontsize=12)
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig('files/plots/news.png', dpi=300, bbox_inches='tight')
    plt.close()