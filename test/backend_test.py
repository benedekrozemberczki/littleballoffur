from littleballoffur import NetworKitBackEnd, NetworkXBackEnd

def test_networkit_backend():
    backend = NetworKitBackEnd()
    x = backend.get_x()
    assert x == 1

def test_networkx_backend():
    backend = NetworXBackEnd()
    x = backend.get_x()
    assert x == 1
