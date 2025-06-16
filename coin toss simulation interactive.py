from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import numpy as np
 
class CoinTossSimulator(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Coin Toss Simulator")
        self.tosses = []
 
        self.layout = QVBoxLayout()
        self.label = QLabel("Click 'Toss Coin' to simulate.")
        self.canvas = FigureCanvas(Figure(figsize=(8, 6)))
        self.button = QPushButton("Toss Coin")
 
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.button)
 
        self.setLayout(self.layout)
 
        self.button.clicked.connect(self.toss_coin)
 
        self.ax_bar = self.canvas.figure.add_subplot(211)
        self.ax_pvar = self.canvas.figure.add_subplot(212)
 
    def toss_coin(self):
        toss = np.random.choice([0, 1])
        self.tosses.append(toss)
        n = len(self.tosses)
 
        p_estimate = np.mean(self.tosses)  # p̂ for heads
        p_tail = 1 - p_estimate
        var_p = p_estimate * p_tail / n if n > 0 else 0
 
        self.label.setText(
            f"Tosses: {n} | Heads: {sum(self.tosses)} | p_estimate for heads = {p_estimate:.3f} | Var(p_estimate) = {var_p:.6f}"
        )
 
        self.ax_bar.clear()
        self.ax_pvar.clear()
 
        self.ax_bar.bar(['Tails', 'Heads'], [p_tail, p_estimate], color=['gray', 'skyblue'])
        self.ax_bar.set_ylim(0, 1)
        self.ax_bar.set_ylabel('Estimated Probability')
        self.ax_bar.set_title('Estimated p for Tails and Heads')
 
        x = np.arange(1, n + 1)
        if n > 1:
            p_estimate_arr = np.cumsum(self.tosses) / x
            var_arr = p_estimate_arr * (1 - p_estimate_arr) / x
            self.ax_pvar.plot(x, var_arr, color='orange', label='Var(p_estimate)')
 
        self.ax_pvar.set_title(f'Variance of p_estimate over {n} Tosses')
        self.ax_pvar.set_xlabel('Number of Tosses')
        self.ax_pvar.set_ylabel('Variance')
        self.ax_pvar.legend()
 
        self.canvas.draw()
 
 
def run_app():
    app = QApplication(sys.argv)
    window = CoinTossSimulator()
    window.show()
    sys.exit(app.exec())
 
run_app()
