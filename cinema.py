"""Lógica principal del sistema de cine."""
from typing import Dict, List, Tuple
from models import Reserva, CinemaState
from utils import validar_numero, formatear_precio, mostrar_banner, validar_confirmacion
from data import PELICULAS

class  CinemaManager:
    """Gestor principal del cine."""
    
    def __init__(self):
        self.state = CinemaState(PELICULAS.copy(), [])
    
    def mostrar_menu_peliculas(self) -> None:
        """Muestra menú de películas disponibles."""
        mostrar_banner("🎬 PELÍCULAS DISPONIBLES")
        for i, pelicula in enumerate(self.state.peliculas, 1):
            horarios = list(self.state.peliculas[pelicula]["horarios"].keys())
            print(f"  {i:2d} - {pelicula} ({len(horarios)} horarios)")
    
    def seleccionar_pelicula(self) -> str:
        """Selecciona película validando entrada."""
        idx = validar_numero(1, len(self.state.peliculas), "Película: ")
        return list(self.state.peliculas.keys())[idx - 1]
    
    def seleccionar_horario(self, pelicula: str) -> str:
        """Selecciona horario de película específica."""
        horarios = list(self.state.peliculas[pelicula]["horarios"].keys())
        mostrar_banner(f"Horarios - {pelicula}")
        
        for i, horario in enumerate(horarios, 1):
            boletos = self.state.peliculas[pelicula]["horarios"][horario]
            print(f"  {i:2d} - {horario} ({boletos} disponibles)")
        
        idx = validar_numero(1, len(horarios), "Horario: ")
        return horarios[idx - 1]
    
    def procesar_reserva(self) -> bool:
        """Procesa una reserva completa."""
         # Selección (ya validada)
        self.mostrar_menu_peliculas()
        pelicula = self.seleccionar_pelicula()
        horario = self.seleccionar_horario(pelicula)
        
        # Validar boletos (ya validado)
        max_boletos = self.state.peliculas[pelicula]["horarios"][horario]
        cantidad = validar_numero(1, max_boletos, f"Cantidad (max {max_boletos}): ")
        
        # Cálculo
        precio = self.state.peliculas[pelicula]["precio"]
        subtotal = cantidad * precio
        
        # Confirmación REFACTORIZADA (2 líneas)
        mostrar_banner("RESUMEN COMPRA")
        print(f"Película: {pelicula}\nHorario: {horario}\nCantidad: {cantidad}")
        print(f"Precio: {formatear_precio(precio)}\nSUBTOTAL: {formatear_precio(subtotal)}")
        
        # 🔧 NUEVA FUNCIÓN - 1 LÍNEA
        if validar_confirmacion("¿Confirmar reserva? (s/n): "):
            # Guardar reserva
            reserva = Reserva(pelicula, horario, cantidad, precio, subtotal)
            self.state.reservas.append(reserva)
            self.state.costo_total += subtotal
            self.state.peliculas[pelicula]["horarios"][horario] -= cantidad
            print("✅ ¡Reserva confirmada!")
            return True
        else:
            print("❌ Reserva cancelada")
            return False

    def mostrar_resumen(self) -> None:
        """Muestra resumen final de reservas."""
        mostrar_banner("📋 RESUMEN FINAL")
        if self.state.reservas:
            for i, reserva in enumerate(self.state.reservas, 1):
                print(f"{i:2d}. {reserva.pelicula} - {reserva.horario}")
                print(f"    {reserva.cantidad} × {formatear_precio(reserva.precio_unitario)}")
                print(f"    Subtotal: {formatear_precio(reserva.subtotal)}")
            print("-" * 50)
            print(f"TOTAL: {formatear_precio(self.state.costo_total)}")
        else:
            print("No hay reservas realizadas")
