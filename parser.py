def parse_message(text):
	result_hash = {}	
	splitted_text = text.split(',')
	for idx, element in enumerate(splitted_text):
		splitted_element = element.split(': ')
		if 'direction' in element:
			result_hash['direction'] = [float(splitted_element[1][1:]), float(splitted_text[idx+1]), float(splitted_text[idx+2][:-1])] 
		if 'type' in element:
			result_hash['type'] = splitted_element[1]
		if 'speed' in element:
			result_hash['speed'] = float(splitted_element[1].split(' ')[0])
	return result_hash
