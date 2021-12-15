class som:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        sum = self.a + self.b
        print(f'soma: {sum}')

        return
    def mul(self):
        mul = self.a * self.b
        print(f'multiplicação: {mul}')

        return
    def div(self):
        div = self.a / self.b
        print(f'divisão: {div}')

        return
    def sub(self):
        sub = self.a - self.b
        print(f'subtração: {sub}')

        return
    def rest(self):
        rest = self.a % self.b
        print(f'resto: {rest}')

        return

    def evy(self):

            sum = self.a + self.b
            print(f'soma: {sum}')

            mul = self.a * self.b
            print(f'multiplicação: {mul}')

            div = self.a / self.b
            print(f'divisão: {div}')

            sub = self.a - self.b
            print(f'subtração: {sub}')

            rest = self.a % self.b
            print(f'resto: {rest}')

            return

    def evy_html(self):

        sum = self.a + self.b
        print(f'soma: {sum}')

        mul = self.a * self.b
        print(f'multiplicação: {mul}')

        div = self.a / self.b
        print(f'divisão: {div}')

        sub = self.a - self.b
        print(f'subtração: {sub}')

        rest = self.a % self.b
        print(f'resto: {rest}')

        html = open('helloworld.html', 'w')

        message = f"""<html>
        <head></head>
        <body>
        <h1>Hello World!</h1>
        <p>Soma: {sum}</p>
        <p>Multiplicação: {mul}</p>
        <p>Divisão: {div}</p>
        <p>Subtração: {sub}</p>
        <p>Resto: {rest}</p>
        </body>
        
        </html>"""

        html.write(message)
        html.close()