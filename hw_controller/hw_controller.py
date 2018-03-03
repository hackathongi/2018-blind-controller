import click


@click.command()
@click.option('--elem_id', type=int, help="Objective  HW element id")
def main (elem_id):
    print elem_id


if __name__ == '__main__':
    main()