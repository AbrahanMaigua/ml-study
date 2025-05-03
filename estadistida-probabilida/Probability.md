Thanks! Here’s the full transcription of the content from the new screenshot:

---

### **Probability of an event "A"**
$$
P(A) = \frac{\# \text{ ways A can happen}}{\# \text{ of things that can happen}}
$$
---

### **Example (Left): I flip a coin twice**
$$
Ω ={hh,ht,th,tt}\Omega = \{hh, ht, th, tt\}
$$
1. **A = at least one heads**
    
$$
A={hh,ht,th}⇒P(A)=34=75%A = \{hh, ht, th\} \quad \Rightarrow \quad P(A) = \frac{3}{4} = 75\%
$$
2. **B = no heads**
    
$$
B={tt}⇒P(B)=14=25%B = \{tt\} \quad \Rightarrow \quad P(B) = \frac{1}{4} = 25\%
$$
---

### **Example (Right): I roll two dice**

**1. Probability at least one die is a 5?**
$$
Ω={11,12,13,14,15,...,66}\Omega = \{11, 12, 13, 14, 15, ..., 66\} A={15,25,35,45,51,52,53,54,55,56,65}A = \{15, 25, 35, 45, 51, 52, 53, 54, 55, 56, 65\} P(A)=1136P(A) = \frac{11}{36}
$$
Diagram shows branching tree (sample space visualization)

At bottom:
$$
16+56⋅16=P(A)=P(D1=5)+P(D1≠5)⋅P(D2=5)\frac{1}{6} + \frac{5}{6} \cdot \frac{1}{6} = P(A) = P(D_1 = 5) + P(D_1 \neq 5) \cdot P(D_2 = 5)

---
$$



### 📌 ** Ejemplos de conteo de casos**

#### 🪙 **Ejemplo: secuencia de 10 lanzamientos de moneda**

- Cada lanzamiento tiene 2 resultados posibles (cara o cruz).
    
- Como se permite repetir (with replacement), el total de secuencias es:
    
$$
2102^{10}
$$
#### 🃏 **Ejemplo: Baraja de 52 cartas – 5 cartas sin reemplazo**

- Se toman 5 cartas una tras otra sin volver a ponerlas (without replacement).
    
- El número de combinaciones posibles:
    
$$
52!(52−5)!=52!47!\frac{52!}{(52 - 5)!} = \frac{52!}{47!}
$$
Esto es una **permutación**, ya que el orden sí importa.

---

### 📌 **Fórmulas clave**

#### 🟣 Permutaciones con reemplazo (cuando el orden importa):
$$
nrn^r
$$
donde:

- nn: número de opciones por posición.
    
- rr: número de posiciones.
    

#### 🔵 Permutaciones sin reemplazo:

$$
n!(n−r)!\frac{n!}{(n - r)!}
$$
#### 🟢 Combinaciones (cuando el orden NO importa):

$$
n!(n−r)!r!=(nr)\frac{n!}{(n - r)!r!} = \binom{n}{r}
$$
---

### 📌 **Ejemplo de placas de carro (License Plates)**

- Supone que hay letras y números, y se puede calcular el total de placas posibles combinando ambos grupos.
    

