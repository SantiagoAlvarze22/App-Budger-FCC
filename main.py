class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = ''):
        self.ledger.append({
            'amount': amount,
            'description': description
            })

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': - amount,
                'description': description
            })
            return True
        return False

    def get_balance(self):
        amount = 0
        for i in self.ledger:
            amount += i['amount']

        return amount 
    
        
    def check_funds(self, amount):
        return self.get_balance() >= amount

    def transfer(self, amount, o_category):
        if self.check_funds(amount):
            self.withdraw(amount, description=f'Transfer to {o_category.name}')
            o_category.deposit(amount, description=f"Transfer from {self.name}")
            return True
        return False
    
    def __str__(self):
        lista = []
        lista.append(f"{((30 - len(self.name)) // 2) * '*'}{self.name}{((30 - len(self.name)) // 2) * '*'}")
        
        for i in self.ledger:
            
            if len(i['description']) >= 23:
                description = i['description']

                trunc_des = description[:23] + ' '
                
                lista.append(f"{trunc_des}{((30 - (len(trunc_des) + len(str(i['amount']))))-3)* ' '}{i['amount']:.2f}")
            else:
                lista.append(f"{i['description']}{((30 - (len(i['description']) + len(str(i['amount']))))-3)* ' '}{i['amount']:.2f}")
                
        lista.append(f"Total: {self.get_balance()}")

        return "\n".join(lista)


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
# print(food)

auto = Category('Auto')
food.transfer(100, auto)
auto.withdraw(10.89, 'crackers')
clothing.withdraw(28, 'shoes')

# print(auto)
# print(clothing)



def create_spend_chart(categories):
    lista_para_str = []
    total_cantidad_negativos = [] # para sumar el total de los negativos
    categoria_cantidad_nega = [] # para sumar los negativos de cada categoria
    for i in categories:
        suma_negativos = 0 #cada suma inicia en 0
        for j in i.ledger:
            if int(j['amount']) < 0:
                total_cantidad_negativos.append(j['amount'])
                suma_negativos += j['amount']
        categoria_cantidad_nega.append(suma_negativos) 

        #Redondeo
    porcentajes_cat = [(i/sum(total_cantidad_negativos) * 100) // 10 * 10 for i in categoria_cantidad_nega]
    # print(porcentajes_cat)

    #Construcción gráfico
    #Titulo 
    lista_para_str.append('Percentage spent by category')

    for i in range(100,-10,-10):
        linea =f'{i:3}|' #Asigna valores fijos y alinea rellenando los valores hacia la izquierda
        for j in porcentajes_cat:
            if i <= j:
                linea += ' o '
            else:
                linea += '   '
        lista_para_str.append(linea+' ')

    cantidad_categorias = len(categoria_cantidad_nega)

    lista_para_str.append('    '+('-' * (cantidad_categorias* 3)+ ('-')))

    #verifica longitud de las categorias para poder asignar a cada renglon un valor de una letra 
    maxi= []
    for i in categories:
        longitud = len(i.name)
        maxi.append(longitud)
    maximo = max(maxi )
    
    #grafica la cantidad de lineas
    for i in range(maximo):
        linea_2 = '    '
        for j in categories:
            if i >= len(j.name):
                linea_2 += '   '
            else:
                linea_2 += f' {j.name[i]} '
        lista_para_str.append(linea_2+ ' ')
    return '\n'.join(lista_para_str)


print(create_spend_chart([food, clothing, auto]))
