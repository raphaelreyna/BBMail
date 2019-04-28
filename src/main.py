from BBMail import BBMail
import time

if __name__ == "__main__":
    bbmail = BBMail('foo')
    while True:
        bbmail.run()
        time.sleep(5)
