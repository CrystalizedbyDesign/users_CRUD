from flask import Flask, render_template, request, redirect

from users import User

app = Flask('__name__')


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    print("####################################33")
    return render_template("read_all.html", users=User.get_all())

@app.route('/users/new')
def new():
    print("******************************22")
    return render_template("new_user.html")



@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    print("################################44")
    User.save(request.form)
    return redirect('/users')

@app.route('/user/<int:id>/edit')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit.html", user=User.get_one_user(data))


@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("users.html", user=User.get_one_user(data)) #Here corresponds to the data you are submitting


@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        "id":id
    }
    
    User.delete(data)
    return redirect('/users')





if __name__=="__main__":
    app.run(debug=True)