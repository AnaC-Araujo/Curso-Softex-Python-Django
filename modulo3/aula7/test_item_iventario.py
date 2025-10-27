from item_iventario import ItemInventario

def test_valor_total_basico():
    item = ItemInventario("Lapis", 10, 2.0)
    assert item.valor_total() == 20.0

def test_valor_total_zero():
    item = ItemInventario("Fichário", 0, 10.0)
    assert item.valor_total() == 0.00