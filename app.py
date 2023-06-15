from flask import Flask, render_template, request

  
app = Flask(__name__)

def gauss_jordan(matrix):
    pass

@app.route('/')
def index():
    return render_template('index.html')
   
@app.route('/solve', methods=['POST'])
def solve():
   matrix = request.form.getlist('matrix[]')

   # Convert the coefficients into a matrix of numbers
   matrix = [list(map(float, row.split(','))) for row in matrix]

   # Call the Gauss-Jordan function to solve the system of equations or find the inverse matrix
   result = gauss_jordan(matrix)

   # Render the result template and pass the result as an argument
   return render_template('result.html', result=result)

if __name__ == '__main__':
   app.run(debug=True)

