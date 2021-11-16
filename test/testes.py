# TODO: Criar teste que falha quando a entrada é '1.0'

formatar_numero_testes = (
    # ((inteiro, decimal, casas_decimais), padrao, (*entradas))
    ((1, 0, 0), 'br', ('1', '1,0')),
    ((12, 0, 0), 'br', ('12', '12,0')),
    ((123, 0, 0), 'br', ('123', '123,0')),
    ((1, 1, 1), 'br', ('1,1',)),
    ((12, 1, 2), 'br', ('12,01',)),
    ((123, 1, 2), 'br', ('123,01',)),
    ((1234, 1, 2), 'br', ('1234,01', '1.234,01')),
    ((12345, 1, 2), 'br', ('12345,01', '12.345,01')),
    ((123456, 1, 2), 'br', ('123456,01', '123.456,01')),
    ((1234, 0, 0), 'br', ('1234', '1234,0', '1.234,0')),
    ((12345, 0, 0), 'br', ('12345', '12345,0', '12.345,0')),
    ((123456, 0, 0), 'br', ('123456', '123456,0', '123.456,0')),
    ((1, 123, 3), 'br', ('1,123',)),
    ((12, 987, 3), 'br', ('12,987',)),
    ((123, 987, 3), 'br', ('123,987',)),
    ((1234, 98, 2), 'br', ('1234,98', '1.234,98')),
    ((12345, 9, 1), 'br', ('12345,9', '12.345,9')),
    ((123456, 1, 1), 'br', ('123456,1', '123.456,1')),
    ((1023456, 1, 1), 'br', ('1023456,1', '1.023.456,1')),
    ((11023456, 1, 1), 'br', ('11023456,1', '11.023.456,1')),
    ((115023456, 1, 1), 'br', ('115023456,1', '115.023.456,1')),
    ((1815023456, 1, 1), 'br', ('1815023456,1', '1.815.023.456,1')),

    ((1, 0, 0), 'us', ('1', '1.0')),
    ((12, 0, 0), 'us', ('12', '12.0')),
    ((123, 0, 0), 'us', ('123', '123.0')),

    ((1, 1, 1), 'us', ('1.1',)),
    ((12, 1, 2), 'us', ('12.01',)),
    ((123, 1, 2), 'us', ('123.01',)),
    ((1234, 1, 2), 'us', ('1234.01', '1,234.01')),
    ((12345, 1, 2), 'us', ('12345.01', '12,345.01')),
    ((123456, 1, 2), 'us', ('123456.01', '123,456.01')),

    ((1234, 0, 0), 'us', ('1234', '1234.0', '1,234.0')),
    ((12345, 0, 0), 'us', ('12345', '12345.0', '12,345.0')),
    ((123456, 0, 0), 'us', ('123456', '123456.0', '123,456.0')),
    ((1, 123, 3), 'us', ('1.123',)),
    ((12, 987, 3), 'us', ('12.987',)),
    ((123, 987, 3), 'us', ('123.987',)),
    ((1234, 98, 2), 'us', ('1234.98', '1,234.98')),
    ((12345, 9, 1), 'us', ('12345.9', '12,345.9')),
    ((123456, 1, 1), 'us', ('123456.1', '123,456.1')),
    ((1023456, 1, 1), 'us', ('1023456.1', '1,023,456.1')),
    ((11023456, 1, 1), 'us', ('11023456.1', '11,023,456.1')),
    ((115023456, 1, 1), 'us', ('115023456.1', '115,023,456.1')),
    ((1815023456, 1, 1), 'us', ('1815023456.1', '1,815,023,456.1')),
)

real_fracoes_testes = (
    # (por_extenso, padrao, (*valores))
    ('zero', 'br', ('0', '0,0')),

    ('um décimo', 'br', ('0,1',)),  # 1 casa decimal
    ('três décimos', 'br', ('0,3',)),
    ('seis décimos', 'br', ('0,6',)),
    ('nove décimos', 'br', ('0,9',)),

    ('dois centésimos', 'br', ('0,02',)),
    ('um centésimo', 'br', ('0,01',)),  # 2 casas decimais
    ('três centésimos', 'br', ('0,03',)),
    ('seis centésimos', 'br', ('0,06',)),
    ('nove centésimos', 'br', ('0,09',)),
    ('onze centésimos', 'br', ('0,11',)),
    ('quarenta e um centésimos', 'br', ('0,41',)),
    ('cinquenta e três centésimos', 'br', ('0,53',)),
    ('oitenta e seis centésimos', 'br', ('0,86',)),

    ('um milésimo', 'br', ('0,001',)),  # 3 casas decimais
    ('três milésimos', 'br', ('0,003',)),
    ('seis milésimos', 'br', ('0,006',)),
    ('nove milésimos', 'br', ('0,009',)),
    ('onze milésimos', 'br', ('0,011',)),
    ('quarenta e um milésimos', 'br', ('0,041',)),
    ('cinquenta e três milésimos', 'br', ('0,053',)),
    ('oitenta e seis milésimos', 'br', ('0,086',)),
    ('cento e um milésimos', 'br', ('0,101',)),
    ('quatrocentos e três milésimos', 'br', ('0,403',)),
    ('setecentos e seis milésimos', 'br', ('0,706',)),
    ('cento e vinte e um milésimos', 'br', ('0,121',)),
    ('quatrocentos e cinquenta e três milésimos', 'br', ('0,453',)),
    ('setecentos e oitenta e seis milésimos', 'br', ('0,786',)),

    ('um décimo de milésimo', 'br', ('0,0001',)),  # 4 casas decimais
    ('três décimos de milésimo', 'br', ('0,0003',)),
    ('seis décimos de milésimo', 'br', ('0,0006',)),
    ('nove décimos de milésimo', 'br', ('0,0009',)),

    ('vinte e um décimos de milésimo', 'br', ('0,0021',)),
    ('cento e cinquenta e três décimos de milésimo', 'br', ('0,0153',)),
    ('quatrocentos e cinquenta e seis décimos de milésimo', 'br', ('0,0456',)),
    ('setecentos e oitenta e nove décimos de milésimo', 'br', ('0,0789',)),
    ('onze décimos de milésimo', 'br', ('0,0011',)),
    ('quarenta e um décimos de milésimo', 'br', ('0,0041',)),
    ('cinquenta e três décimos de milésimo', 'br', ('0,0053',)),
    ('oitenta e seis décimos de milésimo', 'br', ('0,0086',)),

    ('quarenta e um décimos de milésimo', 'br', ('0,0041',)),
    ('três mil e cinquenta e três décimos de milésimo', 'br', ('0,3053',)),
    ('seis mil e oitenta e seis décimos de milésimo', 'br', ('0,6086',)),
    ('nove mil cento e um décimos de milésimo', 'br', ('0,9101',)),
    ('dois mil quatrocentos e três décimos de milésimo', 'br', ('0,2403',)),
    ('cinco mil setecentos e seis décimos de milésimo', 'br', ('0,5706',)),
    ('oito mil cento e vinte e um décimos de milésimo', 'br', ('0,8121',)),
    ('um mil quatrocentos e cinquenta e três décimos de milésimo', 'br', ('0,1453',)),
    ('três mil setecentos e oitenta e seis décimos de milésimo', 'br', ('0,3786',)),

    ('um centésimo de milésimo', 'br', ('0,00001',)),  # 5 casas decimais
    ('dois centésimos de milésimo', 'br', ('0,00002',)),

    ('um milionésimo', 'br', ('0,000001',)),  # 6 casas decimais
    ('três milionésimos', 'br', ('0,000003',)),

    ('um décimo de milionésimo', 'br', ('0,0000001',)),  # 7 casas decimais
    ('quatro décimos de milionésimo', 'br', ('0,0000004',)),

    ('um centésimo de milionésimo', 'br', ('0,00000001',)),  # 8 casas decimais
    ('cinco centésimos de milionésimo', 'br', ('0,00000005',)),

    ('um bilionésimo', 'br', ('0,000000001',)),  # 9 casas decimais
    ('seis bilionésimos', 'br', ('0,000000006',)),

    ('um décimo de bilionésimo', 'br', ('0,0000000001',)),  # 10 casas decimais
    ('sete décimos de bilionésimo', 'br', ('0,0000000007',)),

    ('um centésimo de bilionésimo', 'br', ('0,00000000001',)),  # 11 casas decimais
    ('setenta centésimos de bilionésimo', 'br', ('0,00000000070',)),

    ('um trilionésimo', 'br', ('0,000000000001',)),  # 12 casas decimais
    ('setecentos e um trilionésimos', 'br', ('0,000000000701',)),

    ('um décimo de trilionésimo', 'br', ('0,0000000000001',)),  # 13 casas decimais
    ('setecentos e um décimos de trilionésimo', 'br', ('0,0000000000701',)),

    ('um centésimo de trilionésimo', 'br',
     ('0,00000000000001',)),  # 14 casas decimais
    ('setecentos e um centésimos de trilionésimo', 'br', ('0,00000000000701',)),

    ('um quatrilionésimo', 'br', ('0,000000000000001',)),  # 15 casas decimais
    ('sete mil e doze quatrilionésimos', 'br', ('0,000000000007012',)),

    ('um décimo de quatrilionésimo', 'br',
     ('0,0000000000000001',)),  # 16 casas decimais
    ('sete mil e doze décimos de quatrilionésimo', 'br', ('0,0000000000007012',)),

    ('um centésimo de quatrilionésimo', 'br',
     ('0,00000000000000001',)),  # 17 casas decimais
    ('sete mil e doze centésimos de quatrilionésimo', 'br', ('0,00000000000007012',)),

    ('um quintilionésimo', 'br', ('0,000000000000000001',)),  # 18 casas decimais
    ('setenta mil cento e vinte e três quintilionésimos',
     'br', ('0,000000000000070123',)),

    ('um décimo de quintilionésimo', 'br',
     ('0,0000000000000000001',)),  # 19 casas decimais
    ('setenta mil cento e vinte e três décimos de quintilionésimo',
     'br', ('0,0000000000000070123',)),

    ('um centésimo de quintilionésimo', 'br',
     ('0,00000000000000000001',)),  # 20 casas decimais
    ('setenta mil cento e vinte e três centésimos de quintilionésimo',
     'br', ('0,00000000000000070123',)),

    ('um sextilionésimo', 'br', ('0,000000000000000000001',)),  # 21 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro sextilionésimos',
     'br', ('0,000000000000000701234',)),

    ('um décimo de sextilionésimo', 'br',
     ('0,0000000000000000000001',)),  # 22 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro décimos de sextilionésimo',
     'br', ('0,0000000000000000701234',)),

    ('um centésimo de sextilionésimo', 'br',
     ('0,00000000000000000000001',)),  # 23 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro centésimos de sextilionésimo',
     'br', ('0,00000000000000000701234',)),

    ('um septilionésimo', 'br', ('0,000000000000000000000001',)),  # 24 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro septilionésimos',
     'br', ('0,000000000000000000701234',)),

    ('um octilionésimo', 'br', ('0,000000000000000000000000001',)),  # 27 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro octilionésimos',
     'br', ('0,000000000000000000000701234',)),

    # 30 casas decimais
    ('um nonilionésimo', 'br', ('0,000000000000000000000000000001',)),
    ('setecentos e um mil duzentos e trinta e quatro nonilionésimos',
     'br', ('0,000000000000000000000000701234',)),

    # 33 casas decimais
    ('um decilionésimo', 'br', ('0,000000000000000000000000000000001',)),
    ('setecentos e um mil duzentos e trinta e quatro decilionésimos',
     'br', ('0,000000000000000000000000000701234',)),

    # (por_extenso, padrao, (*valores))
    ('zero', 'us', ('0', '0.0')),

    ('um décimo', 'us', ('0.1',)),  # 1 casa decimal
    ('três décimos', 'us', ('0.3',)),
    ('seis décimos', 'us', ('0.6',)),
    ('nove décimos', 'us', ('0.9',)),

    ('dois centésimos', 'us', ('0.02',)),
    ('um centésimo', 'us', ('0.01',)),  # 2 casas decimais
    ('três centésimos', 'us', ('0.03',)),
    ('seis centésimos', 'us', ('0.06',)),
    ('nove centésimos', 'us', ('0.09',)),
    ('onze centésimos', 'us', ('0.11',)),
    ('quarenta e um centésimos', 'us', ('0.41',)),
    ('cinquenta e três centésimos', 'us', ('0.53',)),
    ('oitenta e seis centésimos', 'us', ('0.86',)),

    ('um milésimo', 'us', ('0.001',)),  # 3 casas decimais
    ('três milésimos', 'us', ('0.003',)),
    ('seis milésimos', 'us', ('0.006',)),
    ('nove milésimos', 'us', ('0.009',)),
    ('onze milésimos', 'us', ('0.011',)),
    ('quarenta e um milésimos', 'us', ('0.041',)),
    ('cinquenta e três milésimos', 'us', ('0.053',)),
    ('oitenta e seis milésimos', 'us', ('0.086',)),
    ('cento e um milésimos', 'us', ('0.101',)),
    ('quatrocentos e três milésimos', 'us', ('0.403',)),
    ('setecentos e seis milésimos', 'us', ('0.706',)),
    ('cento e vinte e um milésimos', 'us', ('0.121',)),
    ('quatrocentos e cinquenta e três milésimos', 'us', ('0.453',)),
    ('setecentos e oitenta e seis milésimos', 'us', ('0.786',)),

    ('um décimo de milésimo', 'us', ('0.0001',)),  # 4 casas decimais
    ('três décimos de milésimo', 'us', ('0.0003',)),
    ('seis décimos de milésimo', 'us', ('0.0006',)),
    ('nove décimos de milésimo', 'us', ('0.0009',)),

    ('vinte e um décimos de milésimo', 'us', ('0.0021',)),
    ('cento e cinquenta e três décimos de milésimo', 'us', ('0.0153',)),
    ('quatrocentos e cinquenta e seis décimos de milésimo', 'us', ('0.0456',)),
    ('setecentos e oitenta e nove décimos de milésimo', 'us', ('0.0789',)),
    ('onze décimos de milésimo', 'us', ('0.0011',)),
    ('quarenta e um décimos de milésimo', 'us', ('0.0041',)),
    ('cinquenta e três décimos de milésimo', 'us', ('0.0053',)),
    ('oitenta e seis décimos de milésimo', 'us', ('0.0086',)),


    ('quarenta e um décimos de milésimo', 'us', ('0.0041',)),
    ('três mil e cinquenta e três décimos de milésimo', 'us', ('0.3053',)),
    ('seis mil e oitenta e seis décimos de milésimo', 'us', ('0.6086',)),
    ('nove mil cento e um décimos de milésimo', 'us', ('0.9101',)),
    ('dois mil quatrocentos e três décimos de milésimo', 'us', ('0.2403',)),
    ('cinco mil setecentos e seis décimos de milésimo', 'us', ('0.5706',)),
    ('oito mil cento e vinte e um décimos de milésimo', 'us', ('0.8121',)),
    ('um mil quatrocentos e cinquenta e três décimos de milésimo', 'us', ('0.1453',)),
    ('três mil setecentos e oitenta e seis décimos de milésimo', 'us', ('0.3786',)),

    ('um centésimo de milésimo', 'us', ('0.00001',)),  # 5 casas decimais
    ('dois centésimos de milésimo', 'us', ('0.00002',)),

    ('um milionésimo', 'us', ('0.000001',)),  # 6 casas decimais
    ('três milionésimos', 'us', ('0.000003',)),

    ('um décimo de milionésimo', 'us', ('0.0000001',)),  # 7 casas decimais
    ('quatro décimos de milionésimo', 'us', ('0.0000004',)),

    ('um centésimo de milionésimo', 'us', ('0.00000001',)),  # 8 casas decimais
    ('cinco centésimos de milionésimo', 'us', ('0.00000005',)),

    ('um bilionésimo', 'us', ('0.000000001',)),  # 9 casas decimais
    ('seis bilionésimos', 'us', ('0.000000006',)),

    ('um décimo de bilionésimo', 'us', ('0.0000000001',)),  # 10 casas decimais
    ('sete décimos de bilionésimo', 'us', ('0.0000000007',)),

    ('um centésimo de bilionésimo', 'us', ('0.00000000001',)),  # 11 casas decimais
    ('setenta centésimos de bilionésimo', 'us', ('0.00000000070',)),

    ('um trilionésimo', 'us', ('0.000000000001',)),  # 12 casas decimais
    ('setecentos e um trilionésimos', 'us', ('0.000000000701',)),

    ('um décimo de trilionésimo', 'us', ('0.0000000000001',)),  # 13 casas decimais
    ('setecentos e um décimos de trilionésimo', 'us', ('0.0000000000701',)),

    ('um centésimo de trilionésimo', 'us',
     ('0.00000000000001',)),  # 14 casas decimais
    ('setecentos e um centésimos de trilionésimo', 'us', ('0.00000000000701',)),

    ('um quatrilionésimo', 'us', ('0.000000000000001',)),  # 15 casas decimais
    ('sete mil e doze quatrilionésimos', 'us', ('0.000000000007012',)),

    ('um décimo de quatrilionésimo', 'us',
     ('0.0000000000000001',)),  # 16 casas decimais
    ('sete mil e doze décimos de quatrilionésimo', 'us', ('0.0000000000007012',)),

    ('um centésimo de quatrilionésimo', 'us',
     ('0.00000000000000001',)),  # 17 casas decimais
    ('sete mil e doze centésimos de quatrilionésimo', 'us', ('0.00000000000007012',)),

    ('um quintilionésimo', 'us', ('0.000000000000000001',)),  # 18 casas decimais
    ('setenta mil cento e vinte e três quintilionésimos',
     'us', ('0.000000000000070123',)),

    ('um décimo de quintilionésimo', 'us',
     ('0.0000000000000000001',)),  # 19 casas decimais
    ('setenta mil cento e vinte e três décimos de quintilionésimo',
     'us', ('0.0000000000000070123',)),

    ('um centésimo de quintilionésimo', 'us',
     ('0.00000000000000000001',)),  # 20 casas decimais
    ('setenta mil cento e vinte e três centésimos de quintilionésimo',
     'us', ('0.00000000000000070123',)),

    ('um sextilionésimo', 'us', ('0.000000000000000000001',)),  # 21 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro sextilionésimos',
     'us', ('0.000000000000000701234',)),

    ('um décimo de sextilionésimo', 'us',
     ('0.0000000000000000000001',)),  # 22 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro décimos de sextilionésimo',
     'us', ('0.0000000000000000701234',)),

    ('um centésimo de sextilionésimo', 'us',
     ('0.00000000000000000000001',)),  # 23 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro centésimos de sextilionésimo',
     'us', ('0.00000000000000000701234',)),

    ('um septilionésimo', 'us', ('0.000000000000000000000001',)),  # 24 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro septilionésimos',
     'us', ('0.000000000000000000701234',)),

    ('um octilionésimo', 'us', ('0.000000000000000000000000001',)),  # 27 casas decimais
    ('setecentos e um mil duzentos e trinta e quatro octilionésimos',
     'us', ('0.000000000000000000000701234',)),

    # 30 casas decimais
    ('um nonilionésimo', 'us', ('0.000000000000000000000000000001',)),
    ('setecentos e um mil duzentos e trinta e quatro nonilionésimos',
     'us', ('0.000000000000000000000000701234',)),

    # 33 casas decimais
    ('um decilionésimo', 'us', ('0.000000000000000000000000000000001',)),
    ('setecentos e um mil duzentos e trinta e quatro decilionésimos',
     'us', ('0.000000000000000000000000000701234',)),
)

real_testes = (
    ('um', 'br', ('1', '1,0')),
    ('doze', 'br', ('12', '12,0')),
    ('cento e vinte e três', 'br', ('123', '123,0')),
    ('um mil duzentos e trinta e quatro', 'br', ('1234', '1234,0', '1.234', '1.234,0')),
    ('doze mil trezentos e quarenta e cinco', 'br', ('12345', '12345,0', '12.345', '12.345,0')),
    ('cento e vinte e três mil quatrocentos e cinquenta e seis', 'br', ('123456', '123456,0', '123.456', '123.456,0')),

    ('um milhão', 'br', ('1000000', '1.000.000,0', '1.000.000')),
    ('doze milhões', 'br', ('12000000', '12.000.000,0', '12.000.000')),
    ('um bilhão', 'br', ('1000000000', '1.000.000.000,0', '1.000.000.000')),
    ('doze bilhões', 'br', ('12000000000', '12.000.000.000,0', '12.000.000.000')),
    ('um trilhão', 'br', ('1000000000000', '1.000.000.000.000,0', '1.000.000.000.000')),
    ('cento e vinte e três trilhões', 'br', ('123000000000000', '123.000.000.000.000,0', '123.000.000.000.000')),
    ('um quatrilhão', 'br', ('1000000000000000', '1.000.000.000.000.000,0', '1.000.000.000.000.000')),
    ('duzentos e trinta e quatro quatrilhões', 'br', ('234000000000000000', '234.000.000.000.000.000,0', '234.000.000.000.000.000')),
    ('um quintilhão',  'br', ('1000000000000000000', '1.000.000.000.000.000.000,0', '1.000.000.000.000.000.000')),
    ('um sextilhão',  'br', ('1000000000000000000000', '1.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000')),
    ('um septilhão',  'br', ('1000000000000000000000000', '1.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000')),
    ('um octilhão',  'br', ('1000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000')),
    ('um nonilhão',  'br', ('1000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000')),
    ('um decilhão',  'br', ('1000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000')), #33
    ('um unodecilhão',  'br', ('1000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000')), #36
    ('um duodecilhão',  'br', ('1000000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000.000')), #39
    ('um tredecilhão',  'br', ('1000000000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000')), #42
    ('um quatuordecilhão',  'br', ('1000000000000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000')), #45
    ('um quindecilhão',  'br', ('1000000000000000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000')), #48
    ('um sexdecilhão',  'br', ('1000000000000000000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000')), #51
    ('um sepdecilhão',  'br', ('1000000000000000000000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000')), #54
    ('um octodecilhão',  'br', ('1000000000000000000000000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000')), #57
    ('um novemdecilhão',  'br', ('1000000000000000000000000000000000000000000000000000000000000', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000,0', '1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000')), # 60
    ('cento e vinte e três novemdecilhões quatrocentos e cinquenta e seis octodecilhões setecentos e oitenta e nove sepdecilhões noventa e oito sexdecilhões setecentos e sessenta e cinco quindecilhões quatrocentos e trinta e dois quatuordecilhões cento e nove tredecilhões dois duodecilhões trezentos e trinta e três unodecilhões cinco decilhões dez nonilhões quinze octilhões novecentos e noventa e nove septilhões dezoito bilhões vinte e quatro milhões duzentos mil novecentos e seis', 'br', ('123.456.789.098.765.432.109.002.333.005.010.015.999.000.000.000.000.018.024.200.906',))
)

monetario_testes = ()
