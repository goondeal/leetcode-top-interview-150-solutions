"""[[ HARD ]]"""
from typing import List


class Solution:
    def _format_line(self, words: List[str], words_length, max_width):
        num_of_spaces = len(words) - 1
        space = max_width - words_length
        # Place available spaces as evenly as possible
        if space and num_of_spaces:
            space_size, space_mod = divmod(space, num_of_spaces)
            spaces = ['']  # to be as the same length as words
            spaces += [' ' * space_size] * num_of_spaces
            # Distribute as evenly as possible, with advantage to the left.
            if space_mod:
                for i in range(space_mod):
                    spaces[i+1] += ' '
            # Merge words with spaces and join them.
            result = [spaces[i] + words[i] for i in range(len(words))]
            return ''.join(result)

        return ' '.join(words).ljust(max_width)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        Approach:
            First, determine the words that will be in each line,
            Then adjust spaces and justification for each line of words to fulfill the conditions.

        Time Complexity: O(n) 
        Space Complexity: O(n)
        '''
        n = len(words)
        result = []
        line_words = []
        line_words_length = 0
        i = 0
        while i < n:
            s = len(words[i])
            # Collect words till their total length (with minimum spaces required for concatenation) exceeds maxWidth.
            if line_words_length + s + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_words_length += s
                i += 1
            else:
                # If a line of words was collected, adjust the line.
                result.append(self._format_line(
                    line_words, line_words_length, maxWidth))
                line_words = []
                line_words_length = 0
        if line_words:
            result.append(' '.join(line_words).ljust(maxWidth))

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fullJustify(["This", "is", "an", "example",
          "of", "text", "justification."], maxWidth=16))
    print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], maxWidth=16))
