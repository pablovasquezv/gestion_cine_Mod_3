```markdown
# 🎬 **CinemaManager** - Sistema de Reservas Cinematográficas


**🎫 Gestor inteligente de reservas de cine** con **validaciones automáticas**, **menús interactivos** y **control de stock en tiempo real**.


---

## 🚀 **Flujo Completo de Funcionamiento**

```
🎬 MENÚ PRINCIPAL → 🎥 PELÍCULA → ⏰ HORARIO → 🎫 CANTIDAD → ✅ CONFIRMAR → 📋 RESUMEN
```

### **1. 🎥 Selección de Películas**
```
🎬 PELÍCULAS DISPONIBLES
  1 - Avengers Endgame (3 horarios)
  2 - Spider-Man: No Way Home (2 horarios)
  3 - Batman (4 horarios)
```

**`mostrar_menu_peliculas()`** → Lista numerada con horarios disponibles

### **2. ⏰ Selección de Horario**
```
Horarios - Avengers Endgame
  1 - 15:00 (120 disponibles)
  2 - 18:30 (80 disponibles) ← STOCK REAL-TIME
  3 - 21:00 (150 disponibles)
```

**`seleccionar_horario(pelicula)`** → Muestra disponibilidad actualizada

### **3. 🎫 Reserva Inteligente**
```
🔥 RESUMEN COMPRA
Película: Avengers Endgame
Horario: 18:30
Cantidad: 2
Precio: $8.500
💰 SUBTOTAL: $17.000

¿Confirmar reserva? (s/n): 
```

**`procesar_reserva()`** → Validación + cálculo + confirmación en 1 flujo

### **4. 📋 Resumen Final**
```
📋 RESUMEN FINAL
 1. Avengers Endgame - 18:30
    2 × $8.500 → Subtotal: $17.000
 2. Batman - 21:00  
    1 × $9.200 → Subtotal: $9.200
──────────────────────────────────
💎 TOTAL: $26.200
```

---

## 🏗️ **Arquitectura Técnica**

| **Método** | **Responsabilidad** | **Validaciones** | **Complejidad** |
|------------|-------------------|------------------|-----------------|
| `mostrar_menu_peliculas()` | Menú numerado | Conteo horarios | 🟢 Simple |
| `seleccionar_pelicula()` | Input 1-N | `validar_numero()` | 🟡 Media |
| `seleccionar_horario()` | Stock real-time | Disponibilidad | 🟡 Media |
| `procesar_reserva()` | **Flujo maestro** | Stock+Precio+Confirm | 🔴 Alta |
| `mostrar_resumen()` | Reporte final | Total acumulado | 🟢 Simple |

### **🔧 Utilidades Críticas**
```
validar_numero(min, max, prompt)     # Input robusto
formatear_precio(precio)             # $12.500 legible
mostrar_banner(titulo)              # 🎬 UI atractiva
validar_confirmacion(prompt)        # s/n inteligente
```



## ✨ **Características Premium**

| ✅ **Validación Automática** | Sin errores de input |
|-----------------------------|---------------------|
| ✅ **Stock Real-Time** | Control inventario |
| ✅ **UI Intuitiva** | Menús numerados |
| ✅ **Cálculos Exactos** | Subtotal + Total |
| ✅ **UX Confirmación** | Revisión previa |
| ✅ **Escalable** | +Películas fácil |



## 📦 **Estructura de Datos**

```
CinemaState(
    peliculas={
        "Avengers": {
            "precio": 8500,
            "horarios": {"15:00": 120, "18:30": 80}
        }
    },
    reservas: [Reserva(pelicula, horario, cantidad, precio, subtotal)],
    costo_total: 0
)
```

🎯 Cómo Usar (5 pasos)
1. cinema = CinemaManager()
2. cinema.mostrar_menu_peliculas()
3. pelicula = cinema.seleccionar_pelicula()
4. cinema.procesar_reserva()  # Flujo completo
5. cinema.mostrar_resumen()
```

---

## 📈 **Demo Interactivo**

```
> Película: 1
> Horario: 2  
> Cantidad (max 80): 2
> ¿Confirmar? s
✅ ¡Reserva confirmada!
```

---

## 🤝 **Contribuciones**

¡Bienvenidas! 🚀  
1. **Fork** el repositorio  
2. Crea **feature branch** (`git checkout -b feature/nueva-pelicula`)  
3. **Commit** tus cambios (`git commit -m 'feat: nueva pelicula'`)  
4. **Push** (`git push origin feature/nueva-pelicula`)  
5. Abre **Pull Request**

## 📄 **Licencia**

[MIT License](LICENSE) - Usa libremente 🎥

## 👨‍💻 **Autor**

**Juan Pablo Vásquez**  
💼 Full Stack Developer | 🎨 Python Specialist  
[vasquezsoftwaresolutions@gmail.com](mailto:vasquezsoftwaresolutions@gmail.com) | [+56 9 7669 5206](tel:+56976695206)

---

*Última actualización: **12-12-2025*** ✨
```

