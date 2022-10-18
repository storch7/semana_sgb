const card_cristiano_question = document.querySelector('.card_face-front-c h2');

card_cristiano_question.addEventListener('click', function () {

    var questions = new Map();

    questions.set(0, {pergunta: "As normas de segurança de alimentos se aplicam desde os nossos fornecedores homologados e finalizam no consumo do produto pelo cliente final.", resposta:"Verdadeiro"});

    questions.set(1, {pergunta: "Situação hipotética: um colaborador adentrou na área de envase sem o uso de touca e não higienizou as mãos. Sabendo do ocorrido, seu gestor imediato o orientou que, quando fosse possível, realizasse a higienização das mãos; disse ainda qaue o uso de touca seria opcional, já que o serviço prestado seria inferior a 30 minutos. Com base no contexto descrito, podemos classificar a conduta do gestor como positiva.", resposta: "Falso"});

    questions.set(2, {pergunta: "O conceito principal de segurança de alimentos é entregar o produto para o cliente final livre de potenciais contaminações.", resposta: "Verdadeiro"});

    questions.set(3, {pergunta: "A assimilação da cultura de segurança de alimentos é de responsabilidade apenas daquele que os manipula, não sendo necessário a expansão para o restante da cadeia produtiva.", resposta: "Falso"});

    questions.set(4, {pergunta: "O consumo de alimentos em área de processo e nos corredores da fábrica é totalmente aceito; a probabilidade de o alimento cair dentro de uma garrafa na linha de envase ou de haver contaminação é mínima.", resposta: "Falso"});

    questions.set(5, {pergunta: "A disseminação da cultura de segurança de alimentos é de responsabilidade apenas do manipulador dos alimentos, não sendo necessário a expansão para o restante da cadeia produtiva.", resposta: "Falso"});

    questions.set(6, {pergunta: "A variação de temperatura para garrafas pet não altera as características físico-químicas na composição final dos produtos.", resposta: "Falso"});

    questions.set(7, {pergunta: "A correta armazenagem de produtos finais deve seguir as seguintes diretrizes: (i) conservar ao abrigo do sol e calor, em local limpo e seco, arejado e sem odor e (ii) não congelar.", resposta: "Verdadeiro"});

    questions.set(8, {pergunta: "É correto afirmar que um produto com contaminação biológica é seguro para consumo.", resposta: "Falso"});

    questions.set(9, {pergunta: "Fornecer ao mercado produtos seguros e buscar melhoraria continua de seus processos são itens que fazem parte da Política de Segurança de Alimentos.", resposta: "Verdadeiro"});

    questions.set(10, {pergunta: "A contaminação física, química e biológica do produto pode representar efeito adverso à saúde do consumidor", resposta: "Verdadeiro"});

    questions.set(11, {pergunta: "Um dos conceitos de Segurança de Alimentos é cuidar da saúde das pessoas.", resposta: "Verdadeiro"});

    questions.set(12, {pergunta: "São itens fundamentais para prevenir e reduzir os perigos a segurança de alimentos: higiene, organização e limpeza.", resposta: "Verdadeiro"});

    questions.set(12, {pergunta: "'Não consumir alimento fora das áreas designadas e não os guardar em locais impróprios' é uma das regra de ouro referente a segurança de alimentos", resposta: "Verdadeiro"});

    questions.set(13, {pergunta: "Um dos objetivos da Segurança de Alimentos é zelar pela da saúde das pessoas/consumidores.", resposta: "Verdadeiro"});

    questions.set(14, {pergunta: "Deitar ou sentar na grama e depois acessar as áreas de manipulação de alimentos ou armazenagem de ingredientes é uma conduta vista como correta.", resposta: "Falso"});

    questions.set(15, {pergunta: "Os pacotes de refrigerantes devem ser armazenados diretamente no chão, não sendo necessário o uso de pallets.", resposta: "Falso"});

    questions.set(16, {pergunta: "É permitido lanchar e dormir no espaço ZEN.", resposta: "Falso"});

    questions.set(17, {pergunta: "Devo lavar as mãos somente uma vez ao dia; fazê-lo mais de uma vez implica no ressecamento da pele e não é saudável.", resposta: "Falso"});

    questions.set(18, {pergunta: "Restos de comida atraem pragas (baratas, ratos e moscas), que podem contaminar os produtos.", resposta: "Verdadeiro"});

    questions.set(19, {pergunta: "Sol e chuva podem danificar as embalagens, alterando características do produto - como gosto, odor e aparência -, afetando a segurança do alimento.", resposta: "Verdadeiro"});

    questions.set(20, {pergunta: "A política de segurança de alimentos não garante totalmente um alimento seguro no mercado.", pergunta: "Verdadeiro"});

    questions.set(21, {pergunta: "Sempre que falamos de segurança de alimentos, estamos nos referindo única e exclusivamente a produtos livres de contaminações.", resposta:"Falso"});

    questions.set(22, {pergunta: "São exemplos de boas práticas de armazenagem: armazenar as embalagens diretamente no chão e armazenar produtos próximos de químicos.", resposta: "Falso"});

    questions.set(23, {pergunta: "As DTAs (Doença Transmitidas por Alimentos) são ocasionadas somente por falta de higiene das mãos.", resposta: "Falso"});

    questions.set(24, {pergunta: "Devemos higienizar as mãos sempre que acessarmos as áreas de processo (fabricação e produção).", resposta: "Verdadeiro"});

    questions.set(25, {pergunta: "Nas áreas administrativas, onde é permitida a alimentação, pode-se deixar o copo de café em qualquer local, já que não há risco de atrair pragas.", resposta: "Falso"});

    questions.set(26, {pergunta: "Ao higienizar as mãos posso secá-las na minha roupa.", resposta: "Falso"});

    questions.set(27, {pergunta: "Todos os colaboradores são responsáveis pela limpeza do ambiente.", resposta: "Verdadeiro"});

    questions.set(28, {pergunta: "Os produtos químicos devem ser mantidos com acesso restrito e devem estar dentro do prazo de validade.", resposta: "Verdadeiro"});
    
    function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min) + min);
    }

    var indexQuestion = getRandomInt(0, 29);
    var dados = questions.get(indexQuestion);

    var imprimir = document.getElementById('imprimir_c');
    imprimir.innerHTML = dados.pergunta;

    const cristiano_true = document.querySelector('.alternativa_label_t_c');
    cristiano_true.addEventListener('click', function () {
        if (dados.resposta == "Verdadeiro") {
            alert("Resposta correta!");
            document.location.reload(true);
        }
        else {
            alert("Resposta incorreta!");
            document.location.reload(true);
        }
    });

    const cristiano_false = document.querySelector('.alternativa_label_f_c');
    cristiano_false.addEventListener('click', function () {
        if (dados.resposta == 'Falso') {
            alert("Resposta correta!");
            document.location.reload(true);
        }
        else {
            alert("Resposta incorreta!");
            document.location.reload(true);
        }
    });
});