import json
import copy

def rotate_matrix(matrix):
	k = 0
	new_matrix = copy.deepcopy(matrix)
	if len(matrix) > 1:
		if len(matrix[0]) == 1:
			new_matrix[0][0] = matrix[1][0]
			new_matrix[1][0] = matrix[0][0]
		else:
			for j in range(len(matrix[0]) - 1, -1, -1):
				for i in range(len(matrix)):
					new_matrix[i][k] = matrix[j][i]
				k += 1
	return new_matrix

if __name__ == "__main__":
    input_str = input()
    matrix = json.loads(input_str)
    answer = rotate_matrix(matrix)
    
    print(json.dumps(answer))
