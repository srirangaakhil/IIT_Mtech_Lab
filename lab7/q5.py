import glob
import os

keyword_file = './data/heroes.txt'
corpus = './data/avengers_Universe/*.txt'
dest = './data/survivors_of_snap/'

if __name__ == '__main__':
	keyword_file_ptr = open(keyword_file, "r")
	keywords = []
	for line in keyword_file_ptr:
		if line: keywords.append(line)
	keyword_file_ptr.close()

	if not os.path.exists(dest):
		os.mkdir(dest)

	for file in glob.glob(corpus):
		file_ptr = open(file)
		for line in file_ptr:
			found = ''
			for keyword in keywords:
				if keyword in line:
					found = keyword
					file_ptr.close()
					os.rename(file, dest + file.split('/')[-1])
					break
			if found:
				keywords.remove(found)
				break 
