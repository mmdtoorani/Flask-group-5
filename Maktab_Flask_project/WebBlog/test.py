if request.method == "POST":
    username_form = request.form["username"]
    password_form = request.form["password"]
    error = None
    if User.objects(username=username_form):
        user = User.objects(username=username_form)[0]
        if (str(hash(password_form)) != user.password):
            error = "Incorrect password."
    else:
        error = "Incorrect username."
    if error is None:
        session.clear()
        session['username'] = request.form['username']
        return redirect(url_for("blog.home"))
    flash(error)
return render_template("login.html")
