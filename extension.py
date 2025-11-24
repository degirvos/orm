from sqlalchemy import Column, String, DateTime
from datetime import datetime
from database import crear_tablas, obtener_sesion
from models import ResPartner

class ResPartnerExtendido(ResPartner):
    def saludar(self):
        return f"¡Hola! Soy {self.name} (ID: {self.id})"

    def info_completa(self):
        return f"Partner: {self.name} - ID: {self.id}"

from database import Base
from sqlalchemy import Column, Integer, String, DateTime

class ResPartner(Base):
    __tablename__ = 'res_partner'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    telefono = Column(String(20))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<ResPartner(id={self.id}, name='{self.name}', email='{self.email}')>"
    
    # Métodos adicionales
    def info_extendida(self):
        return f"{self.name} | Email: {self.email} | Tel: {self.telefono}"

# 🔧 FUNCIONES CRUD EXTENDIDAS
def crear_partner_completo(nombre: str, email: str = None, telefono: str = None):
    """Crear un nuevo partner con todos los campos"""
    session = obtener_sesion()
    try:
        nuevo_partner = ResPartner(
            name=nombre,
            email=email,
            telefono=telefono
        )
        session.add(nuevo_partner)
        session.commit()
        session.refresh(nuevo_partner)
        print(f"Partner extendido creado: {nuevo_partner}")
        print(f"Email: {email}")
        print(f"Telefono: {telefono}")
        return nuevo_partner
    except Exception as e:
        session.rollback()
        print(f"❌ Error al crear partner extendido: {e}")
        return None
    finally:
        session.close()

def listar_partners_completos():
    """Listar todos los partners con información extendida"""
    session = obtener_sesion()
    try:
        partners = session.query(ResPartner).all()
        print(f"Partners extendidos en la base de datos ({len(partners)}):")
        for partner in partners:
            print(f"   - {partner.info_extendida()}")
        return partners
    finally:
        session.close()

def actualizar_partner_email(partner_id: int, nuevo_email: str):
    """Actualizar email de un partner"""
    session = obtener_sesion()
    try:
        partner = session.query(ResPartner).filter(ResPartner.id == partner_id).first()
        if partner:
            partner.email = nuevo_email
            session.commit()
            session.refresh(partner)
            print(f"Email actualizado: {partner.info_extendida()}")
            return partner
        else:
            print(f"Partner con ID {partner_id} no encontrado")
            return None
    except Exception as e:
        session.rollback()
        print(f"Error al actualizar email: {e}")
        return None
    finally:
        session.close()

# 🚀 EJEMPLO DE USO DESDE EL NUEVO ARCHIVO
def ejemplo_nuevo_archivo():
    print("EJECUTANDO DESDE NUEVO_ARCHIVO.PY")
    print("=" * 50)
    
    # 1. Crear tablas (esto actualizará la tabla con los nuevos campos)
    crear_tablas()
    print()
    
    # 2. Crear partners con todos los campos
    print("1. CREANDO PARTNERS EXTENDIDOS...")
    partner1 = crear_partner_completo(
        "Ana García", 
        "ana@empresa.com", 
        "+1234567890"
    )
    
    partner2 = crear_partner_completo(
        "Pedro Martínez",
        "pedro@empresa.com", 
        "+0987654321"
    )
    
    partner3 = crear_partner_completo("Carlos Lopez")  # Sin email ni teléfono
    print()
    
    # 3. Listar todos los partners
    print("2. LISTANDO PARTNERS EXTENDIDOS...")
    listar_partners_completos()
    print()
    
    # 4. Actualizar un partner
    print("3. ACTUALIZANDO EMAIL...")
    if partner3:
        actualizar_partner_email(partner3.id, "carlos@nuevoemail.com")
    print()
    
    # 5. Lista final
    print("4. LISTA FINAL...")
    listar_partners_completos()
    print()
    
    print("NUEVO_ARCHIVO.PY COMPLETADO")
    print("=" * 50)

if __name__ == "__main__":
    ejemplo_nuevo_archivo()
