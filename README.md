# App-Budger-FCC
<h1 align="center">💰 Aplicación de Presupuesto</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/freeCodeCamp-0A0A23?style=for-the-badge&logo=freecodecamp&logoColor=white" alt="freeCodeCamp"/>
  <img src="https://img.shields.io/badge/Tests-24%2F24%20✓-2ea043?style=for-the-badge" alt="Tests"/>
</p>

<p align="center"><i>Programación Orientada a Objetos · Certificación de Python</i></p>

---

## 🎯 Objetivo

> Construir una aplicación de presupuesto que rastree el gasto en diferentes categorías mediante una clase `Category` y una función `create_spend_chart` que genera un gráfico de barras con el porcentaje relativo de gasto.

---

## 📋 Descripción

La aplicación permite crear **categorías de presupuesto** (como Food, Clothing, Auto), realizar depósitos, retiros y transferencias entre ellas. Cada categoría mantiene un **ledger** (libro de registros) con todas las transacciones.

Además, incluye una función que genera un **gráfico de barras vertical** mostrando el porcentaje gastado por categoría, con los nombres escritos verticalmente debajo de las barras.

---

## ▶️ Uso

```python
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```

---

## 📥 Ejemplo de salida

### 📒 Imprimir categoría
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

### 📊 Gráfico de gasto
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

---

## 🔧 Clase y funciones

| Elemento | Tipo | Descripción |
|----------|------|-------------|
| `Category(name)` | Clase | 🏷️ Crea una categoría de presupuesto con un nombre y un ledger vacío |
| `deposit(amount, description)` | Método | 💵 Agrega un depósito al ledger |
| `withdraw(amount, description)` | Método | 💸 Registra un retiro (monto negativo) si hay fondos suficientes |
| `get_balance()` | Método | 💰 Devuelve el balance actual basado en el ledger |
| `transfer(amount, category)` | Método | 🔄 Transfiere fondos a otra categoría |
| `check_funds(amount)` | Método | ✅ Verifica si hay fondos suficientes |
| `__str__()` | Método | 🖨️ Devuelve la representación en cadena de la categoría |
| `create_spend_chart(categories)` | Función | 📊 Genera un gráfico de barras con porcentajes de gasto |

---

## 📏 Reglas de formato

### 🖨️ Representación de categoría (`__str__`)

| Elemento | Regla |
|----------|-------|
| Título | 30 caracteres, nombre centrado entre `*` |
| Descripción | Máximo 23 caracteres, alineada a la izquierda |
| Monto | Máximo 7 caracteres, 2 decimales, alineado a la derecha |
| Total | `Total: [balance]` al final |

### 📊 Gráfico de gasto (`create_spend_chart`)

| Elemento | Regla |
|----------|-------|
| Título | `Percentage spent by category` |
| Porcentajes | Solo retiros, redondeados hacia abajo al múltiplo de 10 |
| Eje Y | De `100` a `0` en pasos de 10, alineados a la derecha |
| Barras | Carácter `o`, separadas por 2 espacios entre categorías |
| Línea horizontal | 3 guiones `-` por categoría, más 1 adicional |
| Nombres | Escritos verticalmente, misma longitud en cada línea |

---

## 💡 Conceptos clave aplicados

- **Programación Orientada a Objetos**: clases, métodos de instancia, `__str__`, atributos de instancia.
- **Construcción de strings vs impresión directa**: construir líneas como strings y almacenarlas en una lista para reutilización (patrón espejo).
- **Formateo con f-strings**: alineación con `{i:3}`, decimales con `:.2f`.
- **Bucles anidados**: recorrer categorías y sus entradas de ledger para calcular totales.
- **`"\n".join(lista)`**: unir líneas para retornar un solo string desde `__str__` y `create_spend_chart`.

---

## ✅ Historias de usuario

- [x] 🏷️ Clase `Category` con atributo `ledger` como lista de transacciones.
- [x] 💵 Método `deposit` agrega objetos al ledger con `amount` y `description`.
- [x] 💸 Método `withdraw` almacena montos negativos y devuelve `True`/`False`.
- [x] 💰 Método `get_balance` devuelve el balance actual.
- [x] 🔄 Método `transfer` retira de una categoría y deposita en otra.
- [x] ✅ Método `check_funds` valida fondos antes de retiros y transferencias.
- [x] 🖨️ `__str__` muestra título, transacciones formateadas y total.
- [x] 📊 `create_spend_chart` genera gráfico con porcentajes correctos.
- [x] 📏 Todas las líneas del gráfico tienen la misma longitud.
- [x] ✍️ Nombres de categorías escritos verticalmente con espaciado exacto.

---

## 🧪 Tests

| # | Estado | Descripción |
|:-:|:------:|:------------|
| 1 | ✔️ | El método `deposit` debe crear un objeto específico en el ledger |
| 2 | ✔️ | `deposit` sin descripción debe crear una descripción en blanco |
| 3 | ✔️ | El método `withdraw` debe crear un objeto específico en el ledger |
| 4 | ✔️ | `withdraw` sin descripción debe crear una descripción en blanco |
| 5 | ✔️ | `withdraw` debe devolver `True` si la retirada se realizó |
| 6 | ✔️ | `deposit(900)` y `withdraw(45.67)` debe devolver saldo de `854.33` |
| 7 | ✔️ | `transfer` debe crear un artículo específico del ledger |
| 8 | ✔️ | `transfer` debe devolver `True` si la transferencia se realizó |
| 9 | ✔️ | `transfer` debe reducir el saldo en la categoría de origen |
| 10 | ✔️ | `transfer` debe aumentar el saldo en la categoría de destino |
| 11 | ✔️ | `transfer` debe crear un artículo en la categoría de destino |
| 12 | ✔️ | `check_funds` debe devolver `False` si el monto excede el saldo |
| 13 | ✔️ | `check_funds` debe devolver `True` si el monto no excede el saldo |
| 14 | ✔️ | `withdraw` debe devolver `False` si no se realizó |
| 15 | ✔️ | `transfer` debe devolver `False` si no se realizó |
| 16 | ✔️ | Imprimir `Category` debe dar representación de cadena correcta |
| 17 | ✔️ | Título del gráfico: `Percentage spent by category` |
| 18 | ✔️ | Porcentajes correctos a la izquierda |
| 19 | ✔️ | Barras redondeadas hacia abajo al 10 más cercano |
| 20 | ✔️ | Todas las líneas con la misma longitud y espaciado correcto |
| 21 | ✔️ | Línea horizontal correcta debajo de las barras |
| 22 | ✔️ | Sin carácter de nueva línea al final |
| 23 | ✔️ | Nombres verticales con espaciado correcto |
| 24 | ✔️ | Espaciado exacto en todo el gráfico |

---

<p align="center">
  <b>🎉 24 / 24 tests aprobados</b>
</p>
