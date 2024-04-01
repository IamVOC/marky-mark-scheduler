from celery import Celery


app = Celery('main', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


def main() -> None:
    pass

if __name__ == '__main__':
    pass
