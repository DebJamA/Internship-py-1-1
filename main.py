from simcoblog import create_app

simcoblog = create_app()

if __name__ == "__main__":
    simcoblog.run(debug=False)
