import pytest
import main 
@pytest.fixture
def client():
    main.tarefas_db.clear()
    main.proximo_id = 1
    yield TestClient(app)
    main.tarefas_db.clear()
    main.proximo_id = 1