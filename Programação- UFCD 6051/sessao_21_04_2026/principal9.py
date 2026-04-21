#### operações com numeros
IVA_continental = 23
preco_sem_iva = 100
preco_com_iva = 1.23 * preco_sem_iva
preco_com_iva = (1 + IVA_continental / 100) * preco_sem_iva
print (preco_com_iva)