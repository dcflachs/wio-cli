from time import sleep
import click
import threading

class waiting_echo(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.exiting=False
        self.flag = True
    def run(self):
        while not self.exiting:
            click.echo("\r-%s" %self.msg, nl=False)
            click.echo(" "*(80-len(self.msg)), nl=False)
            click.echo("\b"*(80-len(self.msg)), nl=False)
            sleep(0.1)
            click.echo("\r\%s" %self.msg, nl=False)
            click.echo(" "*(80-len(self.msg)), nl=False)
            click.echo("\b"*(80-len(self.msg)), nl=False)
            sleep(0.1)
            click.echo("\r|%s" %self.msg, nl=False)
            click.echo(" "*(80-len(self.msg)), nl=False)
            click.echo("\b"*(80-len(self.msg)), nl=False)
            sleep(0.1)
            click.echo("\r/%s" %self.msg, nl=False)
            click.echo(" "*(80-len(self.msg)), nl=False)
            click.echo("\b"*(80-len(self.msg)), nl=False)
            sleep(0.1)

        click.echo('\r' + " "*(80-len(self.msg)), nl=False)
        click.echo('\r', nl=False)
    def message(self, msg):
        self.msg = msg
    def stop(self, msg):
        self.exiting = True
        self.msg = msg

def tree(list):
    if not list:
        click.echo('No Wio devices could be found.')
        return
    for l in list[:-1]:
        click.echo('|-- ', nl=False)
        if l['online']:
            click.secho(l['name'] + ' (%s) [%s]' %(l['onoff'], l['board'].split()[1]), fg='green')
        else:
            click.secho(l['name'] + ' (%s) [%s]' %(l['onoff'], l['board'].split()[1]), fg='cyan')
        click.echo('|   |-- ', nl=False)
        click.echo('sn: ' + l['node_sn'])
        click.echo('|   |-- ', nl=False)
        click.echo('token: ' + l['node_key'])
        click.echo('|   |-- ', nl=False)
        click.echo('API url: ' + l['resources'])
        click.echo('|   |-- ', nl=False)
        click.echo('APIs: ')
        for api in l['well_known']:
            click.echo('|       |-- ', nl=False)
            click.echo(api)

    l = list[-1]
    click.echo('|-- ', nl=False)
    if l['online']:
        click.secho(l['name'] + ' (%s) [%s]' %(l['onoff'], l['board'].split()[1]), fg='green')
    else:
        click.secho(l['name'] + ' (%s) [%s]' %(l['onoff'], l['board'].split()[1]), fg='cyan')
    click.echo('    |-- ', nl=False)
    click.echo('sn: ' + l['node_sn'])
    click.echo('    |-- ', nl=False)
    click.echo('token: ' + l['node_key'])
    click.echo('    |-- ', nl=False)
    click.echo('API url: ' + l['resources'])
    click.echo('    |-- ', nl=False)
    click.echo('APIs: ')
    for api in l['well_known']:
        click.echo('        |-- ', nl=False)
        click.echo(api)
