import pytest
from myblog import app, db
from myblog.models.user import User
from myblog.models.post import Post

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["WTF_CSRF_ENABLED"] = False
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

# prueba 1 - el index carga correctamente
def test_index_carga(client):
    response = client.get("/")
    assert response.status_code == 200

# prueba 2 - registro de usuario nuevo
def test_registro_usuario(client):
    response = client.post("/user/register", data={
        "username": "testuser",
        "password": "1234"
    })
    assert response.status_code in [200, 302]

# prueba 3 - login con usuario inexistente retorna 401
def test_login_usuario_inexistente(client):
    response = client.post("/user/login", data={
        "username": "noexiste",
        "password": "1234"
    })
    assert response.status_code == 401

# prueba 4 - login con contraseña incorrecta retorna 401
def test_login_contraseña_incorrecta(client):
    client.post("/user/register", data={
        "username": "testuser",
        "password": "1234"
    })
    response = client.post("/user/login", data={
        "username": "testuser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401

# prueba 5 - crear post sin autenticacion redirige al login
def test_crear_post_sin_autenticacion(client):
    response = client.get("/blog/create")
    assert response.status_code == 302

# prueba 6 - health check retorna ok
def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200