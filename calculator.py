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
    
    def multiplicacao(self, a, b):
        if a is None or b is None:
            return None
        elif not (isinstance(a, (int, float)) and isinstance (b, (int, float))):
            return None
        else:
            resultado = a * b
            return resultado
    
    def divisao(self, a, b):
        if a is None or b is None:
            return None
        elif not (isinstance(a, (int, float)) and isinstance (b, (int, float))):
            return None
        elif b == 0:
            return None
        else:
            resultado = a / b
            return resultado
        
    
    def potencia(self):
        return
    
    def raiz_quadrada(self):
        return
    
    def fatorial(self):
        return
    
    def resto_divisao(self):
        return 
    
    
    
        