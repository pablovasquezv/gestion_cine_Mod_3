```markdown
# 🎬 **CinemaManager** - Sistema de Reservas Cinematográficas


**Gestor inteligente de reservas de cine** con validaciones automáticas, menús interactivos y control de stock en tiempo real.

---

## 🚀 **Flujo Completo de Funcionamiento**

```
🎬 MENÚ PRINCIPAL → 🎥 PELÍCULA → ⏰ HORARIO → 🎫 CANTIDAD → ✅ CONFIRMAR → 📋 RESUMEN
```

### **1. 🎥 Selección de Películas**
```
PELÍCULAS DISPONIBLES
  1 - Avengers Endgame (3 horarios)
  2 - Spider-Man (2 horarios)
  3 - Batman (3 horarios)
```

**`mostrar_menu_peliculas()`** → Lista numerada con horarios disponibles

### **2. ⏰ Selección de Horario**
```
Horarios - Avengers Endgame
  1 - 15:00 (120 disponibles)
  2 - 18:30 (80 disponibles)
  3 - 21:00 (150 disponibles)
```

**`seleccionar_horario(pelicula)`** → Muestra stock real-time

### **3. 🎫 Reserva Inteligente**
```
RESUMEN COMPRA
Película: Avengers Endgame
Horario: 18:30
Cantidad: 2
Precio: $8.500
SUBTOTAL: $17.000

¿Confirmar reserva? (s/n): 
```

**`procesar_reserva()`** → Validación automática + cálculo + confirmación

### **4. 📋 Resumen Final**
```
RESUMEN FINAL
 1. Avengers Endgame - 18:30
    2 × $8.500
    Subtotal: $17.000
 2. Batman - 21:00
    1 × $9.200
    Subtotal: $9.200
--------------------------------------------------
TOTAL: $26.200
```

---

## 🛠️ **Arquitectura y Características**

| **Función**                | **Propósito**           | **Validaciones**            |
|----------------------------|-------------------------|-----------------------------|
| `mostrar_menu_peliculas()` | Menú numerado películas | Conteo horarios             |
| `seleccionar_pelicula()`   | Input validado          | 1-N (índices)               |
| `seleccionar_horario()`    | Stock por horario       | Disponibilidad real         |
| `procesar_reserva()`       | Flujo completo          | Stock, precio, confirmación |
| `mostrar_resumen()`        | Reporte final           | Total acumulado             |

### **🔧 Funciones Auxiliares Críticas:**
```
validar_numero(min, max, prompt)  # Input numérico seguro
formatear_precio(precio)          # $12.500 formato
mostrar_banner(titulo)           # 🎬 Encabezados visuales
validar_confirmacion(prompt)     # s/n robusto
```

---

## ✨ **Ventajas del Sistema**

✅ **Validación automática** - Sin errores de input  
✅ **Stock en tiempo real** - Control inventario  
✅ **UI intuitiva** - Menús numerados claros  
✅ **Cálculos precisos** - Subtotales + totales  
✅ **Confirmación** - Usuario revisa antes pagar  
✅ **Escalable** - Fácil agregar películas  

---

## 📦 **Estructura de Datos**

```
CinemaState(
    peliculas={
        "Avengers": {
            "precio": 8500,
            "horarios": {"15:00": 120, "18:30": 80}
        }
    },
    reservas: [Reserva(...)]
)
```

---

## 🎯 **Uso Práctico**

```
1. Ejecutar CinemaManager()
2. Seleccionar película (1-3)
3. Elegir horario disponible
4. Indicar cantidad (≤ stock)
5. Confirmar → Reserva guardada
6. Repetir o ver resumen final
```

**Sistema production-ready** para taquillas digitales - robusto, intuitivo y sin bugs [web:350][web:351].
```
## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para reportar bugs o sugerir mejoras. Envía pull requests para colaborar con nuevas funcionalidades o correcciones.

## 👨‍💻 Autor

**Juan Pablo Vásquez** – Proyecto desarrollado y mantenido.

#### Última actualización: 12-12-2025