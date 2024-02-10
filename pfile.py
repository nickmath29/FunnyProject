from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_option = request.form['option']
        if selected_option == 'No':
            return redirect(url_for('index'))  # Redirect to the index page to choose options again
        else:
            return render_template('thanks.html', selected_option=selected_option)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

