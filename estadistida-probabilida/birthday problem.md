
### 🧾 Enunciado principal

> _If there are n people in a room, how large does 'n' need to be for at least 50% chance of at least 2 people sharing a birthday?_

(Traducción: Si hay _n_ personas en una sala, ¿cuán grande debe ser _n_ para que haya al menos un 50% de probabilidad de que al menos 2 personas compartan cumpleaños?)

---

### 🧮 Fórmulas importantes

- **Probabilidad de al menos 2 personas compartiendo cumpleaños:**
    $$
    P(≥2 share)=1−P(no shares)P(\geq 2 \text{ share}) = 1 - P(\text{no shares})
    $$
- **Probabilidad de que _nadie_ comparta cumpleaños:**
    $$
        P(no one shares)=365!(365−n)!⋅365nP(\text{no one shares}) = \frac{365!}{(365-n)! \cdot 365^n}
    $$
    
- Para _n = 20_:
    $$
    
    P(no shared)≈0.589P(\text{no shared}) \approx 0.589
    $$

---

### ✅ Resultado clave

> **n = 23** → Probabilidad de cumpleaños compartido ≥ 50%

---

### 🔢 Ejemplo visual destacado (parte inferior derecha):

> Para calcular la cantidad de combinaciones **únicas** de cumpleaños (sin repetidos), se representa:
    $$
\frac{365}{365} \times \frac{364}{365} \times \frac{363}{365} \times \dots \times \frac{365 - n + 1}{365}
    $$

Esto es equivalente a:
 $$

365!(365−n)!⋅365n\frac{365!}{(365-n)! \cdot 365^n}
    $$
