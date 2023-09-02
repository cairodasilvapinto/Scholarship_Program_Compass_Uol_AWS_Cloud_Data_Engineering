
# Apresentação

Olá sou Cairo da Silva Pinto tenho 19 anos e moro em Ilha Solteira-SP, estou cursando Sistemas de Informação na UFMS de Três Lagoas, atualmente no quarto semestre. Tenho cinco meses de experiência com desenvolvimento web full stack. Como hobbies, tenho a musculação, que é uma paixão minha. Além disso, sou fascinado por tecnologia. Meus objetivos na trajetória da bolsa são aprender ao máximo e aprimorar minhas habilidades.

[Click para Sprint 1](https://github.com/cairodasilvapinto/bolsaCOMPASS#1-sprint-1) [Click para Sprint 2](https://github.com/cairodasilvapinto/bolsaCOMPASS#2-sprint-2) [Click para Sprint 3](https://github.com/cairodasilvapinto/bolsaCOMPASS/blob/main/README.md#3-sprint-3)
# Cultura Ágil e Segurança
[Certificados de Cultura Ágil e Segurança](https://github.com/cairodasilvapinto/bolsaCOMPASS/tree/main/Cultura%20%C3%81gil%20e%20Seguran%C3%A7a)
## Segurança em Aplicações WEB
### Principios da segurança da informação
Os princípios da segurança da informação são um conjunto de diretrizes e direcionamentos que ajudam a orientar a forma como as organizações e os indivíduos devem abordar a proteção da informação e dos sistemas. Esses princípios fornecem um conjunto de valores fundamentais para garantir a confidencialidade, integridade e disponibilidade das informações. Os principais princípios da segurança da informação são:

- Confidencialidade: Garantir que as informações só sejam acessíveis por pessoas autorizadas e que não sejam reveladas a indivíduos não autorizados. Isso envolve criptografia, autenticação e controle de acesso.

- Integridade: Assegurar que as informações sejam precisas, completas e não tenham sido alteradas de forma não autorizada. Isso pode ser alcançado por meio de controle de alterações, assinaturas digitais e hashes.

- Disponibilidade: Garantir que as informações e os sistemas estejam disponíveis e acessíveis quando necessário. Isso envolve proteção contra interrupções, falhas e ataques que possam afetar a disponibilidade.

- Autenticidade: Verificar a identidade dos usuários e a autenticidade das informações. Isso é crucial para prevenir acesso não autorizado e manipulação de dados.

- Não Repúdio: Evitar que uma pessoa negue sua autoria ou participação em uma transação. Isso é frequentemente alcançado por meio de assinaturas digitais e registros de auditoria.

- Princípio do Menor Privilégio: Conceder apenas os privilégios mínimos necessários a um usuário para realizar suas tarefas. Isso limita o impacto potencial de um comprometimento.

- Separação de Funções: Dividir as responsabilidades entre diferentes usuários para evitar conflitos de interesse e reduzir a possibilidade de fraude interna.

- Defesa em Profundidade: Utilizar várias camadas de segurança para proteger sistemas e informações, garantindo que uma única medida de segurança não seja suficiente para evitar um ataque.

- Avaliação e Gerenciamento de Riscos: Identificar, avaliar e gerenciar os riscos de segurança da informação, priorizando ações de acordo com a gravidade das ameaças e vulnerabilidades.

- Conformidade: Cumprir com as regulamentações, leis e padrões relevantes em relação à segurança da informação, garantindo que as práticas de segurança estejam em conformidade com os requisitos legais e do setor.

- Treinamento e Conscientização: Educar os usuários sobre as práticas de segurança, ameaças cibernéticas e suas responsabilidades na proteção das informações.

- Resposta a Incidentes: Ter planos e processos em vigor para lidar com incidentes de segurança, minimizando os danos e restaurando a operação normal o mais rápido possível.

Esses princípios formam a base para a construção de uma estratégia de segurança eficaz, ajudando a proteger os ativos de informação e a minimizar os riscos associados às ameaças de segurança.

### Tipos de vulnerabilidades citados pela OWASP

A OWASP (Open Web Application Security Project) é uma organização que se dedica a melhorar a segurança de software, especialmente em aplicações web. O projeto OWASP Top Ten lista os dez principais riscos de segurança em aplicações web. As vulnerabilidades mencionadas no OWASP Top Ten podem variar ao longo das diferentes versões, mas vou fornecer uma visão geral das vulnerabilidades frequentemente citadas:

- Injection (Injeção): Isso ocorre quando dados não confiáveis são incorporados em comandos ou consultas de forma inadequada, permitindo que um invasor execute comandos não autorizados.

- Broken Authentication (Autenticação Quebrada): Refere-se a falhas na implementação de recursos de autenticação e sessões, permitindo que invasores assumam contas de usuários.

- Sensitive Data Exposure (Exposição de Dados Sensíveis): Ocorre quando dados confidenciais, como senhas, são armazenados ou transmitidos de forma inadequada, tornando-os suscetíveis a acesso não autorizado.

- XML External Entities (XXE): É uma vulnerabilidade que ocorre quando uma aplicação processa entradas XML maliciosas, permitindo que um invasor acesse recursos do sistema ou execute ataques de negação de serviço.

- Broken Access Control (Controle de Acesso Quebrado): Isso acontece quando um sistema não impõe restrições adequadas sobre quais usuários têm acesso a quais recursos, permitindo que invasores acessem funcionalidades não autorizadas.

- Security Misconfiguration (Configuração de Segurança Incorreta): Refere-se a falhas na configuração de segurança, como padrões de senha fracos, acesso não autorizado a diretórios ou configurações inadequadas do servidor.

- Cross-Site Scripting (XSS): É uma vulnerabilidade que permite que invasores injetem código malicioso em páginas da web visualizadas por outros usuários, levando a ataques de roubo de informações ou sessões.

- Insecure Deserialization (Desserialização Insegura): Ocorre quando dados serializados (por exemplo, em JSON ou XML) são manipulados de forma inadequada, permitindo que um invasor execute código malicioso.

- Using Components with Known Vulnerabilities (Uso de Componentes com Vulnerabilidades Conhecidas): Isso acontece quando uma aplicação usa bibliotecas, frameworks ou componentes com falhas de segurança conhecidas.

- Insufficient Logging & Monitoring (Log e Monitoramento Insuficientes): Refere-se à falta de registro adequado de eventos de segurança e à falta de monitoramento, dificultando a detecção e resposta a incidentes.

Quanto às vulnerabilidades mais graves do OWASP Top Ten, essa avaliação pode variar dependendo do contexto, do tipo de aplicação e das medidas de segurança adotadas. No entanto, vulnerabilidades como Injeção, Autenticação Quebrada, Exposição de Dados Sensíveis e Cross-Site Scripting tendem a ser amplamente consideradas como riscos críticos, pois podem levar a comprometimento significativo dos dados e da funcionalidade da aplicação. É importante lembrar que a gravidade das vulnerabilidades também depende da forma como elas são exploradas e das medidas de mitigação implementadas.

### Planejamento da Análise de Vulnerabilidades
O planejamento da análise de vulnerabilidade é uma etapa crucial na garantia da segurança de sistemas e redes. Envolve a identificação de vulnerabilidades potenciais para que possam ser mitigadas antes que sejam exploradas por invasores. Existem várias etapas na análise de vulnerabilidade, incluindo a coleta de informações, varreduras, obtenção e manutenção de acesso não autorizado. O projeto OWASP também oferece um método abrangente para realizar análises de vulnerabilidade eficazes.

#### Tipos de Análise de Vulnerabilidade:

1. Footprinting (Levantamento de Informações): Envolve a coleta de informações sobre o alvo, como detalhes da rede, domínios, subdomínios, endereços IP, registros WHOIS etc. Isso ajuda a entender a superfície de ataque e os pontos fracos potenciais.

2. Scanning (Varredura): Nesta fase, ferramentas automatizadas são usadas para identificar ativamente vulnerabilidades conhecidas. Isso pode incluir varreduras de portas, varreduras de serviços e análise de configurações de segurança inadequadas.

3. Gaining Access (Obtenção de Acesso): Se as vulnerabilidades são encontradas, a próxima etapa é explorá-las para ganhar acesso não autorizado. Isso pode envolver a exploração de falhas de segurança ou o uso de técnicas como injeções, cross-site scripting, entre outras.

4. Maintaining Access (Manutenção de Acesso): Uma vez obtido o acesso, os invasores podem tentar manter sua presença oculta, por meio de backdoors ou outros métodos, para poderem acessar o sistema novamente no futuro.

#### Método de Análise de Vulnerabilidade OWASP:

A OWASP fornece um guia abrangente para a análise de vulnerabilidade chamado "OWASP Application Security Verification Standard Project". Este método incorpora as melhores práticas da indústria para conduzir avaliações de segurança em aplicações web e fornece uma estrutura detalhada para a análise de vulnerabilidades.

##### **Ele inclui várias atividades, como:**

- Modelagem de Ameaças: Identificar ameaças potenciais que podem afetar o sistema ou aplicativo, avaliando o risco associado a cada ameaça.

- Verificação de Segurança da Aplicação: Realizar testes de segurança que abrangem uma variedade de categorias, como autenticação, autorização, manipulação de entrada, entre outras.

- Verificação de Infraestrutura e Configuração: Avaliar a configuração do ambiente em que o aplicativo é executado, incluindo servidores, bancos de dados e serviços.

- Verificação de Implementação Segura: Avaliar o código-fonte do aplicativo em busca de vulnerabilidades específicas de programação, como injeções de SQL ou cross-site scripting.

- Avaliação de Risco: Avaliar a gravidade das vulnerabilidades encontradas e determinar as ações corretivas necessárias.

O método OWASP enfatiza a abordagem em camadas para avaliação de segurança, cobrindo vários aspectos da aplicação e do ambiente em que ela opera. Isso ajuda a identificar uma variedade de vulnerabilidades, desde erros de configuração até falhas de codificação, contribuindo para a criação de sistemas mais seguros.

![image](https://github.com/cairodasilvapinto/bolsaCOMPASS/assets/131769429/b5c9641b-c0c5-4b3d-8977-082ee926a9dd)

## Métodos ágeis de A a Z: o curso completo
### Gestão de projeto: do método tradicional ao ágil

- Método Tradicional: O gerenciamento de projetos tradicional, também conhecido como abordagem cascata ou waterfall, é caracterizado por fases sequenciais e rígidas, onde o projeto é dividido em etapas bem definidas, como planejamento, execução, monitoramento e encerramento. As decisões são tomadas antecipadamente e as mudanças são difíceis de incorporar após o início do projeto. Essa abordagem funciona melhor para projetos estáveis e previsíveis.
- Método Ágil: O gerenciamento ágil de projetos é uma abordagem adaptativa e flexível, que valoriza a colaboração, a entrega incremental e a resposta rápida às mudanças. É baseado em princípios ágeis, como o Manifesto Ágil, e utiliza metodologias como Scrum e Kanban. As equipes trabalham em ciclos curtos, entregando incrementos do produto em intervalos frequentes, permitindo assim a obtenção de feedback constante dos clientes e stakeholders para orientar a evolução do projeto.

### Mundo VUCA e Mundo BANI:

- Mundo VUCA: VUCA é um acrônimo das palavras Volátil, Incerto, Complexo e Ambíguo. Esse termo descreve a natureza do ambiente atual de negócios e projetos, onde as condições são marcadas por mudanças rápidas e imprevisíveis. O mundo VUCA exige que as organizações e os profissionais se adaptem constantemente a novas circunstâncias, sejam ágeis na tomada de decisões e estejam preparados para lidar com complexidades e ambiguidades.
- Mundo BANI: BANI é outro acrônimo das palavras Frágil, Ansioso, Não Linear e Incompreensível. Esse conceito foi proposto como uma atualização do VUCA, levando em conta as mudanças sociais e tecnológicas ainda mais aceleradas. No mundo BANI, as estruturas e sistemas podem ser mais frágeis e sujeitos a falhas, a ansiedade prevalece devido à incerteza constante, as relações de causa e efeito são menos lineares e as situações podem ser tão complexas que são difíceis de serem compreendidas em sua totalidade.

Em resumo, a transição do método tradicional para o ágil se torna cada vez mais relevante no mundo VUCA e, especialmente, no mundo BANI, pois as abordagens ágeis permitem maior adaptabilidade e resposta às rápidas mudanças e complexidades que enfrentamos hoje.

### Manifesto ágil
é um documento criado em fevereiro de 2001 por um grupo de 17 especialistas em desenvolvimento de software, que se reuniram em Utah, EUA. Esses profissionais representavam diferentes abordagens de desenvolvimento de software, como Scrum, XP, entre outras. O objetivo do manifesto era estabelecer valores e princípios comuns que fundamentassem uma nova abordagem de desenvolvimento ágil de software. Ele é composto por quatro valores e doze princípios, que enfatizam a importância de responder a mudanças, de promover a colaboração entre indivíduos e equipes, de entregar valor funcional de forma rápida e contínua, e de focar nas necessidades do cliente. Os quatro valores do Manifesto Ágil são os seguintes:

1. Indivíduos e interações acima de processos e ferramentas: Valoriza a importância da comunicação e colaboração entre as pessoas envolvidas no projeto, enfatizando que a interação direta é mais eficiente do que depender excessivamente de processos ou ferramentas.
2. Software funcionando acima de documentação abrangente: Dá prioridade à entrega de software funcional, que atenda às necessidades do cliente, em vez de se concentrar em extensa documentação, que pode se tornar obsoleta rapidamente.
3. Colaboração com o cliente acima de negociação de contratos: Enfatiza a importância de envolver o cliente ou usuário final ao longo do processo de desenvolvimento, buscando feedback constante para garantir a satisfação do cliente e o alinhamento com suas necessidades.
4. Responder a mudanças acima de seguir um plano: Reconhece que, em ambientes complexos e dinâmicos, a capacidade de se adaptar a mudanças é fundamental para o sucesso do projeto. Em vez de se apegar rigidamente a planos pré-definidos, o foco deve ser na flexibilidade e na capacidade de responder rapidamente às mudanças.

As práticas e metodologias ágeis, como Scrum, Kanban, Lean e XP, se baseiam nesses fundamentos. O Manifesto Ágil promoveu uma cultura de adaptabilidade, trabalho em equipe e entrega contínua de valor em várias áreas de negócios e projetos.

**O que é Scrum?** É um framework que permite que equipes desenvolvam, entreguem e melhorem produtos complexos de forma iterativa e incremental. Foi originalmente criado para o desenvolvimento de software, mas hoje é amplamente utilizado em diversas áreas, como marketing, engenharia, desenvolvimento de produtos e muito mais. O Scrum é baseado em alguns conceitos-chave: Scrum Team, Sprints, Product Backlog, Sprint Backlog, Daily Scrum, Sprint Review, Sprint Retrospective, essência mas de acordo com as necessidades e variáveis dentro da empresa os conceitos podem se adaptar. O Scrum oferece uma abordagem flexível e iterativa para o gerenciamento de projetos, permitindo que as equipes respondam rapidamente a mudanças e entreguem valor em curtos períodos de tempo. Através do foco na transparência, inspeção e adaptação contínua, o Scrum busca maximizar a eficiência da equipe e a satisfação do cliente ao longo do processo de desenvolvimento do produto.

**O que é Kanban?** O Kanban utiliza um quadro visual, geralmente dividido em colunas, para representar o fluxo de trabalho do projeto ou processo. Cada item de trabalho é representado por um cartão ou post-it e é movido ao longo do quadro à medida que progride no processo, desde o início até a conclusão. As colunas podem ser personalizadas de acordo com as etapas do fluxo de trabalho específicas da equipe ou projeto.
Os princípios fundamentais do Kanban incluem:
1. Visualização do Trabalho: O quadro Kanban proporciona uma visão clara do trabalho em andamento, permitindo que todos na equipe acompanhem o progresso das tarefas.
2. Limite de Trabalho em Progresso (WIP - Work in Progress): O Kanban incentiva a limitação da quantidade de trabalho em andamento em cada etapa do processo. Isso ajuda a evitar sobrecarregar a equipe e a identificar gargalos no fluxo de trabalho.
3. Gestão do Fluxo: O foco está na manutenção de um fluxo contínuo de trabalho, eliminando atrasos e desperdícios e garantindo a entrega consistente de valor.
4. Feedback Contínuo e Melhoria: O Kanban promove a melhoria contínua, incentivando a equipe a revisar regularmente o processo e buscar maneiras de otimizar o fluxo de trabalho.
O Kanban é particularmente útil para equipes que trabalham com demandas variáveis ou que precisam lidar com tarefas emergentes. Ele oferece maior flexibilidade em relação a prazos e prioridades, permitindo que as equipes respondam rapidamente a mudanças nas necessidades do cliente ou nas condições do mercado.

**O que é Lean?** O Lean também conhecico como Lean Thinking ou Pensamento Enxuto, o conceito central do Lean é eliminar desperdícios e criar valor para o cliente, com o objetivo de otimizar o desempenho e a eficiência de um sistema ou processo. O Lean pode ser aplicado não apenas na indústria automobilística, mas em várias áreas, incluindo manufatura, serviços, saúde, tecnologia da informação, entre outros. A filosofia dele visa criar sistemas eficientes, com foco no cliente e adaptados às mudanças, resultando em maior produtividade, qualidade, redução de custos e satisfação do cliente. Além disso, o Lean incentiva a participação e o envolvimento de todos os funcionários, promovendo uma cultura de melhoria contínua e aprendizado.
Seus principais fundamentos são: Identificar Valor, Mapear o Fluxo de Valor, Criar Fluxo Contínuo, Produzir de Acordo com a Demanda e Buscar a Perfeição.

**O que é XP?** Ela foi concebida para melhorar a qualidade do software e a produtividade da equipe, enfatizando práticas de desenvolvimento que valorizam a simplicidade, a comunicação eficiente e a resposta rápida às mudanças.
XP tem como base cinco valores fundamentais:
1. Comunicação: Incentiva a comunicação frequente e eficiente entre todos os membros da equipe, bem como com os clientes e stakeholders, para garantir que todos entendam os requisitos e objetivos do projeto.
2. Simplicidade: Defende a ideia de que o código deve ser simples, direto e fácil de entender. A simplicidade reduz a complexidade e torna o software mais fácil de ser mantido e modificado.
3. Feedback: Busca obter feedback constante do cliente e das partes interessadas para orientar o desenvolvimento do produto. O feedback é essencial para garantir que o software atenda às necessidades reais dos usuários.
4. Coragem: Incentiva a equipe a assumir riscos calculados e a fazer mudanças necessárias, mesmo que sejam difíceis. A coragem é necessária para garantir que o software evolua de acordo com as necessidades do cliente e as mudanças do mercado.
5. Respeito: Promove o respeito mútuo entre os membros da equipe, valorizando suas contribuições e habilidades individuais.
XP se baseia em práticas específicas para apoiar esses valores, incluindo:

- Programação em Pares (Pair Programming): Dois programadores trabalham em conjunto, um escrevendo o código e o outro revisando-o em tempo real. Isso aumenta a qualidade do código e promove o compartilhamento de conhecimento.
- Testes Automatizados (Test-Driven Development - TDD): Os testes são escritos antes do código, garantindo que o software atenda aos requisitos e funcione conforme o esperado.
- Integração Contínua (Continuous Integration): As alterações de código são integradas ao repositório principal várias vezes ao dia, o que ajuda a evitar conflitos e detectar problemas rapidamente.
- Releases Pequenos e Frequentes: O software é entregue em incrementos menores e mais frequentes, permitindo que os clientes vejam resultados mais rapidamente e forneçam feedback contínuo.

O Extreme Programming é uma abordagem ágil que busca fornecer software de alta qualidade, adaptado às mudanças e que atenda às necessidades do cliente de forma eficiente. As práticas XP podem ser adaptadas e combinadas com outras metodologias ágeis para atender às necessidades específicas de cada projeto e equipe.

#### Design Sprint Google
O Design Sprint da Google é geralmente realizado em cinco etapas durante um período de cinco dias:

1. *Segunda, Entendimento*: A equipe se reúne para compreender profundamente o problema ou desafio a ser resolvido. Isso envolve a análise de informações relevantes, realização de pesquisas com usuários e a identificação das metas a serem alcançadas.
2. *Terça, Ideação*: Os membros da equipe geram uma grande quantidade de ideias para resolver o problema. Essa etapa é focada na criatividade e na diversidade de perspectivas, e nenhuma ideia é descartada inicialmente.
3. *Quarta, Decisão*: As ideias geradas são revisadas e discutidas pela equipe. Após uma análise detalhada, as melhores ideias são selecionadas e refinadas para formar uma única solução que será prototipada.
4. *Quinta, Prototipagem*: Com a solução escolhida, a equipe cria um protótipo de baixa fidelidade que simula o funcionamento da solução final. O protótipo pode ser feito de várias formas, como desenhos, wireframes, maquetes ou mesmo um protótipo digital interativo.
5. *Sexta, Teste*: O protótipo é testado com usuários reais para obter feedback valioso. Esses testes podem ser feitos em pessoas que fazem parte do público-alvo do produto ou serviço. O objetivo é validar a solução, identificar possíveis problemas e fazer ajustes antes de iniciar a implementação completa.
Ela permite que as equipes superem a indecisão, economizem tempo e recursos e obtenham insights valiosos dos usuários antes de comprometerem-se com a implementação completa de uma ideia. Além disso, essa abordagem ajuda a eliminar suposições e riscos, uma vez que as decisões são baseadas em testes reais.

#### Modelo Spotify Squads
O modelo se baseia em um conjunto de princípios ágeis e é projetado para se adaptar às necessidades e tamanho da organização, promovendo a descentralização do poder de decisão e a capacidade de resposta rápida às mudanças.
Os principais componentes do Modelo Spotify Squads são:

- Squads: São equipes pequenas e multidisciplinares, compostas por profissionais de diferentes áreas, como desenvolvedores, designers e especialistas em produto. Cada Squad é responsável por uma parte específica do produto ou funcionalidade.
- Tribes (Tribos): São agrupamentos de Squads que compartilham um propósito comum, geralmente relacionado a uma área ou tema específico. As Tribes são formadas para promover a colaboração entre equipes que trabalham em áreas relacionadas.
- Chapters (Capítulos): São comunidades de profissionais que compartilham a mesma especialidade, independentemente de estarem em Squads ou Tribes diferentes. Os Capítulos ajudam a garantir o crescimento profissional e o intercâmbio de conhecimento entre os membros.
- Guilds (Guildas): São grupos de interesse ou comunidades de prática que reúnem pessoas de diferentes Tribes e Capítulos que têm interesses ou habilidades comuns. As Guilds promovem a colaboração e o aprendizado entre os membros.
- Tribe Leads e Squad Leads: São líderes que têm a responsabilidade de garantir que suas Tribes e Squads alcancem seus objetivos e forneçam valor aos clientes. Eles também atuam como facilitadores e apoiam o crescimento e o desenvolvimento das equipes.

O Modelo Spotify Squads promove uma cultura de autonomia, colaboração e aprendizado contínuo. Ele permite que as equipes sejam ágeis e responsivas às mudanças, ao mesmo tempo que mantêm um foco claro nos objetivos da empresa e nas necessidades dos clientes.

#### SMART
SMART é uma sigla utilizada para definir critérios que tornam os objetivos mais claros, específicos, mensuráveis, alcançáveis, relevantes e com prazo determinado. Essa técnica é frequentemente utilizada em gerenciamento de projetos, definição de metas pessoais e profissionais, e em diversos contextos onde é necessário estabelecer metas bem definidas.

Os elementos do SMART são os seguintes:

- Específico (Specific): O objetivo deve ser claro e específico, definindo exatamente o que será alcançado. Quanto mais claro e detalhado for o objetivo, mais fácil será entender o que precisa ser feito.
- Mensurável (Measurable): O objetivo deve ser quantificável e permitir a medição do progresso e do sucesso. Isso envolve o estabelecimento de indicadores e critérios que podem ser avaliados ao longo do tempo.
- Alcançável (Attainable): O objetivo deve ser realista e alcançável, considerando os recursos disponíveis, o conhecimento e as habilidades da equipe ou pessoa envolvida.
- Relevante (Relevant): O objetivo deve ser relevante e estar alinhado com os objetivos gerais do projeto ou da pessoa. Ele deve fazer sentido e ter um impacto significativo.
- Tempo-bound (Time-bound): O objetivo deve ter um prazo definido para sua conclusão. Um prazo estabelecido ajuda a criar um senso de urgência e a manter o foco na realização do objetivo dentro de um período determinado.

Um exemplo de objetivo SMART seria: "Aumentar as vendas da empresa em 10% nos próximos seis meses, através da implementação de uma estratégia de marketing digital focada em atrair novos clientes".
Ao usar o SMART para definir objetivos, fica mais fácil planejar e medir o progresso, além de aumentar as chances de sucesso ao garantir que os objetivos sejam claros, realistas e orientados para resultados concretos.

#### Ferramentas de projetos para usar em métodos ágeis
**brainstroming**: é uma técnica de geração de ideias em grupo, utilizada para promover a criatividade e a solução de problemas de forma colaborativa. Nesse processo, os participantes são incentivados a expressar livremente suas ideias, sem julgamentos ou críticas, com o objetivo de gerar o maior número possível de sugestões e alternativas. O brainstorming geralmente é conduzido da seguinte forma, definição do problema, regras, geração de ideias, divergência e convergência, consolidação.

É uma técnica amplamente utilizada em equipes de trabalho, sessões de inovação, resolução de problemas, desenvolvimento de projetos e tomada de decisões, ajudando a desbloquear a criatividade e a explorar novas possibilidades.

**Moodboard**: 
É uma ferramenta visual usada para representar a aparência e a sensação de um projeto ou conceito de forma rápida e eficiente. É uma coleção organizada de imagens, cores, texturas, fontes e outros elementos visuais que capturam a atmosfera, o estilo e a temática de um determinado projeto.
O objetivo do Moodboard é fornecer uma referência visual clara e compartilhar a visão do projeto com outras pessoas envolvidas, como clientes, designers, equipes de marketing e desenvolvedores. Ele ajuda a criar uma linguagem visual comum e a estabelecer uma direção estética para o projeto, garantindo que todas as partes interessadas estejam alinhadas com o mesmo conceito. Para projetos de design gráfico, branding, websites, decoração de interiores e planejamento de eventos, o Moodboard pode incluir, paleta de cores, imagens e fotografias, tipografia, texturas e padrões, elementos gráficos, logotipos e marcas e o que mais for necessario, mas de forma que não tenha poluições visuais que atarpalhem a compreenção.

Ao criar um Moodboard, é importante garantir que as imagens e elementos visuais selecionados estejam alinhados com a visão do projeto e transmitam a mensagem correta aos envolvidos. Ele serve como uma ferramenta poderosa para a comunicação visual, facilitando o processo de desenvolvimento e permitindo que todas as partes interessadas tenham uma visão clara e compartilhada do conceito a ser criado.

**Mapa Mental**: 

As características principais dos mapas mentais de Tony Buzan são:

- Centralidade: O mapa mental começa com uma palavra ou imagem central que representa o tema ou conceito principal. Essa palavra ou imagem fica no centro do mapa.
- Associatividade: Os ramos do mapa mental são conectados à ideia central através de linhas curvas, que representam as associações e conexões entre os diferentes elementos.
- Palavras-chave: O mapa mental usa palavras-chave e frases curtas para representar as informações. Buzan acreditava que as palavras-chave eram mais eficazes para estimular a memória e a compreensão do que frases longas e textos completos.
- Imagens e cores: Buzan enfatizou o uso de imagens e cores no mapa mental para torná-lo mais visualmente atraente e facilitar a memorização e a criatividade.
- Hierarquia e ramificação: O mapa mental segue uma estrutura hierárquica, com ramificações que representam subtemas ou conceitos relacionados.

A técnica do mapa mental de Tony Buzan se tornou amplamente popular e é amplamente utilizada em diversas áreas, como educação, negócios, planejamento, resolução de problemas, anotações, entre outros. Sua abordagem proporcionou uma maneira eficaz de organizar e explorar informações de forma criativa, tornando-se uma ferramenta valiosa para melhorar a aprendizagem e a produtividade.

**Persona e Mapa de Empatia**:

- Persona é uma representação fictícia e detalhada de um cliente ideal ou usuário típico do produto ou serviço que está sendo desenvolvido. É uma técnica de criação de personagens que ajuda a humanizar e personificar os dados demográficos e comportamentais do público-alvo.
- Mapa de Empatia é uma ferramenta visual que ajuda a compreender melhor as necessidades, desejos, emoções e comportamentos do público-alvo. Ele coloca o criador no lugar do cliente ou usuário, permitindo que ele entenda suas perspectivas, motivações e frustrações.

**Grupos de Usuários**

São os conjuntos específicos de pessoas ou indivíduos que compartilham interesses, necessidades ou características comuns em relação a um determinado produto, serviço ou projeto. Esses grupos desempenham um papel essencial na análise, desenvolvimento e melhoria contínua de produtos e serviços.

**Jornada do Usuário**

A jornada do usuário é uma ferramenta valiosa para compreender a perspectiva e a experiência do cliente, permitindo que as empresas identifiquem pontos de contato críticos e oportunidades de melhoria em todo o ciclo de vida do cliente. Ela é frequentemente utilizada em marketing, UX e desenvolvimento de produtos, com o objetivo de criar uma experiência mais positiva e satisfatória para o cliente. Ao mapear a jornada do usuário, as empresas podem identificar pontos de farqueza, fricção ou insatisfação ao longo do processo e, assim, implementar melhorias para aprimorar a experiência do cliente. A compreensão dessas etapas também ajuda na criação de estratégias mais eficazes de marketing, atendimento ao cliente e desenvolvimento de produtos, contribuindo para a conquista e retenção de clientes.

**storyboard**

Um storyboard, usado muito na gestão de projetos é uma sequência de ilustrações ou esboços organizados em uma estrutura visual, semelhante a um quadrinho, usado para planejar ou contar uma história, é uma forma de pré-visualização, onde as cenas são representadas em uma sequência lógica para comunicar a história. É uma ferramenta essencialmente visual que ajuda a visualizar uma narrativa, seja para filmes, animações, vídeos, quadrinhos, jogos, telas de sites ou qualquer outra forma de mídia que envolva uma sequência de eventos ou cenas. Ele permite que a equipe criativa tenha uma visão geral do projeto antes de iniciar a produção completa em qualquer etapa do projeto, ajudando a economizar tempo e recursos ao planejar cuidadosamente cada aspecto da história.

# Sprints
# 1. Sprint 1
[Link para certificados e arquivos da sprint 1](https://github.com/cairodasilvapinto/bolsaCOMPASS/tree/main/SPRINT1)
## Git e GitHub do básico ao avançado (c/ gist e GitHub Pages)

**O que é um repositorio?** e para que serve?* Um repositório é um espaço onde são armazenados os arquivos e as informações relacionadas a um projeto ou sistema de controle de versão, como o Git. Ele contém todo o histórico de alterações (commits), bem como as diferentes versões dos arquivos que compõem o projeto. São essenciais para facilitar a colaboração em equipe e manter o controle de versões de um projeto. Eles são fundamentais para o desenvolvimento de software colaborativo, pois permitem que várias pessoas trabalhem no mesmo projeto sem interferir no trabalho umas das outras.

**O que é git?** É um sistema de controle de versão utilizado para o gerenciamento eficiente e seguro de projetos de desenvolvimento de software. Criado em 2005 por Linus Torvalds, o mesmo criador do kernel do Linux, e desde então se tornou um dos sistemas de controle de versão mais populares do mundo.

**O que é github?** O GitHub é uma plataforma de hospedagem e colaboração de código-fonte baseada em Git. Ele fornece uma plataforma na nuvem onde desenvolvedores e equipes podem armazenar, gerenciar e compartilhar seus repositórios Git, facilitando muito o tarbalho de desenvolvimento e controle de versão, testes e etc. Ele permite hospedagem de repositorios, cotrolde de acesso e de problemas(issues), pull requests, reviews de codigo, gists e muito mais.

**O que é markdown?** Markdown é uma linguagem de marcação leve e simples, foi desenvolvida com o objetivo de ser facilmente legível e convertida para HTML sem a necessidade de ferramentas complexas ou editores especiais.

Alguns comandos mais usados do git:

`git init`                              | Inicia um novo repositório Git em um diretório local.

`git clone [URL]`                       | Clona um repositório existente para o seu computador.

`git add [arquivo]`                     | Adiciona arquivos ao índice para prepará-los para o commit.

`git commit -m "[mensagem]"`            | Registra as mudanças no repositório com uma mensagem.

`git commit -a`                         | Adiciona automaticamente todas as alterações feitas nos arquivos rastreados ao índice e cria um commit.

`git status`                            | Mostra o status atual do repositório, incluindo os arquivos modificados.

`git log`                               | Exibe o histórico de commits do repositório.

`git pull`                              | Obtém e incorpora as mudanças do repositório remoto para o branch atual.

`git branch`                            | Lista todos os branches no repositório e indica o branch atual com um asterisco.

`git branch [nome-do-branch]`           | Cria um novo branch com o nome especificado.

`git checkout [nome-do-branch]`         | Muda para o branch especificado, atualizando o diretório de trabalho.

`git merge [nome-do-branch]`            | Incorpora as alterações do branch especificado no branch atual.

`git branch -d [nome-do-branch]`        | Deleta o branch especificado. Tenha cuidado, pois essa ação é permanente.

`git push origin [nome-do-branch]`      | Envia o branch especificado para o repositório remoto.

`git pull origin [nome-do-branch]`      | Obtém e incorpora as mudanças do branch especificado do repositório remoto.

`git checkout -b [nome-do-branch]`      | Cria um novo branch com o nome especificado e muda para ele.

`git merge --no-ff [nome-do-branch]`    | Realiza um merge com criação de um commit mesmo em fast-forward.

`git diff [branch1] [branch2]`          | Exibe as diferenças entre dois branches especificados. 

`git fetch`                             | Busca todas as alterações dos branches do repositório remoto.

`git stash`                             | Armazena temporariamente as mudanças não finalizadas para limpar o diretório de trabalho e depois retomá-las posteriormente.

`git tag [nome-da-tag]`                 | Cria uma tag para marcar um ponto específico na história do repositório.

`git show [tag]`                        | Mostra as informações e mudanças associadas a uma tag específica.

`git diff [branch1] [branch2]`          | Exibe as diferenças entre dois branches especificados.

`git gc`                                | Executa a coleta de lixo no repositório, compactando e otimizando o banco de dados Git para melhorar o desempenho.

## Linux para Desenvolvedores (c/ terminal, Shell, Apache e +)
**o que é linux?**  Linux é um sistema operacional de código aberto baseado no kernel Linux, que foi criado originalmente por Linus Torvalds em 1991. O kernel Linux é o coração do sistema operacional e gerencia o acesso aos recursos de hardware, como processador, memória, dispositivos de entrada/saída e outros componentes essenciais de um computador.

O que diferencia o Linux de outros sistemas operacionais é o fato de ser um software open source. Isso significa que seu código-fonte é acessível e pode ser modificado, melhorado e distribuído livremente por qualquer pessoa sob os termos da Licença Pública Geral GNU (GPL).

Uma das características mais marcantes do Linux é sua diversidade de distribuições (distros). Diversos grupos e organizações criam e mantêm diferentes distribuições do Linux com configurações, pacotes e interfaces de usuário variadas. Algumas das distribuições Linux mais populares incluem Ubuntu, Fedora, Debian, CentOS, Linux Mint e muitas outras. Ele se destaca muito pela sua segurança, flexibilidade, estabilidade, sporte da comunidade e por ser open source.


**Quais seus principais usou?** Servidores Web, computação em nuvem, Android, desemvolvimento de software, IoT, administração de redes, supercomputadores e mais.

Alguns comandos úteis amplamente usados no terminal do Linux:

`ls`	                                  | Lista os arquivos e diretórios no diretório atual.

`cd`	                                  | Navega para outro diretório.

`pwd`	                                  | Exibe o caminho completo do diretório atual.

`mkdir`                                 | Cria um novo diretório.

`rm`                                    | Remove arquivos ou diretórios.

`cp`	                                  | Copia arquivos ou diretórios.

`mv`	                                  | Move ou renomeia arquivos ou diretórios.

`touch`	                                | Cria um novo arquivo vazio.

`cat`	                                  | Exibe o conteúdo de um arquivo no terminal.

`grep [padrão] [arquivo]`	              | Pesquisa por padrões em arquivos.

`chmod`	                                | Altera as permissões de um arquivo ou diretório.

`sudo`	                                | Executa um comando com privilégios de superusuário.

`ls -l`	                                | Lista os arquivos e diretórios com detalhes, incluindo permissões, proprietário, tamanho, etc.

`ls -a`	                                | Lista todos os arquivos e diretórios, incluindo os ocultos que começam com um ponto.

`cd ..`                                 | Navega para o diretório pai (diretório acima do diretório atual).

`tar -cvzf [arquivo.tar.gz] [arquivos]` | Cria um arquivo compactado em formato .tar.gz com os arquivos fornecidos.

`tar -xvzf [arquivo.tar.gz]`            | Extrai arquivos de um arquivo compactado em formato .tar.gz.

`zip -r [arquivo.zip] [diretório]`	    | Cria um arquivo compactado em formato .zip a partir do diretório fornecido.

`unzip [arquivo.zip]`	                  | Extrai arquivos de um arquivo compactado em formato .zip.

`df -h`	                                |  Exibe informações sobre o uso de espaço em disco de todas as partições montadas no sistema.

`free -h`	                              | Exibe informações sobre o uso de memória RAM e swap em um formato mais legível.

`ping [endereço]`	                      |  Verifica a conectividade com um determinado endereço de IP ou host.

`ctrl + c`	                            | Interrompe a execução do comando atual no terminal.

`ctrl + d`	                            |  Fecha o terminal atual (envia um sinal de fim de arquivo).

# 2. Sprint 2
[Link para certificados e arquivos da sprint 2](https://github.com/cairodasilvapinto/bolsaCOMPASS/tree/main/SPRINT2)
## Conceitos de Data & Analytics
### Big Data:
O conceito de Big Data refere-se a grandes volumes de dados que exigem formas inovadoras de processamento e podem ser usados para resolver problemas de negócios. Segundo o Gartner, Big Data é caracterizado pelos 3 Vs: volume, velocidade e variedade.

O volume diz respeito à quantidade de dados, que pode variar de terabytes a petabytes. A velocidade refere-se à velocidade com que os dados são recebidos e precisam ser processados em tempo hábil. Já a variedade diz respeito aos diferentes tipos de dados disponíveis, incluindo dados estruturados e não estruturados.

O surgimento do Big Data foi impulsionado pelo aumento da geração de dados por meio de plataformas escaláveis, como redes sociais e dispositivos conectados à Internet. O desenvolvimento de tecnologias como o Hadoop e o NoSQL facilitou o armazenamento e análise de grandes conjuntos de dados.

A importância do Big Data não está apenas na quantidade de dados que uma empresa possui, mas sim no que ela faz com esses dados. A análise de Big Data pode ajudar as empresas a reduzir custos, economizar tempo, desenvolver novos produtos, otimizar ofertas e tomar decisões mais inteligentes.

Em resumo, o Big Data é um conjunto de dados volumosos, de alta velocidade e/ou alta variedade, que requerem formas inovadoras de processamento e podem ser utilizados para obter insights e solucionar problemas de negócios
<img src="https://github.com/cairodasilvapinto/bolsaCOMPASS/assets/131769429/0b41cef2-dc7a-46ad-a007-8647e6f4d256" alt="definição dos 4 v's do big data de acordo com a visão da IBM">

### Ciência de Dados:
A Ciência de Dados é uma área interdisciplinar que envolve o estudo e a análise de dados, estruturados ou não, com o objetivo de extrair conhecimento e insights para tomadas de decisão. Ela combina técnicas de análise de dados, como mineração de dados e aprendizado de máquina, com conhecimentos de estatística, matemática, ciência da computação e outras disciplinas relacionadas.

A Ciência de Dados é impulsionada pelo surgimento do Big Data, que proporciona o acesso a grandes volumes de dados de diversas fontes, como redes sociais, dispositivos conectados e transações comerciais. Esses dados são processados e analisados para identificar padrões, tendências e relações que possam ser utilizados para melhorar processos, desenvolver produtos, otimizar estratégias de negócios e tomar decisões mais informadas.

Os profissionais de Ciência de Dados, conhecidos como Cientistas de Dados, possuem uma ampla gama de habilidades, incluindo conhecimentos em programação, estatística, modelagem, análise de dados, machine learning e bancos de dados. Eles trabalham em colaboração com equipes multidisciplinares, como engenheiros de dados, arquitetos de soluções e desenvolvedores, para coletar, limpar, processar e analisar os dados de forma eficiente.

A Ciência de Dados tem se tornado cada vez mais relevante para as empresas, pois permite transformar grandes quantidades de dados brutos em insights valiosos. Com esses insights, as empresas podem tomar decisões mais embasadas, identificar oportunidades de negócio, melhorar a eficiência operacional e oferecer produtos e serviços mais personalizados aos clientes.

Em resumo, a Ciência de Dados é uma disciplina que utiliza técnicas de análise de dados para extrair conhecimento e insights a partir de grandes volumes de dados, com o objetivo de melhorar processos, tomar decisões mais informadas e impulsionar o sucesso das empresas.

### Diferença entre papeis envolvidos em Big Data:
A diferenciação entre os diferentes papéis envolvidos no campo do Big Data. O principal papel discutido é o do Cientista de Dados, que é um profissional com uma sólida formação em áreas como ciência da computação, estatística, modelagem, análise de dados, matemática, machine learning, entre outros.

O Cientista de Dados é responsável por lidar com a vasta quantidade de conhecimentos necessários para trabalhar com Big Data, e pode ter especializações em áreas específicas de interesse, o que facilita a estruturação de trilhas de estudos.

Além do Cientista de Dados, existem outros papéis importantes no processamento e análise de dados, como o Arquiteto de Soluções para Dados, o Engenheiro de Dados e os Desenvolvedores. O Arquiteto de Soluções para Dados é responsável por projetar e implementar a infraestrutura necessária para o processamento e armazenamento de dados. O Engenheiro de Dados é responsável por coletar, limpar e transformar os dados para que possam ser utilizados na análise. Os Desenvolvedores são responsáveis por criar e implementar algoritmos e modelos de análise de dados.

Esses diferentes papéis trabalham em colaboração para coletar, processar, analisar e interpretar os dados, a fim de extrair insights e conhecimentos valiosos para as empresas. Cada papel desempenha uma função específica e contribui para o sucesso do projeto de Big Data.

### Tipos de Dados (estruturado, semi e não estruturado):
Existem três principais tipos de dados: estruturados, semi-estruturados e não estruturados.

Dados estruturados são aqueles que possuem uma organização predefinida e seguem um formato específico. Eles são armazenados em tabelas com colunas e linhas, como em um banco de dados relacional. Exemplos de dados estruturados incluem informações em planilhas, registros em bancos de dados e dados numéricos.

Dados semi-estruturados são aqueles que não possuem uma estrutura rígida, mas ainda possuem algum nível de organização. Eles podem ser representados em formatos como XML (Extensible Markup Language) e JSON (JavaScript Object Notation). Esses formatos permitem que os dados sejam agrupados e organizados de forma hierárquica, mas sem a necessidade de uma estrutura fixa. Exemplos de dados semi-estruturados incluem documentos HTML, feeds de RSS e arquivos de log.

Dados não estruturados são aqueles que não possuem uma estrutura definida e não podem ser facilmente organizados em tabelas ou formatos hierárquicos. Eles são mais complexos de serem processados e analisados, pois podem incluir texto livre, imagens, áudio, vídeo e outros tipos de mídia. Exemplos de dados não estruturados incluem e-mails, posts em redes sociais, vídeos do YouTube e imagens digitais.

A compreensão dos diferentes tipos de dados é fundamental para o processamento e análise eficiente de Big Data, pois cada tipo requer abordagens e técnicas específicas. A capacidade de lidar com dados estruturados, semi-estruturados e não estruturados é essencial para extrair insights valiosos e tomar decisões informadas a partir de grandes volumes de dados.

### Banco de dados (RDBMS vs NoSQL):
A diferenças entre os bancos de dados relacionais (RDBMS) e os bancos de dados NoSQL. Os bancos de dados relacionais seguem o modelo relacional de dados, com tabelas, colunas e relacionamentos definidos. Eles são adequados para aplicações que exigem consistência transacional e consultas complexas. Exemplos de bancos de dados relacionais incluem MySQL, Oracle e SQL Server.

Por outro lado, os bancos de dados NoSQL são projetados para atender às necessidades de aplicações que exigem escalabilidade horizontal, desempenho superior e flexibilidade de esquema. Eles não seguem o modelo relacional e podem ser classificados em diferentes tipos, como chave-valor, orientado a documentos, orientado a colunas e orientado a grafos. Exemplos de bancos de dados NoSQL incluem MongoDB, Cassandra e Redis.

Uma das principais diferenças entre os dois tipos de bancos de dados é a linguagem de consulta. Os bancos de dados relacionais utilizam a linguagem SQL (Structured Query Language), que é uma linguagem de consulta estruturada e amplamente conhecida. Já os bancos de dados NoSQL podem ter suas próprias linguagens de consulta ou podem usar formatos como JSON para consultas.

Outra diferença significativa é o modelo de consistência. Os bancos de dados relacionais seguem o modelo ACID (Atomicidade, Consistência, Isolamento e Durabilidade), que garante transações completas e consistentes. Já os bancos de dados NoSQL geralmente seguem o modelo BASE (Basicamente Disponível, Estado Leve e Eventualmente Consistente), que prioriza a disponibilidade e a escalabilidade em detrimento da consistência imediata.

A escolha entre um banco de dados relacional e um banco de dados NoSQL depende das necessidades específicas da aplicação. Os bancos de dados relacionais são mais adequados para aplicações com transações complexas e necessidade de consistência transacional. Já os bancos de dados NoSQL são mais adequados para aplicações que exigem escalabilidade horizontal.

### Tipos de armazenamentos de dados:
Existem diferentes formatos utilizados para armazenar dados em arquivos. Alguns dos formatos mais comuns incluem TXT, CSV, XML, JSON, ORC, PARQUET e AVRO.

O formato TXT é um arquivo de texto simples, que pode ser lido e aberto por qualquer programa que leia texto. É facilmente editável, permitindo alterações diretas no conteúdo.

O formato CSV (Comma-Separated Values) é um arquivo de texto delimitado que usa vírgulas para separar os valores. É amplamente utilizado para armazenar dados tabulares, com cada linha representando um registro e os campos separados por vírgulas.

O formato XML (Extensible Markup Language) é um formato de arquivo de texto que utiliza uma linguagem de marcação para organizar dados hierarquicamente. É comumente usado para criar documentos com dados estruturados, como texto formatado, imagens vetoriais ou bancos de dados.

O formato JSON (JavaScript Object Notation) é um formato de arquivo de texto que utiliza uma sintaxe leve para representar dados estruturados. É amplamente utilizado para armazenar e transmitir dados entre sistemas, sendo especialmente adequado para aplicações web.

Os formatos ORC, PARQUET e AVRO são formatos de armazenamento de dados otimizados para processamento e análise eficientes em sistemas de Big Data. Esses formatos oferecem compressão, particionamento e esquemas de dados avançados, permitindo consultas rápidas e eficientes em grandes volumes de dados.

### Data Lake (Arquitetura Lambda):
A arquitetura Lambda proposta por Nathan Marz é um modelo teórico para a construção de sistemas de Big Data. Essa arquitetura é dividida em três camadas: batch layer, speed layer e serving layer. Na batch layer, os dados são armazenados de forma atômica e processados para gerar visualizações pré-calculadas. A speed layer processa os dados em tempo real e os disponibiliza enquanto aguarda a atualização da batch layer. A serving layer fornece acesso aos dados processados para os sistemas finais. Essa arquitetura permite processar grandes volumes de dados, manter a estrutura original dos dados na batch layer e entregar informações em tempo real através da speed layer.

### Técnicas para Processamento de Dados
O processamento de dados pode ser feito em lote(Batch) ou em fluxo(stream). O processamento em lote ocorre em blocos de dados que já foram armazenados durante um período de tempo e é comumente usado para transferir dados ou processar dados com transformações. O processamento de fluxo, por outro lado, trabalha com fluxos de dados que são capturados em tempo real e processados com latência mínima para o sistema de destino. Ele é usado na busca por resultados analíticos em tempo real.

### Business Intelligence (BI)
Business Intelligence (BI) é um conjunto de teorias, metodologias, práticas, tecnologias e estruturas para desenvolver uma inteligência no negócio. É um termo abrangente que inclui aplicações, infraestrutura, ferramentas e boas práticas que permitem o acesso e a análise de informações para melhorar e otimizar as decisões. As tecnologias de BI permitem a visualização do histórico das operações de negócio, assim como a visão atual e as possíveis previsões. As principais funções de um BI são relatórios, análises, mineração de dados, processamento de eventos complexos, gerenciamento de desempenho dos negócios, benchmarking e análises prescritivas.

### Data Warehouse(DW)
O Data Warehouse (DW) é um sistema de armazenamento de dados que é projetado para permitir o processamento analítico de grandes conjuntos de dados. Ele difere de um banco de dados transacional (OLTP), em que é otimizado para o desempenho de consulta e é projetado para executar consultas complicadas em grandes conjuntos de dados. O DW utiliza a modelagem dimensional, que consiste em tabelas de dimensões e fatos, que são usadas em um DW para armazenar informações para análises. O SCD (Slowly Changing Dimension) é uma técnica usada para armazenar dados históricos em um DW. Data Marts são parte do DW que é menor, focado e contém resumos de dados para atender às necessidades de uma equipe ou unidade de negócio específica.

### Mineração de Dados
Mineração de Dados é o processo de descobrir correlações, padrões e tendências significativas analisando grandes quantidades de dados armazenados em repositórios. A mineração de dados utiliza tecnologias de reconhecimento de padrões, bem como técnicas estatísticas e matemáticas. A tecnologia de mineração de dados tem uma longa história e é baseada em três disciplinas científicas entrelaçadas: estatística, inteligência artificial e machine learning. A mineração de dados é usada para descobrir conexões escondidas e prever tendências futuras. A diferença entre mineração de dados e ciência de dados é que a última possui uma profundidade maior.

### Machine Learning
Machine Learning (ML) é um tipo de inteligência artificial que permite que um sistema aprenda com dados em vez de ser explicitamente programado. Ele requer grande quantidade de dados e utiliza técnicas estatísticas e algoritmos para analisá-los e encontrar padrões. O aprendizado é dividido em três tipos: supervisionado, não supervisionado e por reforço. O aprendizado supervisionado é treinado com dados rotulados, enquanto o não supervisionado é treinado sem dados rotulados e o semi-supervisionado utiliza ambos. O aprendizado por reforço é usado em jogos, robótica e navegação. As principais técnicas de Machine Learning incluem regressão, classificação, agrupamento e redes neurais. O ML tem aplicação em áreas como recomendações personalizadas, reconhecimento de padrões e detecção de fraudes.

### Deep Learning
Deep Learning é um subcampo de Machine Learning que utiliza algoritmos de redes neurais artificiais para aprender diretamente a partir de dados, sem depender de regras heurísticas complexas. As redes neurais artificiais são compostas por várias camadas e cada camada extrai características cada vez mais abstratas dos dados. O Deep Learning é usado em tarefas tais como detecção de objetos em imagens e vídeos, tradução de idiomas, reconhecimento de fala e autônoma de veículos. O Deep Learning opera com grandes quantidades de dados e requer grandes quantidades de poder de processamento, o que o torna possível graças a TPU (Tensor Processing Unit), um processador desenvolvido especificamente para computação de IA, bem como tecnologias como GPUs, que apoiam grande poder de processamento em ambientes de desktop.

### Relatórios
Conceito bastante conhecido, porém muitas pessoas confundem e criam gráficos acreditando que estão fazendo relatórios. Relatório é um documento que apresenta informações em um formato organizado para um público específico e propósito. Embora os resumos dos relatórios possam ser entregues oralmente, os relatórios completos são quase sempre na forma de documentos escritos.

### Dashboards
Dashboards, também conhecidos como painéis de dados, são uma importante ferramenta para gerenciamento de informações que analisa e exibe os principais indicadores de desempenho, ou do inglês Key Performance Indicators (KPI) e métricas principais, para monitorar a integridade de uma empresa, departamento ou processo específico. Eles são personalizáveis para atender às necessidades específicas de um departamento e/ou empresa e podem ser compostos por gráficos, tabelas, e outras formas de visualização. Dashboards utilizam um painel que se conecta a seus arquivos, anexos, serviços e APIs, exibindo todos esses dados de forma visualmente organizada.

### Internet das coisas (IoT)
Internet das coisas (IoT) é uma rede de objetos físicos que contém tecnologia embarcada para comunicar, sentir ou interagir com seus estados internos ou com o ambiente externo. Por exemplo, veículos, jogos eletrônicos, edifícios, câmeras, sensores e outros dispositivos dotados de tecnologia embarcada podem coletar e transmitir dados. A IoT é usada em diversos setores, incluindo saúde, agricultura, transporte e manufatura, para tornar as atividades mais eficientes. A IoT também tem potencial para ser uma ferramenta para melhorar a qualidade de vida das pessoas, fornecendo soluções para questões relacionadas a saúde, segurança e bem-estar.

### API
Uma API (Application Programming Interface) é um conjunto de rotinas, protocolos e ferramentas para criar aplicativos de software. Basicamente, uma API especifica como os componentes de software devem interagir. As APIs são compostas de dois elementos: uma especificação que descreve como as informações são trocadas entre os programas, realizadas através de um request/solicitação de processamento e retornando os dados solicitados, e uma interface de software escrita para que essa especificação esteja publicada de alguma forma para que o uso ocorra da forma correta. APIs são importantes para que um sistema interaja com outros sistemas sempre do mesmo formato. Existem três tipos básicos de APIs: local, web-like e program-like, cada um com diferentes funcionalidades e características.

### Métodos de acesso à Banco de Dados
Os métodos de acesso a bancos de dados têm evoluído para soluções mais padronizadas e universais de acordo com as necessidades dos usuários. Historicamente, várias linguagens e APIs de programação próprias de cada fornecedor estavam disponíveis, tornando necessária a aprendizagem de cada uma delas para se comunicar com as diferentes bases de dados existentes. Esse cenário mudou com a criação de uma linguagem padrão única de acesso através do consórcio SAG (Standard Query Language Access Group) que culminou na elaboração do SQL CLI (Standard Query Language Call Level Interface). A interface procedural CLI não é uma nova linguagem de consulta, mas um envoltório para o SQL, permitindo que aplicações se comuniquem com um sistema gerenciador de banco de dados por meio de chamadas CLI. A API ODBC (Open Database Connectivity) da Microsoft foi criada para permitir que uma aplicação cliente acesse diferentes bases de dados através de drivers correspondentes, fornecendo uma maneira comum de acesso usando SQL (ODBC Driver Manager).


### SQL para Análise de Dados: Do Basico ao avançado
#### Comandos básicos
**Select**:
```sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
```
- Comando usado para selecionar colunas de tabelas
- Quando selecionar mais de uma coluna, elas devem ser separadas por vírgula sem conter virgula antes do comando FROM
- Pode-se utilizar o asterisco (*) para selecionar todas as colunas da tabela.
  
**Distinct**:
```sql
select distinct coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
```
- Comando usado para remover linhas duplicadas e mostrar apenas linhas distintas
- Muito utilizado na etapa de exploração dos dados
- Caso mais de uma coluna seja selecionada, o comando SELECT DISTINCT irá retornar todas as combinações distintas.

**Where**:
```sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x
```
- Comando utilizado para filtrar linhas de acordo com uma condição
- No PostgreSQL são utilizadas aspas simples para delimitar strings
- string = sequência de caracteres = texto
- Pode-se combinar mais de uma condição utilizando os operadores lógicos
- No PostgreSQL as datas são escritas no formato 'YYYY-MM-DD' ou 'YYYYMMDD'

**Order by**:

select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x=true
order by coluna_1
```
- Comando utilizado para ordenar a seleção de acordo com uma regra definida
- Por padrão o comando ordena na ordem crescente. Para mudar para a ordem decrescente usar o comando DESC
- No caso de strings a ordenação será seguirá a ordem alfabetica

**Limit**
```sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condilção_x=true
order by coluna_1
limit N
```
- Comando utilizado para limitar o nº de linhas da consulta.
- Muito utilizado na etapa de exploração dos dados
- Muito utilizado em conjunto com o comando ORDER BY quando o que importa são os TOP N. Ex: "N pagamentos mais recentes", "N produtos mais caros"

#### Operadores
<img src="https://github.com/cairodasilvapinto/bolsaCOMPASS/assets/131769429/82416285-1ed1-499e-a7e1-495cb7a3c46a" alt="operadores aritméticos, de comparação e lógicos em SQL" width="450">  

#### Funções agregadas
São funções que pertimem calcular um conjunto de valores e retornar um unico valor.
- Servem para executar operações aritmética nos registros de uma coluna.
- Funções agregadas não computam células vazias (NULL) como zero.
- Na função COUNT() pode-se utilizar o asterisco (*) para contar os registros.
- COUNT(DISTINCT ) irá contar apenas os valores exclusivos.
- COUNT(): Retorna o número de linhas (registros) em um grupo ou conjunto de dados.
- SUM(): Retorna a soma dos valores em uma coluna numérica.
- AVG(): Retorna a média dos valores em uma coluna numérica.
- MIN(): Retorna o menor valor em uma coluna.
- MAX(): Retorna o maior valor em uma coluna.


**Group by**:
- Serve para agrupar registros semelhantes de uma coluna. 
- Normalmente utilizado em conjunto com as Funções de agregação.
- Pode-se referenciar a coluna a ser agrupada pela sua posição ordinal.
- (ex: GROUP BY 1,2,3 irá agrupar pelas 3 primeiras colunas da tabela).
- O GROUP BY sozinho funciona como um DISTINCT, eliminando linhas duplicadas.
```sql
-- (Exemplo) Contagem agrupada de várias colunas
-- Calcule o nº de clientes por estado e status profissional 
select state, professional_status, count(*) as contagem
from sales.customers
group by 1, 2
order by state, contagem desc
```

**Having**:
- Serve para filtrar linhas da seleção por uma coluna agrupada
- Tem a mesma função do WHERE mas pode ser usado para filtrar os resultados 
- das funções agregadas enquanto o WHERE possui essa limitação
- A função HAVING também pode filtrar colunas não agregadas
```sql
-- (Exemplo) seleção com filtro no HAVING 
-- Calcule o nº de clientes por estado filtrando apenas estados acima de 100 clientes
select 
    state, 
    count(*)
from sales.customers
group by state
having count(*) > 100
```
							
<img src="https://github.com/cairodasilvapinto/bolsaCOMPASS/assets/131769429/863e1263-737a-401c-bd47-211cfe6092ee" alt="Tipos de Joins em SQL" width="700">

<img src="https://github.com/cairodasilvapinto/bolsaCOMPASS/assets/131769429/51c8b966-7885-45d6-b45a-9b8d271348f2" alt="Tipos de Unions" wifdth="700">

```sql									
-- (Exemplo 1) Subquery no WHERE
-- Informe qual é o veículo mais barato da tabela products

select *
from sales.products
where price = (select min(price) from sales.products)


-- (Exemplo 2) Subquery com WITH
-- Calcule a idade média dos clientes por status profissional
with alguma_tabela as (
select
	professional_status,
	(current_date - birth_date)/365 as idade
from sales.customers
)

select
	professional_status,
	avg(idade) as idade_media
from alguma_tabela
group by professional_status


-- (Exemplo 3) Subquery no FROM
-- Calcule a média de idades dos clientes por status profissional
select
	professional_status,
	avg(idade) as idade_media
from (
		select
			professional_status,
			(current_date - birth_date)/365 as idade
		from sales.customers
	 ) as alguma_tabela
group by professional_status


-- (Exemplo 4) Subquery no SELECT
-- Na tabela sales.funnel crie uma coluna que informe o nº de visitas acumuladas 
-- que a loja visitada recebeu até o momento

select
	fun.visit_id,
	fun.visit_page_date,
	sto.store_name,
	(
		select count(*)
		from sales.funnel as fun2
		where fun2.visit_page_date <= fun.visit_page_date
			and fun2.store_id = fun.store_id
	) as visitas_acumuladas
from sales.funnel as fun
left join sales.stores as sto
	on fun.store_id = sto.store_id
order by sto.store_name, fun.visit_page_date


-- RESUMO ##########################################################################
-- (1) Servem para consultar dados de outras consultas.
-- (2) Para que as subqueries no WHERE e no SELECT funcionem, elas devem retornar 
-- apenas um único valor
-- (3) Não é recomendado utilizar subqueries diretamente dentro do FROM pois isso 
-- dificulta a legibilidade da query.
```
#### Tratamento de Dados
<img src="https://github.com/cairodasilvapinto/bolsaCOMPASS/assets/131769429/0f7ca065-eff2-4c0d-9da8-ff59094395c3" alt="Lista de Unidades" wifdth="700">

**Tratamento de Dados Geral**:
- CASE WHEN é o comando utilizado para criar respostas específicas para diferentes condições e é muito utilizado para fazer agrupamento de dados.
- COALESCE é o comando utilizado para preencher campos nulos com o primeiro valor não nulo de uma sequência de valores.

**Tratamento de Texto**:
- LOWER() é utilizado para transformar todo texto em letras minúsculas.
- UPPER() é utilizado para transformar todo texto em letras maiúsculas.
- TRIM() é utilizado para remover os espaços das extremidades de um texto.
- REPLACE() é utilizado para substituir uma string por outra string.

**Tratamento de Datas**:
- O comando INTERVAL é utilizado para somar datas na unidade desejada. Caso a unidade não seja informada, o SQL irá entender que a soma foi feita em dias.
- O comando DATE_TRUNC é utilizado para truncar uma data no início do período.
- O comando EXTRACT é utilizado para extrair unidades de uma data/timestamp.
- O cálculo da diferença entre datas com o operador de subtração (-) retorna valores em dias. Para calcular a diferença entre datas em outra unidade é necessário fazer uma transformação de unidades (ou criar uma função para isso).
- Utilize o Guia de comandos para consultar as unidades de data e hora utilizadas no SQL.
  
**Funções**:
- Servem para criar comandos personalizados de scripts usados recorrentemente.
- Para criar funções, utiliza-se o comando CREATE FUNCTION.
- Para que o comando funcione é obrigatório informar (a) quais as unidades dos INPUTS (b) quais as unidades dos OUTPUTS e (c) em qual linguagem a função será escrita.
- O script da função deve estar delimitado por $$.
- Para deletar uma função utiliza-se o comando DROP FUNCTION.

#### Manipulação de Tabelas
**Criação e Deleção de Tabelas**:
- Para criar tabelas a partir de uma query basta escrever a query normalmente e colocar o comando INTO antes do FROM informando o schema e o nome da tabela  a ser criada.
- Para criar tabelas a partir do zero é necessário (a) criar uma tabela vazia  com o comando CREATE TABLE (b) Informar que valores serão inseridos com o comando INSERT INTO seguido do nome das colunas (c) Inserir os valores manualmente em forma de lista após o comando VALUES.
- Para deletar uma tabela utiliza-se o comando DROP TABLE.
  
**Inserção e Atualização de Linhas**:
- Para inserir linhas em uma tabela é necessário (a) Informar que valores serão inseridos com o comando INSERT INTO seguido do nome da tabela e nome das colunas (b) Inserir os valores manualmente em forma de lista após o comando VALUES
- Para atualizar as linhas de uma tabela é necessário (a) Informar qual tabela será atualizada com o comando UPDATE (b) Informar qual o novo valor com o comando SET (c) Delimitar qual linha será modificada utilizando o filtro WHERE
- Para deletar linhas de uma tabela é necessário (a) Informar de qual tabela as linhas serão deletadas com o comando DELETE FROM (b) Delimitar qual linha será deletada utilizando o filtro WHERE.

**Inserção e Atualização de Colunas**:

- Para fazer qualquer modificação nas colunas de uma tabela utiliza-se o comando ALTER TABLE seguido do nome da tabela.
- Para adicionar colunas utiliza-se o comando ADD seguido do nome da coluna e da unidade da nova coluna.
- Para mudar o tipo de unidade de uma coluna utiliza-se o comando ALTER COLUMN.
- Para renomear uma coluna utiliza-se o comando RENAME COLUMN.
- Para deletar uma coluna utiliza-se o comando DROP COLUMN.
  
  [link para os projetos de SQL para Análise de Dados: Do básico ao avançado]()

# 3. Sprint 3
[Documentação do python](https://docs.python.org/3/)

# 4. Sprint 4
## Programação Fundamental
A programação funcional é um paradigma de programação que se concentra na construção de software por meio da composição de funções puras, evitando o compartilhamento de estados mutáveis e efeitos colaterais. Em vez de dar instruções passo a passo sobre como realizar uma tarefa, a programação funcional se baseia na declaração de lógica e comportamento, permitindo que o sistema determine como realizar as operações.

Esse paradigma tem suas raízes na matemática e na teoria dos números, onde os matemáticos lidam com abstrações complexas por meio de funções. A programação funcional adota essa abordagem, onde as funções desempenham um papel central na representação de abstrações e comportamentos.

Alguns conceitos fundamentais da programação funcional incluem:

- Composição de Funções: A programação funcional incentiva a criação de novas funções combinando funções existentes. Isso é feito por meio da aplicação sequencial de funções para transformar dados. Por exemplo, filtrar um array de números pares e, em seguida, multiplicar cada número por dois.

- Funções Puras: Uma função é considerada pura quando, ao ser invocada várias vezes com os mesmos argumentos, produz o mesmo resultado sem causar efeitos colaterais. Isso significa que a função não depende de dados mutáveis externos e não altera nenhum estado global.

- Imutabilidade: A imutabilidade refere-se à característica de que, uma vez que um valor é atribuído a uma variável, ele não pode ser alterado. Isso promove a consistência e evita efeitos colaterais indesejados.

- Efeitos Colaterais: Efeitos colaterais ocorrem quando uma função modifica o estado de algo fora de seu escopo ou realiza ações imprevisíveis, como acessar bancos de dados ou alterar variáveis globais. A programação funcional busca minimizar os efeitos colaterais.

- Programação Declarativa: Ao contrário da abordagem imperativa, que descreve explicitamente os passos para alcançar um resultado, a programação declarativa foca em descrever o que deve ser feito, permitindo que o sistema decida como fazer isso.

Estado Compartilhado: O estado compartilhado ocorre quando um valor é acessível por várias partes do programa. A programação funcional busca limitar o uso de estados compartilhados, favorecendo a imutabilidade e a passagem de dados como argumentos para funções.

- A abordagem funcional pode levar a um código mais conciso, modular, testável e compreensível. Ela é amplamente utilizada em linguagens de programação como Haskell, Scala, Clojure e também é aplicada em outras linguagens como JavaScript, por meio de suas características funcionais.

No geral, a programação funcional busca criar software robusto e confiável ao reduzir a complexidade por meio da composição de funções puras e ao minimizar os efeitos colaterais e o compartilhamento de estados mutáveis.



## **Docker** O que é uma imagem e um conteiner?

Uma imagem no Docker é uma espécie de modelo ou pacote que contém um sistema de arquivos completo, incluindo código-fonte, bibliotecas, dependências, configurações e tudo o que é necessário para executar um software. Ela é uma representação estática e imutável de um ambiente de execução.

As imagens Docker são construídas a partir de um arquivo chamado Dockerfile, que contém as instruções para montar o ambiente desejado. Isso inclui a base da imagem (geralmente uma distribuição Linux), as dependências do aplicativo e as configurações necessárias. Quando o Dockerfile é processado, ele gera uma imagem que pode ser usada para criar contêineres.

Um contêiner Docker é uma instância em execução de uma imagem. Os contêineres são isolados uns dos outros e do sistema host, permitindo que você execute aplicativos em um ambiente consistente e confinado. Cada contêiner compartilha o mesmo sistema operacional do host, mas possui seu próprio sistema de arquivos e recursos isolados.

As imagens Docker são essenciais para a abordagem de virtualização baseada em contêineres do Docker, pois fornecem portabilidade, escalabilidade e consistência para aplicativos em diferentes ambientes. Eles facilitam a distribuição de aplicativos, pois os desenvolvedores podem criar uma imagem, compartilhá-la por meio de um registro de contêineres (como o Docker Hub) e, em seguida, outros podem usar essa imagem para executar o aplicativo em seus próprios ambientes de maneira confiável e replicável.

## o que é Volumes?

No Docker, um volume é um recurso que permite persistir e compartilhar dados entre contêineres e o sistema operacional host. Ele fornece um método flexível e eficaz para gerenciar dados que precisam ser mantidos mesmo quando os contêineres são interrompidos ou removidos.

Os volumes no Docker são usados para:

Persistência de Dados: Quando um contêiner é encerrado, os dados armazenados nele normalmente seriam perdidos. No entanto, ao usar volumes, você pode garantir que os dados sejam mantidos mesmo depois que o contêiner seja desligado, permitindo a persistência de bancos de dados, arquivos de configuração e outros dados importantes.

Compartilhamento de Dados: Volumes podem ser compartilhados entre múltiplos contêineres, permitindo que eles acessem os mesmos dados. Isso é útil para cenários em que você precisa compartilhar informações entre contêineres, como quando um contêiner gera arquivos e outro contêiner precisa processá-los.

Backup e Restauração: Volumes facilitam a realização de backups dos dados de um contêiner, tornando mais simples a tarefa de migrar ou restaurar dados em diferentes ambientes.

Isolamento dos Dados: Volumes permitem manter os dados isolados do sistema operacional host, contribuindo para uma separação limpa entre os componentes.

Integração com o Sistema Host: Volumes podem ser montados em caminhos específicos do sistema host, o que é útil para casos em que você deseja interagir diretamente com os dados do contêiner a partir do host.

Os volumes podem ser criados durante a criação do contêiner ou depois, sendo associados a ele. Eles podem ser usados para armazenar diretórios inteiros ou arquivos específicos. Além disso, existem diferentes tipos de volumes, como volumes de host, volumes nomeados e volumes de plug-in, que oferecem diferentes níveis de flexibilidade e gerenciamento.

Em resumo, os volumes no Docker são mecanismos essenciais para gerenciar dados de forma persistente e compartilhada entre contêineres e o sistema operacional host, tornando a arquitetura de aplicativos baseados em contêineres mais versátil e eficiente.

## Tipos de vomules?

No Docker, existem vários tipos de volumes que você pode usar para gerenciar dados persistentes e compartilhados entre contêineres e o sistema operacional host. Alguns dos principais tipos de volumes incluem:

Volumes de Host: Esses volumes são diretórios do sistema host que são montados diretamente em um contêiner. Isso permite que os dados sejam compartilhados entre o host e o contêiner. No entanto, essa abordagem pode ser menos portátil, pois os caminhos do sistema host são específicos para a máquina em que os contêineres estão sendo executados.

Volumes Nomeados: Os volumes nomeados são volumes independentes do sistema de arquivos do host e têm um nome associado. Isso torna mais fácil referenciá-los em múltiplos contêineres. Os volumes nomeados são criados explicitamente e persistem mesmo depois que os contêineres são removidos.

Volumes de Plug-in: Alguns sistemas, como o Docker Swarm, oferecem suporte a plug-ins de volume que permitem estender a funcionalidade de gerenciamento de volumes. Isso pode ser útil em cenários específicos, como integração com sistemas de armazenamento externo.

Volumes do Serviço: No contexto de orquestração de contêineres, como o Docker Swarm ou o Kubernetes, os volumes do serviço são usados para compartilhar dados entre os nós do cluster e os contêineres do serviço. Isso garante que os dados persistam e estejam acessíveis, mesmo que o serviço seja movido entre nós.

Volumes Temporários: Esses volumes são criados automaticamente quando um contêiner é iniciado e são excluídos quando o contêiner é encerrado. Eles são úteis para armazenar dados temporários ou específicos de um único contêiner.

Cada tipo de volume tem suas próprias vantagens e casos de uso específicos. A escolha do tipo de volume dependerá das necessidades do seu aplicativo e do ambiente em que ele será executado.

[Click aqui para voltar para o topo](https://github.com/cairodasilvapinto/bolsaCOMPASS/blob/main/README.md#apresenta%C3%A7%C3%A3o)
