from flask import Flask, render_template
appe = Flask(__name__)
@appe.route('/')
def foot():
    return render_template('index.html')

if __name__ =='__main__':
    appe.run(debug=True)
    #ergerg