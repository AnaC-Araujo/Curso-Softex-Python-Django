from perecivel import Perecivel

def test_heranca_perecivel():
    pere = Perecivel("Agua com gas", 5, 2.0, "27/11/2025")
    assert pere.nome == "Agua com gas"
    assert pere.quantidade == 5
    assert pere.valor_unitario == 2.0
    assert pere.data_validade == "27/11/2025"
