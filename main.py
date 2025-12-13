"""Sistema de gestión de cine - Punto de entrada principal."""
from cinema import CinemaManager
from utils import mostrar_banner

def main():
    """Función principal del programa."""
    manager = CinemaManager()
    
    while True:
        mostrar_banner("🎉 SISTEMA DE GESTIÓN DE CINE")
        print("1. Hacer reserva")
        print("2. Ver resumen") 
        print("3. Salir")
        
        opcion = input("\nOpción: ").strip()
        
        if opcion == "1":
            manager.procesar_reserva()
            # ❌ PROBLEMA: input extra rompe el flujo
            
        elif opcion == "2":
            manager.mostrar_resumen()
            input("Presione Enter para continuar...")  # Pausa opcional
            
        elif opcion == "3":
            manager.mostrar_resumen()
            print("\n¡Gracias por usar el sistema! 🎉")
            break
            
        else:
            print("❌ Opción inválida")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
