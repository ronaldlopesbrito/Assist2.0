from flask import Flask, jsonify, request
app = Flask('assist2.0')
@app.route('/score', methods=['POST'])
def score():
    # Recebe os dados enviados na requisição
    data = request.get_json()
# Definindo as perguntas do questionário 
questions = [
    "1. Em que momento de sua vida você usou drogas pela primeira vez?",
    "2. Quantas vezes você usou drogas nos últimos três meses?",
    "3. Você tem problemas de saúde relacionados ao uso de drogas?",
    "4. Você tem algum problema físico ou mental devido ao uso de drogas?",
    "5. Alguém já sugeriu que você pare de usar drogas?",
    "6. Você já se sentiu mal ou com remorso depois de usar drogas?",
    "7. Você já usou drogas mais do que pretendia?",
    "8. Você já teve perda de memória após usar drogas?"
]

# Definindo as opções de resposta
options = [
    	["Nunca", 
	"Há mais de um ano", 
	"No último ano", 
	"No último mês"],
    	["Nenhuma", 
	"De uma a três vezes", 
	"De quatro a seis vezes", 
	"Mais do que seis vezes"],
	["Não", 
	"Sim, mas não agora", 
	"Sim, nos últimos meses", 
	"Sim, nos últimos dias"],
    	["Não", 
	"Sim, mas não agora", 
	"Sim, nos últimos meses", 
	"Sim, nos últimos dias"],
	["Não", 
	"Sim, mas não agora", 
	"Sim, nos últimos meses", 
	"Sim, nos últimos dias"],
	["Não", 
	"Sim, mas não agora", 
	"Sim, nos últimos meses", 
	"Sim, nos últimos dias"],
    	["Não", 
	"Sim, mas não agora", 
	"Sim, nos últimos meses", 
	"Sim, nos últimos dias"],
	["Não", 
	"Sim, mas não agora", 
	"Sim, nos últimos meses", 
	"Sim, nos últimos dias"]
]

# Definindo as pontuações
scores = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 2, 3, 4]
]

# Iniciando a pontuação do Score ASSIST 2.0
score = 0

# Exibindo as perguntas do questionário e calculando a pontuação
for i in range(8):
    print(questions[i])
    print("0 - " + options[i][0])
    print("1 - " + options[i][1])
    print("2 - " + options[i][2])
    print("3 - " + options[i][3])
    answer = int(input("Insira o número da resposta correta: "))
    score += scores[i][answer]

# Definindo as mensagens de orientação
low_risk_message = "Sua pontuação indica um baixo risco de problemas relacionados ao uso de drogas. Continue a manter hábitos saudáveis!"
moderate_risk_message = "Sua pontuação indica um risco moderado de problemas relacionados ao uso de drogas. Recomendamos que você procure um profissional de saúde para uma avaliação mais detalhada."
high_risk_message = "Sua pontuação indica um alto risco de problemas relacionados ao uso de drogas. É altamente recomendável que você procure ajuda especializada o mais rápido possível."

# Categorizando o risco e exibindo a mensagem de orientação apropriada
if score <= 3:
    message = low_risk_message
elif score >= 4 and score <= 26:
    message = moderate_risk_message
else:
    message = high_risk_message
    
response = {'risk_category': message}
print(response)

@app.route('/score', methods=['POST'])
def score():
    # Recebe os dados enviados na requisição
    data = request.get_json()

    # Extrai as respostas do questionário dos dados recebidos
    answers = [data['q1'], data['q2'], data['q3'], data['q4'], data['q5'], data['q6'], data['q7'], data['q8']]

    # Calcula a pontuação com base nas respostas
    score = 0
    for i in range(8):
        score += scores[i][answers[i]]

    # Define a mensagem de orientação com base na pontuação
    if score <= 3:
        message = low_risk_message
    elif score >= 4 and score <= 26:
        message = moderate_risk_message
    else:
        message = high_risk_message

    # Retorna a pontuação e mensagem de orientação como um objeto JSON
    return jsonify({'score': score, 'message': message})
if __name__ == '__main__':
    app.run()
