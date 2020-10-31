
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':