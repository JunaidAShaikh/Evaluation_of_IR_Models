outFile = open('rev_output.txt','w')
open('rev_output.txt', 'w').close()
parsed_file = open('BM25/BM25parsed.txt','r')

open('rev_output.txt','a')
with open('qrel.txt', encoding="utf-8") as inputFile:
	for line in inputFile:
		rel = line.split(' ') 
		outputLine = ''
		if int(rel[3]) >= 1:
			outputLine += line + '||'
			outputLine = outputLine.replace('\n', ' ')
			parsed_file = open('BM25/BM25parsed.txt','r')
			for parsed_line in parsed_file:
				split_parsed_line = parsed_line.split(' ')
				docid = split_parsed_line[2]
				queryid = split_parsed_line[0]
				if int(docid) == int(rel[2]) and rel[0] == queryid:
					outputLine += parsed_line
					outFile.write(outputLine)
			parsed_file.close()


	outFile.close()