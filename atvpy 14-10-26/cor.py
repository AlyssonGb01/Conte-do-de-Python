import turtle

# Configuração inicial da janela
tela = turtle.Screen()
tela.title("Coração com E & M")
tela.setup(width=600, height=600)
tela.bgcolor("white")

# Configuração da tartaruga (pincel)
t = turtle.Turtle()
t.speed(3)
t.hideturtle()

# --- DESENHANDO O CORAÇÃO ---
t.penup()
t.goto(0, -150)  # Posição inicial (ponto inferior do coração)
t.pendown()

t.color("red")
t.begin_fill()

# Lado esquerdo do coração
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(1.2)

# Lado direito do coração
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(1.2)
t.forward(224)

t.end_fill()

# --- ESCREVENDO AS LETRAS CENTRALIZADAS ---
t.penup()
# Posiciona o pincel um pouco abaixo do centro geométrico para alinhar o texto
t.goto(0, -25)  
t.color("white")

# Alinhamento 'center' garante que o texto fique perfeitamente no meio
t.write("E M", align="center", font=("Arial", 40, "bold"))

# Mantém a janela aberta até que você clique nela
tela.exitonclick()
