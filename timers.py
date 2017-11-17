import click
import re
import time
from datetime import datetime, timedelta


def stopTimer():
    start_time = datetime.now()
    while True:
        time.sleep(1)
        delta_time = datetime.now() - start_time
        print("\r[ST] {}".format(str(delta_time).split('.')[0]), end="")


def Time():
    while True:
        time.sleep(1)
        print("\r [TIME](24h) {}".format(datetime.now().strftime('%H:%M:%S')), end="")


def Timer(stop_time):
    """
    Format:     '15:14:12'
    :param stop_time:
    :return:
    """

    time_pattern = re.compile(r'^(?P<hour>[0-5][0-9]){0,1}:{0,1}(?P<min>[0-5][0-9]){1}:{1}(?P<sec>[0-5][0-9])$')
    time_match = time_pattern.match(stop_time)
    hour_num, min_num, sec_num = [int(i) for i in time_match.groups()]

    timer = timedelta(hours=hour_num, minutes=min_num, seconds=sec_num)
    while True:
        time.sleep(1)
        timer = timer - timedelta(seconds=1)
        print("\r [TR] {}".format(timer), end="")


@click.group()
def cli():
    pass


@click.command()
def t():
    Time()


@click.command()
def st():
    stopTimer()


@click.command()
@click.argument('time')
def tr(time):
    Timer(time)


cli.add_command(t)
cli.add_command(tr)
cli.add_command(st)

if __name__ == '__main__':
    cli()
