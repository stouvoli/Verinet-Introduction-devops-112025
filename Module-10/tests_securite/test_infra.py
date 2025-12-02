import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import socket

# 1. Liaison avec le fichier Gherkin
scenarios('securite.feature')

# 2. Fixture pour stocker les résultats (C'est juste une boîte vide au début)
@pytest.fixture
def context():
    return {}

# 3. Les étapes du test (Elles doivent être en dehors de la fixture context)

@given(parsers.parse('L\'adresse cible est "{host}"'))
def target_host(context, host):
    context['host'] = host

@when(parsers.parse('Je scanne le port {port:d}'))
def check_port(context, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # Timeout rapide (1 seconde)
    
    # connect_ex renvoie 0 si la connexion réussit (port ouvert)
    result = sock.connect_ex((context['host'], port))
    
    context['status'] = "open" if result == 0 else "closed"
    sock.close()

@then(parsers.parse('Le port doit être "{expected_state}"'))
def verify_state(context, expected_state):
    assert context['status'] == expected_state