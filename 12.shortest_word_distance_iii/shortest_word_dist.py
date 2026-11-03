#wordsDict = ["the", "quick", "brown", "fox", "quick"]
#word1 = "quick", word2 = "fox"

def shortest_word_distance_iii(words_dict: list[str], word1: str, word2: str) -> int:
    if len(words_dict) == 1:
        return 0
    word1_ind = -1
    word2_ind = -1
    min = 10000000
    
    if word1 == word2:
        cnt = 0
        for i in range(0, len(words_dict)):
            if words_dict[i] == word1:
                if cnt == 0 or cnt % 2 == 0:
                    word1_ind = i
                else:
                    word2_ind = i
                if word1_ind != -1 and word2_ind != -1:
                    if abs(word1_ind - word2_ind) < min:
                        min = abs(word1_ind - word2_ind)
                cnt += 1
    else:
        for i in range(0, len(words_dict)):
            if words_dict[i] == word1:
                word1_ind = i
                if word2_ind != -1:
                    if abs(word1_ind - word2_ind) < min:
                        min = abs(word1_ind - word2_ind)
            elif words_dict[i] == word2:
                word2_ind = i
                if word1_ind != -1:
                    if abs(word1_ind - word2_ind) < min:
                        min = abs(word1_ind - word2_ind)
    return min

if __name__ == "__main__":
    words_dict = input().split()
    word1 = input()
    word2 = input()
    res = shortest_word_distance_iii(words_dict, word1, word2)
    print(res)
