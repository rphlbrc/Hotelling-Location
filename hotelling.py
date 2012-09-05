import sys

scale = []

def initPositions(numPos):
	scale = [x for x in range(numPos)]

def parse(line):
	words = line.split()

def main():
	scale = [x for x in range(int(sys.argv[1]))]
	line = ""
	while (line = raw_input('>')):
		parse(line)

if __name__ == '__main__':
	main()