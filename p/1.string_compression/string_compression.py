class Solution:
    def compress(self, chars: list[str]) -> int:

        n = len(chars)

        read = 0
        write = 0

        while read < n:
            start = read
            ch = chars[read]
            while read < n and chars[read] == chars[start]:
                read += 1
            
            count = read - start

            chars[write] = ch
            write += 1
            if count > 1:
                for s in str(count):
                    chars[write] = s
                    write += 1
            
        return write
