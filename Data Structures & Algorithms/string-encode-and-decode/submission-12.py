class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'é'
        elif len(strs) > 0:
            return "á".join(strs)
        else:
            return ''

    def decode(self, s: str) -> List[str]:
        if s == 'é':
            return []
        if len(s) > 0:
            return s.split("á")     
        else:
            return ['']
