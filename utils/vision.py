import subprocess

class Vision:

    def __init__ (self, executablePath):
        self.exec = executablePath

    def get_distance (self):
        distance = subprocess.run(f'./{self.exec}', capture_output=True)
        return float(distance.stdout.decode('utf-8'))

if __name__ == "__main__":
    v = Vision('a')
    print(v.get_distance())