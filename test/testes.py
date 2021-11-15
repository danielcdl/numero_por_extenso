# TODO: Criar teste que falha quando a entrada é '1.0'

formatar_numero_testes = (
    ((1, '0'), ('1', '1,0', 1.0, 1)),
    ((12, '0'), ('12', '12,0', 12.0, 12)),
    ((123, '0'), ('123', '123,0', 123.0, 123)),
    ((1234, '0'), ('1234', '1234,0', '1.234,0', 1234.0, 1234)),
    ((12345, '0'), ('12345', '12345,0', '12.345,0', 12345.0, 12345)),
    ((123456, '0'), ('123456', '123456,0', '123.456,0', 123456.0, 123456)),
    ((1, '123'), ('1,123', 1.123)),
    ((12, '987'), ('12,987', 12.987, )),
    ((123, '987'), ('123,987',)), # falha com  123.987
    ((1234, '98'), ('1234,98', '1.234,98', 1234.98)),
    ((12345, '9'), ('12345,9', '12.345,9')),
    ((123456, '1'), ('123456,1', '123.456,1', 123456.1)),
    ((1023456, '1'), ('1023456,1', '1.023.456,1', 1023456.1)),
    ((11023456, '1'), ('11023456,1', '11.023.456,1', 11023456.1)),
    ((115023456, '1'), ('115023456,1', '115.023.456,1', 115023456.1)),
    ((1815023456, '1'), ('1815023456,1', '1.815.023.456,1', 1185023456.1)),
)

real_testes = (
    ('zero', '0', '0.0', '0,0', 0),  
    
    ('um décimo', '0,1', 0.1),
    ('três décimos', '0,3', 0.3),
    ('seis décimos','0,6',  0.6),
    ('nove décimos', '0,9', 0.9),

    ('dois centésimos', '0,02', 0.02),
    ('um centésimo', '0,01', 0.01),
    ('três centésimos', '0,03', 0.03),
    ('seis centésimos', '0,06', 0.06),
    ('nove centésimos', '0,09', 0.09),
    ('onze centésimos', '0,11', 0.11),
    ('quarenta e um centésimos', '0,41', 0.41),
    ('cinquenta e três centésimos', '0,53', 0.53),
    ('oitenta e seis centésimos', '0,86', 0.86),
    
    ('um milésimo', '0,001', 0.001),
    ('três milésimos', '0,003', 0.003),
    ('seis milésimos', '0,006', 0.006),
    ('nove milésimos', '0,009', 0.009),
    ('onze milésimos', '0,011', 0.011),
    ('quarenta e um milésimos', '0,041', 0.041),
    ('cinquenta e três milésimos', '0,053', 0.053),
    ('oitenta e seis milésimos', '0,086', 0.086),
    ('cento e um milésimos', '0,101', 0.101),
    ('quatrocentos e três milésimos', '0,403', 0.403),
    ('setecentos e seis milésimos', '0,706', 0.706),
    ('cento e vinte e um milésimos', '0,121', 0.121),
    ('quatrocentos e cinquenta e três milésimos', '0,453', 0.453),
    ('setecentos e oitenta e seis milésimos', '0,786', 0.786),

    ('um décimo de milésimo', '0,0001', 0.0001),
    ('três décimos de milésimo', '0,0003', 0.0003),
    ('seis décimos de milésimo','0,0006',  0.0006),
    ('nove décimos de milésimo', '0,0009', 0.0009),

    ('vinte e um décimos de milésimo', '0,0021', 0.0021),
    ('cento e cinquenta e três décimos de milésimo', '0,0153', 0.0153),
    ('quatrocentos e cinquenta e seis décimos de milésimo', '0,0456', 0.0456),
    ('setecentos e oitenta e nove décimos de milésimo', '0,0789', 0.0789),
    ('onze décimos de milésimo', '0,0011', 0.0011),
    ('quarenta e um décimos de milésimo', '0,0041', 0.0041),
    ('cinquenta e três décimos de milésimo', '0,0053', 0.0053),
    ('oitenta e seis décimos de milésimo', '0,0086', 0.0086),
    
   
    ('quarenta e um décimos de milésimo', '0,0041', 0.0041),
    ('três mil e cinquenta e três décimos de milésimo', '0,3053', 0.3053),
    ('seis mil e oitenta e seis décimos de milésimo', '0,6086', 0.6086),
    ('nove mil cento e um décimos de milésimo', '0,9101', 0.9101),
    ('dois mil quatrocentos e três décimos de milésimo', '0,2403', 0.2403),
    ('cinco mil setecentos e seis décimos de milésimo', '0,5706', 0.5706),
    ('oito mil cento e vinte e um décimos de milésimo', '0,8121', 0.8121),
    ('um mil quatrocentos e cinquenta e três décimos de milésimo', '0,1453', 0.1453),
    ('três mil setecentos e oitenta e seis décimos de milésimo', '0,3786', 0.3786),
   
    ('um centésimo de milésimo', '0,00001', 0.00001),
    ('dois centésimos de milésimo', '0,00002', 0.00002),

    ('um milionésimo', '0,000001', 0.000001),
    ('três milionésimo', '0,000003', 0.000003),

    ('um décimo de milionésimo', '0,0000001', 0.0000001),
    ('quatro décimos de milionésimo', '0,0000004', 0.0000004),

    ('um centésimo de milionésimo', '0,00000001', 0.00000001),
    ('cinco centésimos de milionésimo', '0,00000005', 0.00000005),

    ('um bilionésimo', '0,000000001', 0.000000001),
    ('seis bilionésimos', '0,000000006', 0.000000006),

    ('um décimo de bilionésimo', '0,0000000001', 0.0000000001),
    ('sete décimos de bilionésimo', '0,0000000007', 0.0000000007),

    ('um centésimo de bilionésimo', '0,00000000001', 0.00000000001),
    ('setetenta décimos de bilionésimo', '0,00000000070', 0.00000000070),

    ('um trilionésimo', '0,000000000001', 0.000000000001),
    ('setecentos e um trilionésimos', '0,000000000701', 0.000000000701),

    ('um quatrilionésimo', '0,0000000000001', 0.0000000000001),
    ('sete mil e doze quatrilionésimos', '0,0000000007012', 0.0000000007012),

    ('um quintilionésimo', '0,00000000000001', 0.00000000000001),
    ('setenta mil cento e vinte e três quintilionésimos', '0,00000000070123', 0.00000000070123),

    ('um sextilionésimo', '0,000000000000001', 0.000000000000001),
    ('setecentos e um mil duzentos e trinta e quatro sextilionésimos', '0,0000000000701234', 0.0000000000701234),

    ('um septilionésimo', '0,0000000000000001', 0.0000000000000001),
    ('setecentos e um mil duzentos e trinta e quatro septilionésimos', '0,00000000000701234', 0.00000000000701234),

    ('um octilionésimo', '0,00000000000000001', 0.00000000000000001),
    ('setecentos e um mil duzentos e trinta e quatro octilionésimo', '0,000000000000701234', 0.000000000000701234),

    ('um nonilionésimo', '0,000000000000000001', 0.000000000000000001),
    ('setecentos e um mil duzentos e trinta e quatro nonilionésimos', '0,0000000000000701234', 0.0000000000000701234),

    ('um decilionésimo', '0,0000000000000000001', 0.0000000000000000001),
    ('setecentos e um mil duzentos e trinta e quatro decilionésimos', '0,00000000000000701234', 0.00000000000000701234),
)

real_test2 = (
    ('um', ('1', '1,0', 1.0, 1)),
    ('doze', ('12', '12,0', 12.0, 12)),
    ('cento e vinte e três', ('123', '123,0', 123.0, 123)),
    ('um mil duzentos e trinta e quatro', ('1234', '1234,0', '1.234', '1.234,0', 1234.0, 1234)),
    ('doze mil trezentos e quarenta e cinco', ('12345', '12345,0', '12.345', '12.345,0', 12345.0, 12345)),
    ('cento e vinte e três mil quatrocentos e cincoenta e seis', ('123456', '123456,0', '123.456', '123.456,0', 123456.0, 123456)),
)

UNIDADES = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
DEZENA_ESPECIAL = ('', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
DEZENAS = ('', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
CENTENAS = ('cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos','oitocentos', 'novecentos')
MILHAR = (
    ('milhão', 'milhões'), ('bilhão', 'bilhões'), ('trilhão', 'trilhões'), ('quatrilhão', 'quatrilhões'), 
    ('quintilhão', 'quintilhões'), ('sextilhão', 'sextilhões'), ('septilhão', 'septilhões'), ('octilhão', 'octilhões'), ('nonilhão', 'nonilhões'), ('decilhão', 'decilhões'),
    ('unodecilhão', 'unodecilhões'), ('duodecilhão', 'duodecilhões'), ('tredecilhão', 'tredecilhões'), ('quatuordecilhão', 'quatuordecilhões'),
    ('quindecilhão', 'quindecilhões'), ('sexdecilhão', 'sexdecilhões'), ('sepdecilhão', 'sepdecilhões'), ('octodecilhão', 'octodecilhões'),
    ('novemdecilhão', 'novemdecilhões')
)


monetario_testes = ()