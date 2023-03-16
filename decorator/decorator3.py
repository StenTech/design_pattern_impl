"""Exemple de décorateur"""

# cette classe affiche un graphique
# et peut enregistrer le graphique en png, svg ou pdf
class plt:
    @staticmethod
    def plot(data):
        print('plot')

    @staticmethod
    def savefig(filename):
        print(f'savefig {filename}')

class Chart:
    def __init__(self, data):
        self.data = data

    def render(self):
        pass

class PNGChartDecorator:
    def __init__(self, chart):
        self.chart = chart

    def render(self):
        self.chart.render()
        plt.savefig('chart.png')

class SVGChartDecorator:
    def __init__(self, chart):
        self.chart = chart

    def render(self):
        self.chart.render()
        plt.savefig('chart.svg')

class PDFChartDecorator:
    def __init__(self, chart):
        self.chart = chart

    def render(self):
        self.chart.render()
        plt.savefig('chart.pdf')

if __name__ == '__main__':
    # Utilisation
    data = [1, 2, 3, 4, 5]
    chart = Chart(data)
    chart = PNGChartDecorator(chart)
    chart = SVGChartDecorator(chart)
    chart = PDFChartDecorator(chart)
    chart.render()
