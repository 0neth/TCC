import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon , QFont
from PyQt5.QtCore import Qt

class JanelaProdutos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar produtos")
        self.setGeometry(30,30,700,600)
        self.nome_produto = QLabel("Nome",self)
        self.nome_produto_line = QLineEdit(self)
        self.preco = QLabel("Preco",self)
        self.preco_line = QLineEdit(self)
        self.peso = QLabel("Peso",self)
        self.peso_line = QLineEdit(self)
        self.validade = QLabel("Validade",self)
        self.validade_line = QLineEdit(self)
        self.marca = QLabel("Marca",self)
        self.marca_line = QLineEdit(self)
        #self.estoque = QLabel("Estoque",self)
        
        #self.codigo_barras = QLabel("Codigo de barras", self)
        self.botao_registrar = QPushButton("Registrar",self)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.nome_produto_line.setPlaceholderText("nome")
        self.preco_line.setPlaceholderText("preco")
        self.peso_line.setPlaceholderText("peso")
        self.validade_line.setPlaceholderText("validade")
        self.marca_line.setPlaceholderText("marca")

        GridLayout = QGridLayout()
        GridLayout.addWidget(self.nome_produto,0,0)
        GridLayout.addWidget(self.nome_produto_line,1,0)
        GridLayout.addWidget(self.preco,0,2)
        GridLayout.addWidget(self.preco_line,1,2)
        GridLayout.addWidget(self.peso,0,3)
        GridLayout.addWidget(self.peso_line,1,3)
        GridLayout.addWidget(self.validade,0,4)
        GridLayout.addWidget(self.validade_line,1,4)
        GridLayout.addWidget(self.marca,0,5)
        GridLayout.addWidget(self.marca_line,1,5)

        GridLayout.addWidget(self.botao_registrar,1,6)
        
        central_widget.setLayout(GridLayout)

        self.setStyleSheet(""" 
            QLineEdit{
                font-size: 20px;
                font-family: Arial;
                padding: 0px 25px;
                margin: 5px;
                border: 3px solid;
                border-radius: 15px;
            }
            QLabel{
                font-size:25px;
                font-family-Arial;
                padding:  0px 15px;
                ;
                margin: 10px;
                border: 1px solid;
            }
        """)
        
        self.botao_registrar.setGeometry(0,0,200,50)
        self.botao_registrar.clicked.connect(self.on_click)

        
        
    def on_click(self):
        print("button clicked")
        self.botao_registrar.setText("Registrando...")
        self.botao_registrar.setDisabled(True)
    

    
def main():
    app = QApplication(sys.argv)
    window = JanelaProdutos()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main() 
    