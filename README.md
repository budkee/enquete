# EnquetApp: descubra, opine e compartilhe!

## Visão Geral

**EnquetApp** é um aplicativo inovador que visa transformar a maneira como as pessoas interagem com enquetes e pesquisas. Com uma interface intuitiva e amigável, o EnquetApp oferece uma plataforma digital envolvente para criar, compartilhar e participar de enquetes sobre uma variedade de tópicos, desde questões sociais e políticas até preferências pessoais e tendências culturais.

## Sobre o Negócio
### Modelo de Negócio

O EnquetApp adota um modelo de negócio freemium, oferecendo funcionalidades básicas gratuitas para todos os usuários, com a opção de atualização para uma assinatura premium para recursos avançados.

Aqui estão os principais componentes do modelo de negócio:

1. **Versão Gratuita:**
   - **Criação de Enquetes Básicas:** Os usuários podem criar enquetes simples com opções de resposta limitadas.
   - **Participação em Enquetes Públicas:** Os usuários podem participar de enquetes públicas e ver os resultados gerais.
   - **Perfil Pessoal:** Cada usuário tem um perfil básico para acompanhar suas enquetes criadas e participadas.

2. **Assinatura Premium:**
   - **Enquetes Avançadas:** Recursos aprimorados de criação de enquetes, incluindo múltiplas opções de resposta, perguntas condicionais e design personalizado.
   - **Análises Detalhadas:** Insights detalhados sobre os resultados das enquetes, incluindo gráficos, estatísticas e tendências.
   - **Enquetes Privadas:** Capacidade de criar enquetes privadas para um grupo seleto de pessoas ou para uso corporativo.
   - **Remoção de Anúncios:** Experiência livre de anúncios para uma navegação mais fluida e sem interrupções.

3. **Receita:**
   - **Assinaturas Premium:** Os usuários podem optar por planos mensais ou anuais para desbloquear os recursos premium.
   - **Publicidade Direcionada:** Parcerias com empresas interessadas em promover produtos e serviços por meio de enquetes segmentadas.
   - **Colaborações Corporativas:** Ofertas personalizadas para empresas que desejam usar o EnquetApp para pesquisas internas, feedback de funcionários e análises de mercado.

### Segmento de Mercado

O EnquetApp tem como alvo um amplo espectro de usuários, incluindo:

- **Indivíduos Curiosos:** Pessoas interessadas em saber a opinião pública sobre diversos assuntos, desde entretenimento até questões sociais.
  
- **Profissionais de Marketing e Pesquisadores:** Para realizar pesquisas de mercado, coletar feedback do público-alvo e testar ideias rapidamente.
  
- **Empresas e Instituições:** Para coletar feedback dos funcionários, envolver clientes em pesquisas de satisfação e criar enquetes para tomadas de decisão internas.

### Estratégias de Crescimento

1. **Marketing Digital:**
   - Campanhas nas redes sociais para aumentar a conscientização sobre o EnquetApp.
   - Parcerias com influenciadores digitais e bloggers para revisões e recomendações.
   - Anúncios segmentados online para alcançar públicos específicos.

2. **Engajamento da Comunidade:**
   - Desafios de enquetes semanais com prêmios para incentivar o uso regular do aplicativo.
   - Recompensas para usuários que convidarem amigos e familiares para se juntarem ao EnquetApp.

3. **Desenvolvimento Contínuo:**
   - Introdução de novos recursos com base no feedback dos usuários.
   - Aperfeiçoamento da experiência do usuário para uma navegação intuitiva e agradável.

4. **Parcerias Estratégicas:**
   - Colaborações com instituições educacionais para uso em salas de aula e pesquisas acadêmicas.
   - Alianças com empresas de mídia para enquetes exclusivas em eventos e programas.

### Vantagens Competitivas

1. **Interface Intuitiva e Atraente:** Uma experiência de usuário moderna e fácil de usar, desde a criação até a participação nas enquetes.

2. **Recursos Avançados de Análise:** Insights detalhados e estatísticas precisas para uma compreensão aprofundada dos resultados das enquetes.

3. **Versatilidade de Uso:** Flexibilidade para enquetes pessoais, profissionais e corporativas, atendendo a uma variedade de necessidades.

4. **Segurança e Privacidade:** Proteção dos dados do usuário e opções para enquetes públicas e privadas para garantir a confidencialidade quando necessário.

O EnquetApp visa se tornar o principal destino para criar, compartilhar e descobrir opiniões em tempo real sobre uma infinidade de tópicos, oferecendo uma plataforma envolvente que une pessoas por meio da participação ativa em pesquisas e enquetes.

## Desenvolvimento

### Models

> Análogo aos Relacionamentos do Banco de Dados. [Aqui](./enquete/models.py) eles se apresentam como classes que por sua vez contém métodos e atributos.

- `Question()`: tabela das perguntas, contendo o texto das perguntas e a data de publicação.

- `Choice()`: tabela das respostas, contendo a pergunta, o texto da resposta e o número de votos.

### Views

> Cada `view` representa uma interface ou conteúdo a ser disponibilizado ao usuário e é representado por uma função ou método `class-based views`.

- Página de “índice” de enquetes - exibe as enquetes mais recente.
- Página de “detalhes” da pergunta – exibe o testo da pergunta, com um formulário para votar.
- Página de “resultados” de perguntas - exibe os resultados de uma pergunta em particular.
- Ação de voto - gerencia a votação para uma escolha particular em uma enquete em particular.

### Criando a interface do admin

   python manage.py createsuperuser

## Próximas Melhorias

- [] Template para Detalhes
- [] Template para Resultados
- [] Template para Votação

## Links e Referências

- [Django App | Part. 01](https://docs.djangoproject.com/pt-br/5.0/intro/tutorial01/)
- [Django App | Part. 02](https://docs.djangoproject.com/pt-br/5.0/intro/tutorial02/)
- [Django App | Part. 03](https://docs.djangoproject.com/pt-br/5.0/intro/tutorial03/#raising-a-404-error)
