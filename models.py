"""Modelos de datos usando dataclasses."""
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Reserva:
    """Representa una reserva de cine."""
    pelicula: str
    horario: str
    cantidad: int
    precio_unitario: float
    subtotal: float

@dataclass
class CinemaState:
    """Estado global del cine."""
    peliculas: Dict[str, Dict]
    reservas: List[Reserva]
    costo_total: float = 0.0
