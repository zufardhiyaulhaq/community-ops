import click

@click.command()
def version():
    click.echo("v1.0.0")
