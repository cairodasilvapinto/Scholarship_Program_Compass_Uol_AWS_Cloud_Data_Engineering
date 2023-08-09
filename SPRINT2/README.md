# Certificados
-  SQL para Análise de Dados: Do básico ao avançado
![SQL para Análise de Dados: Do básico ao avançado](<CERTIFICADOS/SQL para Análise de Dados Do básico ao avançado.png>)

- Certificado de conclução da sprint 2
![Certificado de conclução da sprint 2](<CERTIFICADOS/Data & Analytics - PB - AWS sprint2.jpg>)
# querys dos projetos de SQL
## Projeto 1

```sql
-- (Query 1) Receita, leads, conversão e ticket médio mês a mês
-- Colunas: mês, leads (#), vendas (#), receita (k, R$), conversão (%), ticket médio (k, R$)

-- Definindo a tabela  "leads" que agrupa as visitas à página por mês
-- e conta quantas visitas ocorreram em cada mês.
with leads as (
    select
        date_trunc('month', visit_page_date)::date as visit_page_month,
        count(*) as visit_page_count
    from sales.funnel
    group by visit_page_month
    order by visit_page_month
),

-- Definindo a tabela  "payments" que calcula informações sobre pagamentos.
-- Ela inclui o mês de pagamento, a contagem de pagamentos nesse mês,
-- e a receita total (calculada com base no preço do produto e desconto).
payments as (
    select
        date_trunc('month', fun.paid_date)::date as paid_month,
        count(fun.paid_date) as paid_count,
        sum(pro.price * (1+fun.discount)) as receita
    from sales.funnel as fun
    left join sales.products as pro
        on fun.product_id = pro.product_id
    where fun.paid_date is not null
    group by paid_month
    order by paid_month
)

-- Selecionando as informações finais para exibição.
-- Combinando as tabelas temporárias "leads" e "payments" usando um LEFT JOIN
-- para calcular e exibir várias métricas de desempenho.
select
    leads.visit_page_month as "mês",              -- Seleciona o mês a partir da tabela "leads".
    leads.visit_page_count as "leads (#)",        -- Seleciona o número de leads do mês.
    payments.paid_count as "vendas (#)",          -- Seleciona o número de vendas do mês.
    (payments.receita/1000) as "receita (k, R$)", -- Calcula a receita em milhares de reais.
    (payments.paid_count::float/leads.visit_page_count::float) as "conversão (%)", -- Calcula a taxa de conversão.
    (payments.receita/payments.paid_count/1000) as "ticket médio (k, R$)"        -- Calcula o ticket médio em milhares de reais.
from leads
left join payments
    on leads.visit_page_month = paid_month;  -- Combina as tabelas temporárias através do mês.


-- (Query 2) Estados que mais venderam
-- Colunas: país, estado, vendas (#)

-- Selecionando os estados que mais venderam no Brasil durante agosto de 2021.
select
    'Brazil' as país,                  -- Define o país como "Brazil".
    cus.state as estado,               -- Seleciona o estado do cliente da tabela "sales.customers".
    count(fun.paid_date) as "vendas (#)"  -- Conta o número de datas de pagamento na tabela "sales.funnel".
                                        -- Isso representa o número de vendas em cada estado.
from sales.funnel as fun
left join sales.customers as cus       -- Faz um LEFT JOIN com a tabela "sales.customers" para obter informações do cliente.
    on fun.customer_id = cus.customer_id
where paid_date between '2021-08-01' and '2021-08-31'  -- Filtra as vendas realizadas entre 1º de agosto e 31 de agosto de 2021.
group by país, estado                 -- Agrupa os resultados por país e estado.
order by "vendas (#)" desc             -- Ordena os resultados em ordem decrescente de vendas.
limit 5;                                -- Limita o resultado a apenas 5 registros (estados que mais venderam).


-- (Query 3) Marcas que mais venderam no mês
-- Colunas: marca, vendas (#)

-- Selecionando as marcas que mais venderam durante o mês de agosto de 2021.
select
    pro.brand as marca,                 -- Seleciona a coluna de marca da tabela "sales.products".
    count(fun.paid_date) as "vendas (#)"  -- Conta o número de datas de pagamento na tabela "sales.funnel".
                                         -- Isso representa o número de vendas para cada marca.
from sales.funnel as fun
left join sales.products as pro          -- Faz um LEFT JOIN com a tabela "sales.products" para obter informações do produto.
    on fun.product_id = pro.product_id
where paid_date between '2021-08-01' and '2021-08-31'  -- Filtra as vendas realizadas entre 1º de agosto e 31 de agosto de 2021.
group by marca                           -- Agrupa os resultados por marca.
order by "vendas (#)" desc                -- Ordena os resultados em ordem decrescente de vendas.
limit 5;                                 -- Limita o resultado a apenas 5 registros (marcas que mais venderam).


-- (Query 4) Lojas que mais venderam
-- Colunas: loja, vendas (#)

-- Selecionando as lojas que mais venderam durante o mês de agosto de 2021.
select
    sto.store_name as loja,               -- Seleciona o nome da loja da tabela "sales.stores".
    count(fun.paid_date) as "vendas (#)"  -- Conta o número de datas de pagamento na tabela "sales.funnel".
                                         -- Isso representa o número de vendas para cada loja.
from sales.funnel as fun
left join sales.stores as sto            -- Faz um LEFT JOIN com a tabela "sales.stores" para obter informações da loja.
    on fun.store_id = sto.store_id
where paid_date between '2021-08-01' and '2021-08-31'  -- Filtra as vendas realizadas entre 1º de agosto e 31 de agosto de 2021.
group by loja                            -- Agrupa os resultados por loja.
order by "vendas (#)" desc                -- Ordena os resultados em ordem decrescente de vendas.
limit 5;                                 -- Limita o resultado a apenas 5 registros (lojas que mais venderam).


-- (Query 5) Dias da semana com maior número de visitas ao site
-- Colunas: dia_semana, dia da semana, visitas (#)
-- Seleciona a extração do dia da semana da coluna visit_page_date e dá um apelido de 'dia_semana'
SELECT
    EXTRACT('dow' FROM visit_page_date) AS dia_semana,
    
    -- Usa um bloco CASE para traduzir o valor numérico do dia da semana em seu nome correspondente
    CASE 
        WHEN EXTRACT('dow' FROM visit_page_date) = 0 THEN 'domingo'
        WHEN EXTRACT('dow' FROM visit_page_date) = 1 THEN 'segunda'
        WHEN EXTRACT('dow' FROM visit_page_date) = 2 THEN 'terça'
        WHEN EXTRACT('dow' FROM visit_page_date) = 3 THEN 'quarta'
        WHEN EXTRACT('dow' FROM visit_page_date) = 4 THEN 'quinta'
        WHEN EXTRACT('dow' FROM visit_page_date) = 5 THEN 'sexta'
        WHEN EXTRACT('dow' FROM visit_page_date) = 6 THEN 'sábado'
        ELSE NULL 
    END AS "dia da semana",
    
    -- Conta o número de registros para cada dia da semana
    COUNT(*) AS "visitas (#)"
    
-- Seleciona dados da tabela sales.funnel
FROM sales.funnel

-- Filtra registros dentro do intervalo de datas especificado
WHERE visit_page_date BETWEEN '2021-08-01' AND '2021-08-31'

-- Agrupa os resultados pelo valor extraído do dia da semana
GROUP BY dia_semana

-- Ordena os resultados pelo dia da semana
ORDER BY dia_semana;

```

## Projeto 2

```sql
-- (Query 1) Contagem de Gênero dos Leads
-- Nesta consulta, estamos calculando o número de leads por gênero.

-- Seleciona e categoriza o gênero dos leads com base na coluna 'gender' da tabela 'ibge_genders'.
SELECT
    CASE
        WHEN ibge.gender = 'male' THEN 'homens'
        WHEN ibge.gender = 'female' THEN 'mulheres'
    END AS "gênero",
    
    -- Conta o número total de leads para cada categoria de gênero.
    COUNT(*) AS "leads (#)"
    
-- Seleciona dados da tabela 'customers' com um join à tabela temporária 'ibge_genders'.
FROM sales.customers AS cus
LEFT JOIN temp_tables.ibge_genders AS ibge
    ON LOWER(cus.first_name) = LOWER(ibge.first_name)
    
-- Agrupa os resultados pelo valor da coluna 'gender' da tabela 'ibge_genders'.
GROUP BY ibge.gender;

-- (Query 2) Status profissional dos leads
-- Colunas: status profissional, leads (%)
SELECT
    -- Mapeia o status profissional para categorias mais legíveis
    CASE
        WHEN professional_status = 'freelancer' THEN 'freelancer'
        WHEN professional_status = 'retired' THEN 'aposentado(a)'
        WHEN professional_status = 'clt' THEN 'clt'
        WHEN professional_status = 'self_employed' THEN 'autônomo(a)'
        WHEN professional_status = 'other' THEN 'outro'
        WHEN professional_status = 'businessman' THEN 'empresário(a)'
        WHEN professional_status = 'civil_servant' THEN 'funcionário(a) público(a)'
        WHEN professional_status = 'student' THEN 'estudante'
    END AS "status profissional",
    -- Calcula a porcentagem de leads para cada categoria
    (COUNT(*)::float) / (SELECT COUNT(*) FROM sales.customers) AS "leads (%)"
FROM sales.customers
-- Agrupa os resultados pelo status profissional
GROUP BY professional_status
-- Ordena os resultados pela porcentagem de leads em ordem crescente
ORDER BY "leads (%)";


-- (Query 3) Faixa etária dos leads
-- Consulta 3: Faixa Etária, leads (%)
SELECT
    -- Divide a faixa etária em categorias legíveis
    CASE
        WHEN datediff('years', birth_date, current_date) < 20 THEN '0-20'
        WHEN datediff('years', birth_date, current_date) < 40 THEN '20-40'
        WHEN datediff('years', birth_date, current_date) < 60 THEN '40-60'
        WHEN datediff('years', birth_date, current_date) < 80 THEN '60-80'
        ELSE '80+'
    END AS "faixa etária",
    -- Calcula a porcentagem de leads para cada faixa etária
    COUNT(*)::float / (SELECT COUNT(*) FROM sales.customers) AS "leads (%)"
FROM sales.customers
-- Agrupa os resultados pela faixa etária
GROUP BY "faixa etária"
-- Ordena os resultados pela faixa etária em ordem decrescente
ORDER BY "faixa etária" DESC;


-- Query 4: Faixa Salarial dos Leads
-- Colunas: faixa salarial, leads (%), ordem
SELECT
    -- Divide a faixa salarial em categorias legíveis
    CASE
        WHEN income < 5000 THEN '0-5000'
        WHEN income < 10000 THEN '5000-10000'
        WHEN income < 15000 THEN '10000-15000'
        WHEN income < 20000 THEN '15000-20000'
        ELSE '20000+'
    END AS "faixa salarial",
    -- Calcula a porcentagem de leads para cada faixa salarial
    COUNT(*)::float / (SELECT COUNT(*) FROM sales.customers) AS "leads (%)",
    -- Atribui uma ordem numérica para cada faixa salarial
    CASE
        WHEN income < 5000 THEN 1
        WHEN income < 10000 THEN 2
        WHEN income < 15000 THEN 3
        WHEN income < 20000 THEN 4
        ELSE 5
    END AS "ordem"
FROM sales.customers
-- Agrupa os resultados pela faixa salarial e pela ordem
GROUP BY "faixa salarial", "ordem"
-- Ordena os resultados pela ordem em ordem decrescente
ORDER BY "ordem" DESC;


-- (Query 5) Classificação dos veículos visitados
-- Consulta 5: classificação do veículo, veículos visitados (#)
-- Regra de negócio: Veículos novos tem até 2 anos e seminovos acima de 2 anos
WITH classificacao_veiculos AS (
    -- Cria uma CTE (Common Table Expression) para classificar os veículos
    SELECT
        fun.visit_page_date,
        pro.model_year,
        EXTRACT('year' FROM visit_page_date) - pro.model_year::int AS idade_veiculo,
        CASE
            WHEN (EXTRACT('year' FROM visit_page_date) - pro.model_year::int) <= 2 THEN 'novo'
            ELSE 'seminovo'
        END AS "classificação do veículo"
    FROM sales.funnel AS fun
    LEFT JOIN sales.products AS pro ON fun.product_id = pro.product_id
)
-- Seleciona a classificação do veículo e conta a quantidade de veículos visitados
SELECT
    "classificação do veículo",
    COUNT(*) AS "veículos visitados (#)"
FROM classificacao_veiculos
-- Agrupa os resultados pela classificação do veículo
GROUP BY "classificação do veículo";



-- Query 6: Calcula a distribuição de idade dos veículos visitados
-- Colunas: Idade do veículo, veículos visitados (%), ordem
with
    faixa_de_idade_dos_veiculos as (
        select
            fun.visit_page_date,
            pro.model_year,
            extract('year' from visit_page_date) - pro.model_year::int as idade_veiculo,
            case
                when (extract('year' from visit_page_date) - pro.model_year::int)<=2 then 'até 2 anos'
                when (extract('year' from visit_page_date) - pro.model_year::int)<=4 then 'de 2 à 4 anos'
                when (extract('year' from visit_page_date) - pro.model_year::int)<=6 then 'de 4 à 6 anos'
                when (extract('year' from visit_page_date) - pro.model_year::int)<=8 then 'de 6 à 8 anos'
                when (extract('year' from visit_page_date) - pro.model_year::int)<=10 then 'de 8 à 10 anos'
                else 'acima de 10 anos'
            end as "idade do veículo",
            case
                when (extract('year' from visit_page_date) - pro.model_year::int)<=2 then 1
                when (extract('year' from visit_page_date) - pro.model_year::int)<=4 then 2
                when (extract('year' from visit_page_date) - pro.model_year::int)<=6 then 3
                when (extract('year' from visit_page_date) - pro.model_year::int)<=8 then 4
                when (extract('year' from visit_page_date) - pro.model_year::int)<=10 then 5
                else 6
            end as "ordem"
        from sales.funnel as fun
        left join sales.products as pro
            on fun.product_id = pro.product_id
    )
select
    "idade do veículo",
    count(*)::float/(select count(*) from sales.funnel) as "veículos visitados (%)",
    ordem
from faixa_de_idade_dos_veiculos
group by "idade do veículo", ordem
order by ordem;



-- Query 7: Determina os veículos mais visitados por marca
-- Colunas: brand, model, visitas (#)
select
    pro.brand,
    pro.model,
    count(*) as "visitas (#)"
from sales.funnel as fun
left join sales.products as pro
    on fun.product_id = pro.product_id
group by pro.brand, pro.model
order by pro.brand, pro.model, "visitas (#)";
```