# main.py
from database import crear_tablas, obtener_sesion
from models import ResPartner

def crear_partner(nombre: str):
    """Crear un nuevo partner"""
    session = obtener_sesion()
    try:
        nuevo_partner = ResPartner(name=nombre)
        session.add(nuevo_partner)
        session.commit()
        session.refresh(nuevo_partner)
        print(f"✅ Partner creado: {nuevo_partner}")
        return nuevo_partner
    except Exception as e:
        session.rollback()
        print(f"❌ Error al crear partner: {e}")
        return None
    finally:
        session.close()

def listar_partners():
    """Listar todos los partners"""
    session = obtener_sesion()
    try:
        partners = session.query(ResPartner).all()
        print(f"📋 Partners en la base de datos ({len(partners)}):")
        for partner in partners:
            print(f"   - {partner}")
        return partners
    finally:
        session.close()

if __name__ == "__main__":
    crear_tablas()
    crear_partner("Juan Pérez desde main")
    listar_partners()
