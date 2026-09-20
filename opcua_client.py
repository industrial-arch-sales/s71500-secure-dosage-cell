import asyncio
from asyncua import Client

URL = "opc.tcp://192.168.15.11:4840"
USERNAME = "admin_ot"
PASSWORD = "S71500_SecurePass2026!"

async def main():
    print(f"[*] Conectando ao Servidor OPC UA em {URL}...")
    client = Client(url=URL)
    
    # Ignora divergência de IP no cabeçalho do Endpoint devido ao NAT/PortProxy
    client.check_endpoint_url = False
    
    client.set_user(USERNAME)
    client.set_password(PASSWORD)

    try:
        async with client:
            print("[+] Conexão criptografada e autenticada estabelecida com sucesso!")
            node_state = client.get_node('ns=3;s="DB_Dosagem_Global"."status"."currentState"')
            state_val = await node_state.read_value()
            print(f"[+] Estado Atual da Máquina de Estados (PLC): {state_val}")
    except Exception as e:
        print(f"[-] Erro de Comunicação OPC UA: {type(e).__name__} - {e}")

if __name__ == "__main__":
    asyncio.run(main())
