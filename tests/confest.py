cat > tests/conftest.py << 'EOF'
import pytest
from django.test import Client

@pytest.fixture
def client():
    return Client()
EOF
