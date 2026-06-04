from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_listar_tarefa_vazia():
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert response.json() == []

def test_criar_tarefa():
    response = client.post(
        "/tarefas",
        json={"titulo": "Estudar FastAPI"}
    )
    
    data = response.json()
    assert data["titulo"] == "Estudar FastAPI"
    assert data ["concluida"] == False
    assert "id" in data 
    
    def test_tarefa_nao_encontrada():
        response = client.get("/tarefa/9999")
        
        assert response.status_code == 404
        assert response.json()["detail"] == "Tarefa não encontrada"
        
        