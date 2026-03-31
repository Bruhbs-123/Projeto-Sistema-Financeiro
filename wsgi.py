from src.financeiro import create_app

app = create_app()

# ESTA PARTE É O QUE FAZ O SERVIDOR LIGAR:
if __name__ == "__main__":
    app.run(debug=True)