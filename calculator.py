class Calculator:
    
    def __init__(self) -> None:
        pass
    
    def soma(self, a, b):
        if a is None or b is None:
            return None
        elif not (isinstance(a, (int, float)) and isinstance (b, (int, float))):
            return None
        else:
            resultado = a + b
            return resultado
    
    def subtracao(self, a, b):
        if a is None or b is None:
            return None
        elif not (isinstance(a, (int, float)) and isinstance (b, (int, float))):
            return None
        else:
            resultado = a - b
            return resultado
    
    def multiplicacao(self):
        return
    
    def divisao(self):
        return
    
    def potencia(self):
        return
    
    def raiz_quadrada(self):
        return
    
    def fatorial(self):
        return
    
    def resto_divisao(self):
        return 
    
    
    
        