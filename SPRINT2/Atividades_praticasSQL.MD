# Atividades Práticas de SQL
## Caso de estudo Biblioteca
```sql
-- E1
select
    cod,titulo, autor, editora, valor, publicacao, edicao, idioma
from
    livro
where
    publicacao > '2014-12-30'
order by
    cod
-- E2
select 
    titulo, valor
from
    livro
order by
    valor desc
limit 10

-- E3
select count(cod) as quantidade,
    editora.nome,
    endereco.estado,
    endereco.cidade
from 
    livro
join 
    editora on livro.editora = editora.codEditora
join 
    endereco on editora.endereco = endereco.codEndereco
group by
    editora.codEditora, editora.nome, endereco.estado, endereco.cidade
having 
    quantidade > 0
order by 
    quantidade desc
limit 5;

-- E4
select count(livro.cod) as quantidade, 
autor.codAutor,
autor.nome,
autor.nascimento
from
    autor
left join
    livro on autor.codAutor = livro.autor
group by
    autor.codAutor, autor.nome, autor.nascimento
order by
    autor.nome asc

-- E5
select distinct autor.nome
from autor
left join
    livro on autor.codAutor = livro.Autor
left join
    editora on livro.editora = editora.codEditora
left join
    endereco on editora.endereco = endereco.codEndereco
where
    endereco.estado not in ('PARANÁ', 'RIO GRANDE DO SUL')
order by
    autor.nome

-- E6
select distinct
    autor.nome
from
    autor
left join
    livro on autor.codAutor = livro.Autor
left join
    editora on livro.editora = editora.codEditora
left join
    endereco on editora.endereco = endereco.codEndereco
where
    endereco.estado not in ('PARANÁ', 'RIO GRANDE DO SUL')
order by
    autor.nome

-- E7
select
    autor.nome
from    
    autor
left join
    livro on autor.codAutor = Autor
where
    livro.Autor is null
order by
    autor.nome
```

## Caso de estudo Loja
```sql
-- E8
select
    tbvendedor.cdvdd, tbvendedor.nmvdd
from
    tbvendedor
join
    tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
where  
    tbvendas.status = 'Concluído'
group by
    tbvendedor.cdvdd, tbvendedor.nmvdd
order by
    count(tbvendas.cdvdd) desc
limit 1

-- E9
select
    tbvendas.cdpro, tbvendas.nmpro
from
    tbvendas
join
    tbestoqueproduto on tbvendas.cdpro = tbestoqueproduto.cdpro
where
    tbvendas.status = 'Concluído'
    and tbvendas.dtven between '2014-02-03' and '2018-02-02'
group by
    tbvendas.cdpro, tbvendas.nmpro
order by
    sum(tbestoqueproduto.qtdpro) desc
limit 1
    
-- E10
select
    tbvendas.cdpro, tbvendas.nmpro
from
    tbvendas
join
    tbestoqueproduto on tbvendas.cdpro = tbestoqueproduto.cdpro
where
    tbvendas.status = 'Concluído'
    and tbvendas.dtven between '2014-02-03' and '2018-02-02'
group by
    tbvendas.cdpro, tbvendas.nmpro
order by
    sum(tbestoqueproduto.qtdpro) desc
limit 1

-- E11
select
    cdcli, nmcli,
    sum(tbvendas.qtd * tbvendas.vrunt) as gasto
from
    tbvendas
where
    tbvendas.status = 'Concluído'
group by
    tbvendas.cdcli, tbvendas.nmcli
order by
    gasto desc
limit 1;

-- E12
select
    tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc,
    round(sum(tbvendas.qtd * tbvendas.vrunt), 2) as valor_total_vendas
from
    tbvendas
join
    tbdependente on tbvendas.cdvdd = tbdependente.cdvdd
where
    tbvendas.status = 'Concluído'
group by
    tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
having
    valor_total_vendas > 0
order by
    valor_total_vendas
limit 1;

-- E13
select
    tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc,
    round(sum(tbvendas.qtd * tbvendas.vrunt), 2) as valor_total_vendas
from tbvendas
join
    tbdependente on tbvendas.cdvdd = tbdependente.cdvdd
where
    tbvendas.status = 'Concluído'
group by
    tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
having
    valor_total_vendas > 0
order by
    valor_total_vendas
limit 1;

-- E14
select
    tbvendas.estado,
    round(avg(tbvendas.qtd * tbvendas.vrunt), 2) as gastomedio
from
    tbvendas
where
    tbvendas.status = 'Concluído'
group by
    tbvendas.estado
order by
    gastomedio desc;

-- E15
select
    cdven
from
    tbvendas
where
    deletado = 1
order by
    cdven

-- E16
select
    tbvendas.estado, tbvendas.nmpro,
round(avg(tbvendas.qtd), 4) as quantidade_media
from
    tbvendas
where
    tbvendas.status = 'Concluído'
group by
    tbvendas.estado, tbvendas.nmpro
order by
    estado  asc, nmpro asc;
```