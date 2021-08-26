class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_count = {}
        paragraph = re.sub('[\W]',' ',paragraph.lower())
        word_list = paragraph.split(' ')
        for x in word_list:
            if(not(x in banned or x == '')):
                if(not(x in word_count)):
                    word_count[x] = 0
                word_count[x] += 1

                    
        return sorted(word_count.items(),key=lambda item: item[1],reverse=True)[0][0]
        