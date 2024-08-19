from sistema import SistemaPrincipal

def main():
    sys = SistemaPrincipal()
    core = True
    while core:
        core = sys.menu()
    pass


if __name__ == '__main__':
    main()