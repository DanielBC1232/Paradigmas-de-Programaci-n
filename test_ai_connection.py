#!/usr/bin/env python3
"""
Script para probar la conexión con LM Studio
"""
import requests
import json

# Configuración
API_URL = "http://localhost:1234/v1/chat/completions"
MODEL = "meta-llama-3-8b-instruct"

def test_lm_studio_connection():
    """Prueba la conexión con LM Studio"""
    
    print("🔍 Probando conexión con LM Studio...")
    print(f"🌐 URL: {API_URL}")
    print(f"🤖 Modelo: {MODEL}")
    print("-" * 50)
    
    # Test 1: Verificar que el servidor esté ejecutándose
    try:
        models_url = "http://localhost:1234/v1/models"
        response = requests.get(models_url, timeout=5)
        
        if response.status_code == 200:
            print("✅ Servidor LM Studio: FUNCIONANDO")
            models = response.json()
            available_models = [model['id'] for model in models['data']]
            print(f"📋 Modelos disponibles: {available_models}")
            
            if MODEL in available_models:
                print(f"✅ Modelo '{MODEL}': ENCONTRADO")
            else:
                print(f"❌ Modelo '{MODEL}': NO ENCONTRADO")
                print("💡 Modelos disponibles:", available_models)
                return False
        else:
            print(f"❌ Error HTTP: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar a LM Studio")
        print("💡 Asegúrate de que LM Studio esté ejecutándose en localhost:1234")
        return False
    except requests.exceptions.Timeout:
        print("❌ Error: Timeout de conexión")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    
    # Test 2: Probar generación de texto
    print("\n🧪 Probando generación de texto...")
    
    try:
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "Eres un asistente útil que responde en español."},
                {"role": "user", "content": "Responde brevemente: ¿Estás funcionando correctamente?"}
            ],
            "temperature": 0.3,
            "max_tokens": 100,
            "stream": False
        }
        
        response = requests.post(API_URL, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            message = data['choices'][0]['message']['content'].strip()
            print("✅ Generación de texto: FUNCIONANDO")
            print(f"🤖 Respuesta del modelo: '{message}'")
            return True
        else:
            print(f"❌ Error en generación: HTTP {response.status_code}")
            print(f"📄 Respuesta: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Error: El modelo tardó demasiado en responder")
        print("💡 El modelo puede estar cargándose. Intenta de nuevo en unos minutos.")
        return False
    except Exception as e:
        print(f"❌ Error en generación: {e}")
        return False

def show_troubleshooting():
    """Muestra guía de solución de problemas"""
    print("\n" + "="*60)
    print("🛠️  GUÍA DE SOLUCIÓN DE PROBLEMAS")
    print("="*60)
    print()
    print("Si el test falló, verifica lo siguiente:")
    print()
    print("1. 📱 LM Studio está instalado y abierto")
    print("   - Descargar desde: https://lmstudio.ai/")
    print()
    print("2. 🤖 El modelo está descargado")
    print("   - Ir a 'Discover' en LM Studio")
    print("   - Buscar: 'meta-llama-3-8b-instruct'")
    print("   - Descargar el modelo")
    print()
    print("3. 🌐 El servidor está iniciado")
    print("   - Ir a 'Local Server' en LM Studio")
    print("   - Seleccionar el modelo")
    print("   - Hacer clic en 'Start Server'")
    print("   - Verificar: 'Server running on http://localhost:1234'")
    print()
    print("4. 🔥 El firewall no está bloqueando")
    print("   - Permitir conexiones a localhost:1234")
    print()
    print("5. 💾 Suficiente memoria RAM")
    print("   - Llama-3-8B requiere ~8GB de RAM")
    print("   - Considera un modelo más pequeño si tienes menos RAM")

if __name__ == "__main__":
    print("🚀 PRUEBA DE CONEXIÓN CON LM STUDIO")
    print("="*50)
    
    success = test_lm_studio_connection()
    
    if success:
        print("\n🎉 ¡TODO FUNCIONANDO CORRECTAMENTE!")
        print("💡 Tu aplicación de análisis de datos puede usar IA ahora.")
    else:
        print("\n❌ HAY PROBLEMAS DE CONEXIÓN")
        show_troubleshooting()